# Command Line Tools (CLT)

## 1. Show Hidden Files

- macOS shortcut: `Cmd + Shift + .`
- Use case: toggle hidden files (for example `.ssh`).

## 2. `cat`

```bash
cat file.txt
cat ~/.ssh/id_ed25519
```

- Purpose: print file content to terminal.

## 3. `echo`

```bash
echo "hello"
echo $?
```

- Purpose: display text/string.
- `echo $?`: print exit status of the previous command (`0` usually means success).

## 4. `grep`

```bash
grep [flags] [pattern] [file]
grep "python" code.py
grep -ri "abc" --include="*.py" .
grep -r "abc" --include="*.{py,txt,md}" .
```

- Purpose: search inside file contents.
- `-r`: recursive search.
- `-i`: case-insensitive.
- `--include="PATTERN"`: limit which files are searched.

## 4.1 `find`

```bash
find [dir] -iname "*xx*"
find . -iname "*config*"
```

- Purpose: search by file/directory name.
- `-iname`: case-insensitive name match.

## 5. `touch`

```bash
touch file.txt
touch -c file.txt
```

- Purpose: update file timestamp; create file if missing.
- `-c`: do not create file if it does not exist.

## 6. `mkdir`

```bash
mkdir data
mkdir -p a/b/c
```

- Purpose: create directory.
- `-p`: create parent directories as needed; no error if already exists.

## 6.1 `rmdir`

```bash
rmdir dir
rm -r dir
```

- `rmdir`: remove empty directory only.
- `rm -r`: remove directory recursively.

## 7. `rm`

```bash
rm file.txt
```

- Purpose: remove a file.

## 8. `wget`

```bash
wget -P downloads -O data.csv [URL]
```

- Purpose: download file from web.
- `-O`: output filename.
- `-P`: save into directory.

Common page-mirroring flags:

```bash
wget -E -H -k -K -p https://example.com/page
wget -r -l 1 -np -E -k -K -p https://example.com/page
```

- `-E`: add proper filename extensions.
- `-H`: allow spanning to other hosts.
- `-k`: rewrite links for local browsing.
- `-K`: keep original file backup (`.orig`).
- `-p`: download page assets (CSS/images/etc).
- `-r`: recursive.
- `-l 1`: recursion depth 1.
- `-np`: no parent.

## 9. `unzip`

```bash
unzip file.zip -d output_dir
unzip -l file.zip
```

- Purpose: extract zip files.
- `-l`: list archive contents without extracting.
- `-d`: extract into target directory.

## 10. `mv`

```bash
mv oldname newname
mv file.txt dir/
mv -i oldname newname
```

- Purpose: move or rename files.
- `-i`: prompt before overwrite.

## 11. `source`

```bash
source ~/.zshrc
```

- Purpose: run file in current shell session (does not start a new shell).

## 12. `chmod`

Purpose: change file/directory permissions.

Permission roles:
- `u`: user (owner)
- `g`: group
- `o`: others
- `a`: all (`u+g+o`)

Permission bits:
- `r`: read
- `w`: write
- `x`: execute

Meaning on files:
- `r`: read file contents
- `w`: modify file contents
- `x`: run file as program

Meaning on directories:
- `r`: list directory entries
- `w`: create/delete entries
- `x`: enter directory (`cd`)

Symbolic mode:

```bash
chmod +x file
chmod u+x file
chmod g-w file
chmod o=r file
```

Numeric mode:
- `r=4`, `w=2`, `x=1`

```bash
chmod 644 file   # rw-r--r--
chmod 755 file   # rwxr-xr-x
chmod 700 file   # rwx------
```

Common flag:
- `-R`: apply recursively.

```bash
chmod -R 755 mydir
```

## 13. `du`

```bash
du -sh foldername
```

- Purpose: check directory size.
- `-s`: summary only.
- `-h`: human-readable size.


