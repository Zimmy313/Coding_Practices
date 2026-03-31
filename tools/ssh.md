# SSH Quick Reference

## 1. Key Generation

```bash
ssh-keygen -t ed25519 -C "your_email@example.com" -f ~/Desktop/my_ssh_key
```

- `-t`: key type (for example `ed25519`, `rsa`).
- `-C`: comment to identify key.
- `-f`: output path + key filename.

Generated files:
- `my_ssh_key`: private key (keep secret).
- `my_ssh_key.pub`: public key (share this one).

## 2. SSH Connection

```bash
ssh -i ~/.ssh/testkey -p 2222 -v username@hostname
```

- `-i`: path to private key file.
- `-p`: port number.
- `-v` / `-vv` / `-vvv`: verbose debugging levels.

Check SSH version:

```bash
ssh -V
```

## 3. GitHub Authentication Check

```bash
ssh -T git@github.com
ssh -vT git@github.com
```

- `-T`: disable pseudo-terminal allocation (authenticate only, no shell).
- `-vT`: verbose output + no pseudo-terminal.

## 4. SSH Agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

- Start `ssh-agent` in current shell.
- Add private key into the agent for authentication.
