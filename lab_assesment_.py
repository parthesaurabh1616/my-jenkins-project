# -*- coding: utf-8 -*-
"""Lab Assesment .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E0UZM9Om6cwZ4nU11TIEQKDL0X5hwrES
"""

import subprocess

def run_command(command):
  try:
    subprocess.run(command, check = True, shell = True)
    print(f"Command executed successfully: {command}")
  except subprocess.CalledProcessError as e:
    print(f"Error executing command: {command}")

run_command('git init')

def configure_git_user():
  run_command('git config --global user.name "parthesaurabh1616"')
  run_command('git config --global user.email "saurabh.parthe.1@gmail.com"')

configure_git_user()

def git_commit_initial(commit_message):
    # Add all files to staging area
    run_command('git add .')

    # Check if there are changes to commit
    result = subprocess.run(['git', 'diff', '--cached', '--quiet'], capture_output=True)

    if result.returncode == 1:  # Means there are changes
        # Commit the files
        run_command(f'git commit -m "{commit_message}"')
    else:
        print("No changes to commit.")

git_commit_initial("Initial commit")

def push_to_remote(remote_url, branch = "main"):
  run_command(f'git remote add origin {remote_url}')

  run_command(f'git push -u origin {branch}')

push_to_remote("https://github.com/parthesaurabh1616/parthesaurabh1616")

def sync_with_remote():
  run_command('git pull origin main')

sync_with_remote()

def check_remote():
  run_command('git remote -v')

check_remote()

def check_branches():
  run_command('git branch -a')

check_branches()

def sync_with_remote():
  run_command('git pull origin main')

sync_with_remote()

def stash_changes():
    run_command('git stash')

stash_changes()
sync_with_remote()

def sync_with_remote():
    # Pull changes from remote
    run_command('git pull origin main')

sync_with_remote()

def create_branch(branch_name):
  run_command(f'git checkout -b {branch_name}')

create_branch("feature_branch")

def diff_between_branches(branch1, branch2):
  run_command(f'git diff {branch1} {branch2}')

diff_between_branches("main","feature_branch")

def view_git_logs():
  run_command('git log --oneline')

view_git_logs()

def revert_last_commit():
  run_command('git revert HEAD')

revert_last_commit()

