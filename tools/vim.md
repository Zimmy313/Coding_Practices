# Vim Quick Cheatsheet

## Word Motion

- `w`: next word
- `b`: previous word
- `e`: end of current word

## Files

```vim
:e file.txt
:w
:q
:wq
:q!
:qa
:wqa
:set number
```

- `:e file.txt`: open file
- `:w`: save
- `:q`: quit
- `:wq`: save + quit
- `:q!`: quit without saving
- `:qa`: quit all
- `:wqa`: save all + quit
- `:set number`: show line numbers

## Buffers (Files in Memory)

```vim
:ls
:buffer 2
:buffer name
:buffer #
:bn
:bp
:bd
:bd!
```

- `:ls`: list buffers
- `:buffer 2`: go to buffer 2
- `:buffer name`: go to buffer by name
- `:buffer #`: previous buffer
- `:bn`: next buffer
- `:bp`: previous buffer
- `:bd`: close buffer
- `:bd!`: force close buffer

## Tabs (Workspaces)

```vim
:tabnew file
:tabn
:tabp
:tabclose
:tabonly
gt
gT
2gt
:tabs
```

- `:tabnew file`: open file in new tab
- `:tabn`: next tab
- `:tabp`: previous tab
- `:tabclose`: close tab
- `:tabonly`: close all other tabs
- `gt`: next tab
- `gT`: previous tab
- `2gt`: go to tab 2
- `:tabs`: list tabs

## Splits (Windows)

```vim
:vs
:sp
:vs file
:enew
:e other_file.cpp
:terminal
:botright terminal
```

- `:vs`: vertical split
- `:sp`: horizontal split
- `:vs file`: split and open file
- `:enew`: open a new empty buffer in current split
- `:e other_file.cpp`: open another file in current split
- `:terminal`: open terminal
- `:botright terminal`: open terminal at bottom

## Window Navigation / Management

- `Ctrl+w h` / `Ctrl+w H`: move left / move split far left
- `Ctrl+w l` / `Ctrl+w L`: move right / move split far right
- `Ctrl+w j` / `Ctrl+w J`: move down / move split to bottom
- `Ctrl+w k` / `Ctrl+w K`: move up / move split to top
- `Ctrl+w c`: close split
- `Ctrl+w o`: keep only this split
- `Ctrl+w s`: horizontal split
- `Ctrl+w v`: vertical split
- `Ctrl+w w`: switch window
- `Ctrl+w q`: close window
- `Ctrl+w N`: open new window in Normal mode (useful in terminal buffers)

## Copy / Paste

```vim
gg
G
ggVG
V
v
Ctrl-v
y
p
P
"+y
"+p
```

- `gg`: go to top of file
- `G`: go to bottom of file
- `ggVG`: select entire file
- `V`: line-wise select
- `v`: character-wise select
- `Ctrl-v`: block (column) select
- `y`: yank (copy)
- `p`: paste after cursor
- `P`: paste before cursor
- `"+y`: copy to system clipboard
- `"+p`: paste from system clipboard

Copy right-hand split only:

```vim
Ctrl-w l
ggVG"+y
```

## Terminal / Workflow

```vim
Ctrl-z
fg
:shell
exit
```

- `Ctrl-z`: suspend Vim, go to terminal
- `fg`: return to Vim
- `:shell`: open shell inside Vim
- `exit`: return from shell

## Common Workflows

Split + other file:

```vim
:vs | buffer #
```

See all open files:

```vim
:ls
```

Emergency exit:

```vim
:qa!
```

## Mental Model

- Buffer = file
- Split = view
- Tab = workspace
