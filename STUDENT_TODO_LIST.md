# GitHub Learning Todo List for Students

Welcome to your GitHub learning journey! This todo list will guide you through essential GitHub concepts and skills.

## Getting Started with Git & GitHub

### 1. Setup & Configuration
- [ ] Install Git on your computer
- [ ] Create a GitHub account
- [ ] Configure Git with your name and email
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```
- [ ] Set up SSH keys or Personal Access Token for authentication

### 2. Basic Git Commands
- [ ] Create your first repository (locally or on GitHub)
- [ ] Clone a repository
  ```bash
  git clone <repository-url>
  ```
- [ ] Check repository status
  ```bash
  git status
  ```
- [ ] Add files to staging area
  ```bash
  git add <filename>
  git add .  # Add all files
  ```
- [ ] Commit your changes
  ```bash
  git commit -m "Your commit message"
  ```
- [ ] Push changes to GitHub
  ```bash
  git push origin main
  ```
- [ ] Pull latest changes from remote
  ```bash
  git pull origin main
  ```

### 3. Understanding Branches
- [ ] Learn what branches are and why they're important
- [ ] Create a new branch
  ```bash
  git branch <branch-name>
  ```
- [ ] Switch to a different branch
  ```bash
  git checkout <branch-name>
  # or
  git switch <branch-name>
  ```
- [ ] Create and switch to a new branch in one command
  ```bash
  git checkout -b <branch-name>
  ```
- [ ] List all branches
  ```bash
  git branch -a
  ```
- [ ] Merge branches
  ```bash
  git merge <branch-name>
  ```
- [ ] Delete a branch
  ```bash
  git branch -d <branch-name>
  ```

## Collaboration on GitHub

### 4. Working with Remotes
- [ ] Add a remote repository
  ```bash
  git remote add origin <repository-url>
  ```
- [ ] View remote repositories
  ```bash
  git remote -v
  ```
- [ ] Fetch changes from remote
  ```bash
  git fetch origin
  ```
- [ ] Push a new branch to remote
  ```bash
  git push -u origin <branch-name>
  ```

### 5. Pull Requests (PRs)
- [ ] Fork a repository
- [ ] Create a feature branch
- [ ] Make changes and commit them
- [ ] Push your branch to GitHub
- [ ] Open a Pull Request on GitHub
- [ ] Write a clear PR description
- [ ] Request reviewers for your PR
- [ ] Address review comments
- [ ] Merge your Pull Request

### 6. Issues & Project Management
- [ ] Create an issue on GitHub
- [ ] Use labels to categorize issues
- [ ] Assign issues to team members
- [ ] Reference issues in commits (e.g., "Fixes #123")
- [ ] Close issues via commits or PRs
- [ ] Use issue templates
- [ ] Create a GitHub Project board

## Advanced GitHub Features

### 7. GitHub Actions (CI/CD)
- [ ] Understand what GitHub Actions are
- [ ] Create a simple workflow file
- [ ] Run automated tests on push/PR
- [ ] Set up automated deployment
- [ ] View workflow run results

### 8. GitHub Pages
- [ ] Enable GitHub Pages for a repository
- [ ] Create a simple website using GitHub Pages
- [ ] Use Jekyll or another static site generator
- [ ] Configure a custom domain (optional)

### 9. Code Review & Quality
- [ ] Review someone else's Pull Request
- [ ] Leave constructive comments on code
- [ ] Suggest changes in a review
- [ ] Approve or request changes on a PR
- [ ] Use code owners feature
- [ ] Set up branch protection rules

### 10. Documentation
- [ ] Write a comprehensive README.md
- [ ] Add a LICENSE file
- [ ] Create a CONTRIBUTING.md guide
- [ ] Add a CODE_OF_CONDUCT.md
- [ ] Use GitHub Wiki for documentation
- [ ] Add badges to your README

## Best Practices

### 11. Commit Hygiene
- [ ] Write clear, descriptive commit messages
- [ ] Use conventional commit format (optional but recommended)
- [ ] Make small, focused commits
- [ ] Avoid committing sensitive data
- [ ] Use .gitignore to exclude unnecessary files

### 12. Collaboration Etiquette
- [ ] Always pull before you push
- [ ] Keep your branches up to date with main
- [ ] Resolve merge conflicts properly
- [ ] Communicate with your team
- [ ] Review PRs in a timely manner
- [ ] Be respectful in code reviews

### 13. Repository Management
- [ ] Create meaningful repository descriptions
- [ ] Add topics/tags to your repositories
- [ ] Keep repositories organized
- [ ] Archive old/unused repositories
- [ ] Use GitHub Releases for version management
- [ ] Set up repository insights and analytics

## Practical Exercises

### 14. Hands-On Practice
- [ ] Contribute to an open-source project
- [ ] Create a personal portfolio website using GitHub Pages
- [ ] Build a project with a team using GitHub
- [ ] Practice resolving merge conflicts
- [ ] Set up a CI/CD pipeline for a project
- [ ] Star and watch repositories you're interested in
- [ ] Follow developers whose work you admire

## Security & Privacy

### 15. GitHub Security
- [ ] Enable two-factor authentication (2FA)
- [ ] Use GitHub's security advisories
- [ ] Scan for vulnerable dependencies (Dependabot)
- [ ] Use GitHub Secrets for sensitive data
- [ ] Review repository security settings
- [ ] Understand public vs private repositories

## Additional Resources

### 16. Learning Resources
- [ ] Complete GitHub Learning Lab tutorials
- [ ] Read GitHub documentation
- [ ] Watch GitHub's YouTube tutorials
- [ ] Join GitHub Community Forums
- [ ] Explore GitHub Student Developer Pack (if eligible)
- [ ] Practice with GitHub CLI (gh command)

## Checklist for Your First Contribution

When you're ready to make your first open-source contribution, use this checklist:

- [ ] Find a beginner-friendly project (look for "good first issue" label)
- [ ] Read the project's README and CONTRIBUTING guidelines
- [ ] Fork the repository
- [ ] Create a new branch for your changes
- [ ] Make your changes and test them
- [ ] Commit with a clear message
- [ ] Push to your fork
- [ ] Open a Pull Request
- [ ] Wait for feedback and be ready to make changes
- [ ] Celebrate your contribution! 🎉

---

## Tips for Success

1. **Practice Regularly**: Use Git and GitHub for all your projects
2. **Read Error Messages**: They usually tell you exactly what's wrong
3. **Don't Be Afraid to Experiment**: You can always undo changes in Git
4. **Ask for Help**: The GitHub community is friendly and helpful
5. **Keep Learning**: GitHub is constantly evolving with new features

## Useful Git Commands Reference

```bash
# Check status
git status

# View commit history
git log
git log --oneline --graph

# View differences
git diff
git diff <branch-name>

# Undo changes
git checkout -- <filename>  # Discard changes in working directory
git reset HEAD <filename>   # Unstage file
git revert <commit-hash>    # Revert a commit

# Stash changes
git stash
git stash pop
git stash list

# View branches
git branch -a

# Update from remote
git fetch --all
git pull --rebase
```

---

**Remember**: Everyone starts as a beginner. The key is to practice consistently and don't be afraid to make mistakes. GitHub is a powerful tool that will serve you throughout your development career!

Happy Learning! 🚀
