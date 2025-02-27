#!/bin/bash
# auto_commit.sh: A simple script to add, commit, and push changes with a changelog.

# Ensure you have set up your git remote repository and configured credentials.

# Stage all changes
git add .

# Commit with a message passed as an argument or use a default message
COMMIT_MESSAGE=${1:-"Automated commit: updating GENESIS-1 modules"}
git commit -m "$COMMIT_MESSAGE"

# Push changes to the remote repository (assumes 'origin' and 'main' branch)
git push origin main

echo "Auto-commit complete. Commit message: $COMMIT_MESSAGE"