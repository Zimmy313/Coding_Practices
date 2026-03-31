# GCC / G++ Cheat Sheet

## Compilers

- `gcc`: C compiler driver.
- `g++`: C++ compiler driver.

## Basic Compile

```bash
gcc main.c -o main
g++ main.cpp -o main
```

- `-o <name>`: set output executable name.
- If `-o` is omitted, default output is `a.out`.

## Language Standard

```bash
-std=c11
-std=c++20
```

- `-std=c11`: use C11 standard.
- `-std=c++20`: use C++20 standard.

## Warnings

```bash
-Wall -Wextra -Wpedantic
```

- `-Wall`: common useful warnings.
- `-Wextra`: additional warnings beyond `-Wall`.
- `-Wpedantic`: warnings for non-standard extensions.

## Debugging

```bash
-g
```

- Include debug symbols for debuggers (for example `lldb`).

## Compilation Stages

```bash
gcc -c main.c        # compile only -> main.o
gcc main.o -o main   # link object -> executable
```

- `-c`: compile only; do not link.

## Run and Debug

```bash
./main
lldb ./main
```

## Recommended Defaults

### C

```bash
gcc -std=c11 -Wall -Wextra -Wpedantic -g main.c -o main
```

### C++

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic -g main.cpp -o main
```

## Lima on macOS

- Use `Lima` when you want a lightweight Linux VM on macOS.
- Typical flow:

```bash
limactl start default
limactl shell default
```

- Inside VM, install build tools:

```bash
sudo apt update
sudo apt install -y build-essential
gcc --version
```

- Exit and stop VM:

```bash
exit
limactl stop default
```
