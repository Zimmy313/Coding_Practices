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

---

This is enough for ~95% of real-world workflows.