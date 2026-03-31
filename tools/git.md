## Git Quick Reference (Fork Workflow + Daily Usage)

### 1. Core Concepts

- **Repository (repo)**  
  A project tracked by Git.

- **Commit**  
  A snapshot of your code.

- **Branch**  
  A line of development (e.g. `main`, `feature/x`).

- **Remote**  
  A named reference to a repo URL (e.g. `origin`, `upstream`).

- **Origin**  
  Default name for your fork or the repo you cloned from.

- **Upstream**  
  Conventionally the original repo you forked from.

- **Tracking / Upstream branch**  
  A link between your local branch and a remote branch.

---

### 2. Key Mental Model

- Commits live **locally**
- Remotes are just **places you send commits to**
- Same commits can be pushed to **multiple remotes**

---

### 3. Basic Commands

#### Check remotes
```bash
git remote -v
```

#### Check current branch
```bash
git branch
```

#### Check tracking
```bash
git branch -vv
```

---

### 4. Pushing

#### Basic push
```bash
git push origin main
```
Push local `main` → remote `origin`

#### Push new branch + set upstream
```bash
git push -u origin feature/mingyuan
```

After this:
```bash
git push
git pull
```
will work without extra arguments

---

### 5. `-u` Flag

```bash
git push -u origin branch
```

Means:
- push branch
- remember where it goes

Applies **per branch**, not globally

---

### 6. Push to Different Remote Branch Name

```bash
git push origin local_branch:remote_branch
```

Example:
```bash
git push origin feature/mingyuan:my-branch
```

Shortcut:
```bash
git push origin HEAD:my-branch
```

---

### 7. Fork Workflow (Recommended)

#### Setup

```bash
# rename original repo
git remote rename origin upstream

# add your fork
git remote add origin git@github.com:YOURNAME/repo.git
```

Now:
- `origin` = your fork (push here)
- `upstream` = original repo (pull from here)

#### Push your work
```bash
git push -u origin feature/mingyuan
```

#### Sync with original repo
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

### 8. Changing Remotes

#### Change URL of existing remote
```bash
git remote set-url origin <new-url>
```

#### Add new remote
```bash
git remote add name <url>
```

#### Rename remote
```bash
git remote rename old new
```

---

### 9. Common Errors

#### No upstream branch
```bash
fatal: no upstream branch
```

Fix:
```bash
git push -u origin branch
```

---

#### No permission to push
```bash
permission denied
```

Cause:
- no write access to repo

Solution:
- push to your fork instead

---

#### Remote does not exist
```bash
No such remote
```

Cause:
- trying to modify non-existent remote

Fix:
```bash
git remote add <name> <url>
```

---

### 10. Safe Workflow for Your Case

1. Fork repo on GitHub  
2. Set your fork as `origin`  
3. Keep original as `upstream`  
4. Work on feature branch  
5. Push to your fork  
6. Open PR to upstream  

---

### 11. Summary

- `origin` = where you push (usually your fork)
- `upstream` = original repo
- `-u` = remember push target
- branches are independent
- remotes are just names → URLs
- pushing to one repo does NOT block pushing elsewhere

---

### 12. Minimal Daily Commands

```bash
git checkout -b feature/x
git add .
git commit -m "message"
git push -u origin feature/x
```

After that:

```bash
git push
git pull
```

## Additional Git Command Blocks

### Logs and History

```bash
git log --oneline
git log --graph --decorate --all
```

- `--oneline`: compact commit history.
- `--graph --decorate --all`: visual branch/merge graph with refs.

### Staging and Committing

```bash
git add file.py
git add .
git commit -m "message"
git commit -a -m "message"
git commit --amend
```

- `git add file.py`: stage one file.
- `git add .`: stage all changes under current directory.
- `git commit -a -m "message"`: auto-stage tracked files only.
- `git commit --amend`: rewrite the latest commit (message and/or content).

### Branching and Switching

```bash
git branch
git branch -a
git branch branch_name
git switch branch_name
git checkout branch_name
git branch -d branch_name
git branch -D branch_name
```

- `git branch -a`: include remote-tracking branches.
- `git branch branch_name`: create new branch.
- `git switch` / `git checkout`: move to branch.
- `git branch -d`: delete branch (safe).
- `git branch -D`: force-delete branch.

### Remote, Fetch, Pull, Push

```bash
git remote -v
git fetch
git fetch origin
git pull --rebase
git push origin main
```

- `git remote -v`: show remote URLs.
- `git fetch`: download remote updates without merging.
- `git fetch origin`: update remote-tracking branches from `origin`.
- `git push origin main`: push local `main` to `origin/main`.

### Restore and Unstage

```bash
git restore file.py
git restore --staged file.py
```

- `git restore file.py`: discard local working-tree changes in file.
- `git restore --staged file.py`: unstage file.

### Stash Workflow (Temporary Local Work)

```bash
git stash push -m "WIP: ASSAIA notebook"
git pull
git stash pop
```

- Use when you have temporary changes you do not want to commit yet.

### Merging

```bash
git merge --no-ff branch_name
```

- `--no-ff`: always create a merge commit (keeps branch history explicit).
