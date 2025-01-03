# git-clone-group

A command line tool to clone/pull all projects from GitLab groups and their subgroups.

## Features

- Clone all repositories from a GitLab group
- Automatically handle subgroups
- Pull updates for existing repositories
- Show progress with nice progress bars
- Support both HTTP and SSH URLs
- Support private GitLab instances

## Installation

You can install git-clone-group using pip:

```bash
pip install git-clone-group
```

## Usage

Basic usage:

```bash
gcg -g GITLAB_ADDR -t TOKEN -i GROUP_ID [-d DEST_DIR]
```

Show help:
```bash
gcg -h
```

Examples:
```bash
# Clone all projects from group ID 123 to current directory
gcg -g gitlab.com -t glpat-xxxxxxxxxxxx -i 123

# Clone to a specific directory
gcg -g gitlab.com -t glpat-xxxxxxxxxxxx -i 123 -d /path/to/repos

# Clone from private GitLab instance
gcg -g git.company.com -t glpat-xxxxxxxxxxxx -i 456 -d ./projects
```

## Getting a GitLab Access Token

1. Log in to your GitLab instance
2. Go to Settings > Access Tokens
3. Create a new personal access token with `api` scope
4. Copy the token and use it with the `--token` argument

## Getting a Group ID

You can find the group ID in GitLab:

1. Go to your group's page
2. The group ID is shown in the group information panel
3. Or look at the URL: `https://gitlab.com/groups/your-group-name` - the group ID will be visible in the group details

## Notes

- The tool will automatically handle nested subgroups
- For existing repositories, it will perform a git pull
- Progress bars show real-time cloning/pulling status
- Both HTTP and SSH URLs are supported (SSH recommended)
