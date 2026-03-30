# C Header Quick Notes

`#include <stdio.h>`
- Purpose: standard input/output APIs.
- Common contents:
  - `printf`, `fprintf`, `sprintf`, `snprintf`
  - `scanf`, `fscanf`, `sscanf`
  - `FILE`, `fopen`, `fclose`, `fread`, `fwrite`, `fgets`, `fputs`
  - `stdin`, `stdout`, `stderr`

`#include <unistd.h>`
- Purpose: POSIX system-call interface.
- Common contents:
  - `fork`, `exec*`, `getpid`, `getppid`
  - `read`, `write`, `close`, `pipe`
  - `sleep`, `usleep`

`#include <stdlib.h>`
- Purpose: general utilities and memory management.
- Common contents:
  - `malloc`, `calloc`, `realloc`, `free`
  - `exit`, `abort`, `atexit`
  - `atoi`, `strtol`, `strtod`
  - `rand`, `srand`

`#include <semaphore.h>`
- Purpose: POSIX semaphore APIs for synchronization.
- Common contents:
  - `sem_t`
  - `sem_init`, `sem_wait`, `sem_post`, `sem_destroy`
  - `sem_open`, `sem_close`, `sem_unlink` (named semaphores)

`#include <sys/shm.h>`
- Purpose: System V shared memory APIs.
- Common contents:
  - `shmget`, `shmat`, `shmdt`, `shmctl`
  - `struct shmid_ds`
  - Flags such as `IPC_CREAT`, `IPC_EXCL`, `IPC_PRIVATE`

`#include <sys/wait.h>`
- Purpose: process wait/status inspection for child processes.
- Common contents:
  - `wait`, `waitpid`
  - Status macros: `WIFEXITED`, `WEXITSTATUS`, `WIFSIGNALED`, `WTERMSIG`
