import json
import os
import shlex
import subprocess
from pathlib import Path
import requests
from urllib.request import urlopen
import argparse
from tqdm import tqdm
from typing import Set, List, Dict, Optional
import sys


def get_next(group_id: int, page: Optional[int] = None) -> None:
    """Get and process projects for a given group ID and page."""
    if page is None:
        page = 1
        
    url = gen_next_url(group_id, page)
    try:
        with urlopen(url) as response:
            projects = json.loads(response.read().decode())
    except Exception as e:
        tqdm.write(f"Error fetching projects for group {group_id}: {e}")
        return
        
    if not projects:
        return
        
    with tqdm(projects, desc=f"Group {group_id} - Page {page}") as pbar:
        for project in pbar:
            try:
                project_url = project["ssh_url_to_repo"]
                project_path = project["path_with_namespace"]
                full_path = Path(dest_dir) / project_path
                
                pbar.set_description(f"Processing {project_path}")
                
                if full_path.exists():
                    command = ["git", "-C", str(full_path), "pull"]
                    action = "Updating"
                else:
                    command = ["git", "clone", project_url, str(full_path)]
                    action = "Cloning"
                
                pbar.set_description(f"{action} {project_path}")
                result = subprocess.run(command, capture_output=True, text=True)
                
                if result.returncode == 0:
                    pbar.set_description(f"✓ {project_path}")
                else:
                    pbar.set_description(f"✗ {project_path}")
                    tqdm.write(f"Error in {project_path}: {result.stderr}")
                    
            except Exception as e:
                tqdm.write(f"Error processing {project_path}: {e}")
                
    get_next(group_id, page + 1)


def have_next_projects(group_id: int) -> bool:
    """Check if group has any projects."""
    url = gen_next_url(group_id)
    try:
        with urlopen(url) as response:
            projects = json.loads(response.read().decode())
            return bool(projects)
    except Exception as e:
        tqdm.write(f"Error checking projects for group {group_id}: {e}")
        return False


def get_sub_groups(parent_id: int) -> List[int]:
    """Get list of subgroup IDs for a parent group."""
    url = gen_subgroups_url(parent_id)
    try:
        with urlopen(url) as response:
            groups = json.loads(response.read().decode())
            return [group["id"] for group in groups]
    except Exception as e:
        tqdm.write(f"Error getting subgroups for {parent_id}: {e}")
        return []


def cal_next_sub_group_ids(parent_id: int) -> Set[int]:
    """Calculate all subgroup IDs recursively."""
    parent_list = set()
    sub_ids = get_sub_groups(parent_id)
    has_projects = have_next_projects(parent_id)

    if sub_ids:
        if has_projects:
            parent_list.add(parent_id)
        for sub_id in sub_ids:
            parent_list.update(cal_next_sub_group_ids(sub_id))
    elif has_projects:
        parent_list.add(parent_id)
        
    return parent_list


def download_code(parent_id: int) -> None:
    """Download code for a group and all its subgroups."""
    group_ids = cal_next_sub_group_ids(parent_id)
    tqdm.write(f'Found groups: {group_ids}')
    
    if have_next_projects(parent_id):
        group_ids.add(parent_id)
    
    with tqdm(group_ids, desc="Processing groups") as pbar:
        for group_id in pbar:
            pbar.set_description(f"Processing group {group_id}")
            get_next(group_id)


def gen_next_url(target_id: int, page: int = 1) -> str:
    """Generate URL for getting group projects."""
    return f"http://{gitlabAddr}/api/v4/groups/{target_id}/projects?page={page}&private_token={gitlabToken}"


def gen_subgroups_url(target_id: int) -> str:
    """Generate URL for getting subgroups."""
    return f"http://{gitlabAddr}/api/v4/groups/{target_id}/subgroups?private_token={gitlabToken}"


def gen_global_url() -> str:
    """Generate URL for getting all projects."""
    return f"http://{gitlabAddr}/api/v4/projects?private_token={gitlabToken}"


def add_user_to_group(group_id: int, user_id: int) -> None:
    """Add a user to a group with maintainer access."""
    headers = {"Private-Token": gitlabToken}
    data = {"user_id": user_id, "access_level": 50}
    response = requests.post(
        f"http://{gitlabAddr}/api/v4/groups/{group_id}/members",
        headers=headers,
        data=data,
    )
    if response.status_code == 201:
        print(f"User {user_id} added successfully to group {group_id}")
    else:
        print(f"Failed to add user {user_id} to group {group_id}:", response.json())


def update_user_level(group_id: int, user_id: int, level: int) -> None:
    """Update a user's access level in a group."""
    headers = {"Private-Token": gitlabToken}
    data = {"user_id": user_id, "access_level": level}
    response = requests.put(
        f"http://{gitlabAddr}/api/v4/groups/{group_id}/members/{user_id}",
        headers=headers,
        data=data,
    )
    if response.status_code == 200:
        print(f"User {user_id} updated successfully in group {group_id}")
    else:
        print(f"Failed to update user {user_id} in group {group_id}:", response.json())


def gen_group_url(page: int, per_page: int) -> str:
    """Generate URL for getting groups."""
    return f"http://{gitlabAddr}/api/v4/groups?private_token={gitlabToken}&page={page}&per_page={per_page}"


def download_global_code() -> None:
    """Download all accessible projects."""
    url = gen_global_url()
    try:
        with urlopen(url) as response:
            projects = json.loads(response.read().decode())
            
        if not projects:
            return
            
        for project in tqdm(projects, desc="Downloading projects"):
            try:
                project_url = project["ssh_url_to_repo"]
                project_path = Path(project["path_with_namespace"])
                
                if project_path.exists():
                    command = ["git", "-C", str(project_path), "pull"]
                else:
                    command = ["git", "clone", project_url, str(project_path)]
                    
                result = subprocess.run(command, capture_output=True, text=True)
                if result.returncode != 0:
                    tqdm.write(f"Error with {project_path}: {result.stderr}")
                    
            except Exception as e:
                tqdm.write(f"Error processing project: {e}")
                
    except Exception as e:
        tqdm.write(f"Error downloading projects: {e}")


def main(group_name: str) -> None:
    """Main function to handle group or global downloads."""
    if not group_name:
        download_global_code()
        return
        
    url = gen_group_url(1, 100)
    try:
        with urlopen(url) as response:
            groups = json.loads(response.read().decode())
            
        if not groups:
            return
            
        target_id = next(
            (group["id"] for group in groups if group["name"] == group_name),
            None
        )
        
        if target_id:
            download_code(target_id)
        else:
            print(f"Group {group_name} not found")
            
    except Exception as e:
        print(f"Error in main: {e}")


def add_ssh_key_to_user(user_id: int, title: str, key: str) -> None:
    """Add SSH key to a user's account."""
    headers = {"Private-Token": gitlabToken}
    data = {"title": title, "key": key}
    response = requests.post(
        f"http://{gitlabAddr}/api/v4/users/{user_id}/keys",
        headers=headers,
        data=data,
    )
    if response.status_code == 201:
        print(f"Key added successfully for user {user_id}")
    else:
        print(f"Failed to add key for user {user_id}:", response.json())


def add_user_to_project(project_id: int, user_id: int) -> None:
    """Add a user to a project with maintainer access."""
    headers = {"Private-Token": gitlabToken}
    data = {"user_id": user_id, "access_level": 40}
    response = requests.post(
        f"http://{gitlabAddr}/api/v4/projects/{project_id}/members",
        headers=headers,
        data=data,
    )
    if response.status_code == 201:
        print(f"User {user_id} added successfully to project {project_id}")
    else:
        print(f"Failed to add user {user_id} to project {project_id}:", response.json())


def cli() -> None:
    """Command line interface."""
    parser = argparse.ArgumentParser(
        description='Clone all projects from a GitLab group and its subgroups',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  gcg -g gitlab.com -t glpat-xxxx -i 123

  # With destination directory
  gcg -g gitlab.com -t glpat-xxxx -i 123 -d /path/to/repos

  # From private GitLab instance
  gcg -g git.company.com -t glpat-xxxx -i 456 -d ./projects

Notes:
  - The tool will automatically handle nested subgroups
  - For existing repositories, it will perform a git pull
  - Progress bars show real-time cloning/pulling status
  - Both HTTP and SSH URLs are supported (SSH recommended)
        """
    )
    
    parser.add_argument(
        '--gitlab-addr', '-g',
        required=True,
        help='GitLab server address (e.g. gitlab.com)'
    )
    parser.add_argument(
        '--token', '-t',
        required=True,
        help='GitLab private token (create from Settings > Access Tokens)'
    )
    parser.add_argument(
        '--group-id', '-i',
        required=True,
        type=int,
        help='GitLab group ID to clone (found in group page URL or settings)'
    )
    parser.add_argument(
        '--dest-dir', '-d',
        default='./',
        help='Destination directory for cloned repositories (default: current directory)'
    )
    
    # If no arguments are provided, print help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        print("\nError: No arguments provided. Please provide the required arguments.")
        sys.exit(1)
        
    try:
        args = parser.parse_args()
    except argparse.ArgumentError as e:
        parser.print_help()
        print(f"\nError: {str(e)}")
        sys.exit(1)
    
    global gitlabAddr, gitlabToken, dest_dir
    gitlabAddr = args.gitlab_addr
    gitlabToken = args.token
    dest_dir = args.dest_dir
    
    download_code(args.group_id)


if __name__ == '__main__':
    cli()
