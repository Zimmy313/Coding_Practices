# System V Shared Memory (C)

## What It Is

System V shared memory lets multiple processes map the same memory segment for fast IPC.

## `shmget()`

Prototype:

```c
int shmget(key_t key, size_t size, int shmflg);
```

What it does:
- Creates a new shared-memory segment, or gets an existing one.

Arguments:
- `key`: identifier for the segment.
  - Use `IPC_PRIVATE` to force creation of a new private segment.
  - Or use a generated key (for example from `ftok`) so unrelated processes can find the same segment.
- `size`: bytes to allocate (used on creation).
- `shmflg`: permission bits and creation flags.
  - Typical permissions: `0600`, `0666`.
  - Common flags: `IPC_CREAT` (create if missing), `IPC_EXCL` (fail if already exists when used with `IPC_CREAT`).

Returns:
- `shmid` (shared memory ID) on success.
- `-1` on failure (`errno` set).

## `shmat()`

Prototype:

```c
void *shmat(int shmid, const void *shmaddr, int shmflg);
```

What it does:
- Attaches a shared-memory segment into this process address space.

Arguments:
- `shmid`: ID from `shmget`.
- `shmaddr`: preferred attach address, usually `NULL` (kernel chooses).
- `shmflg`:
  - `0` for read/write attach (default).
  - `SHM_RDONLY` for read-only attach.

Returns:
- Attached address on success.
- `(void *) -1` on failure.

## `shmdt()`

Prototype:

```c
int shmdt(const void *shmaddr);
```

What it does:
- Detaches shared memory from this process.

Arguments:
- `shmaddr`: address previously returned by `shmat`.

Returns:
- `0` on success, `-1` on failure.

## `shmctl()`

Prototype:

```c
int shmctl(int shmid, int cmd, struct shmid_ds *buf);
```

What it does:
- Control operation on a segment (query, modify, or remove).

Common `cmd`:
- `IPC_STAT`: read metadata into `buf`.
- `IPC_SET`: update metadata from `buf`.
- `IPC_RMID`: mark segment for removal (actual delete after last detach).

## End-to-End Usage Flow

1. Create/get segment:

```c
int shmid = shmget(IPC_PRIVATE, 4096, IPC_CREAT | 0600);
```

2. Attach:

```c
char *p = (char *)shmat(shmid, NULL, 0);
if (p == (void *)-1) { /* handle error */ }
```

3. Read/write shared data:

```c
snprintf(p, 4096, "hello from shared memory");
```

4. Detach in each process:

```c
shmdt(p);
```

5. Remove segment when done (usually owner/parent):

```c
shmctl(shmid, IPC_RMID, NULL);
```

## Keyword Notes

- `IPC_PRIVATE`
  - Special key value for creating a new segment that is not looked up by a public key.
  - Common with `fork()`-related parent/child usage where `shmid` is inherited.

- `IPC_CREAT`
  - Create segment if it does not already exist.

- `IPC_EXCL`
  - With `IPC_CREAT`, fail if segment already exists (useful to enforce "create-only").

- `IPC_RMID`
  - Marks segment for deletion; safe cleanup step after all processes finish.

## Semaphores With Shared Memory (`sem_t`)

For inter-process synchronization, put `sem_t` inside shared memory and initialize it with `pshared = 1`.

Headers:

```c
#include <semaphore.h>
#include <sys/shm.h>
```

### `sem_init()`

Prototype:

```c
int sem_init(sem_t *sem, int pshared, unsigned int value);
```

What it does:
- Initializes an unnamed semaphore.

Arguments:
- `sem`: pointer to semaphore object.
- `pshared`:
  - `0`: shared between threads in one process.
  - non-zero: shared between processes (must live in shared memory).
- `value`: initial semaphore count.

Returns:
- `0` on success, `-1` on failure.

### `sem_wait()`

Prototype:

```c
int sem_wait(sem_t *sem);
```

What it does:
- Decrements semaphore count.
- Blocks when count is `0` until another process posts.

### `sem_post()`

Prototype:

```c
int sem_post(sem_t *sem);
```

What it does:
- Increments semaphore count.
- Wakes one waiting process if any.

### `sem_destroy()`

Prototype:

```c
int sem_destroy(sem_t *sem);
```

What it does:
- Releases resources of an unnamed semaphore.
- Call only after all users are done.

## Shared Memory + Semaphore Flow

1. Define a shared struct:

```c
typedef struct {
    sem_t lock;
    int counter;
} shared_t;
```

2. Create shared memory large enough for `shared_t`:

```c
int shmid = shmget(IPC_PRIVATE, sizeof(shared_t), IPC_CREAT | 0600);
```

3. Attach and initialize once (usually parent):

```c
shared_t *s = (shared_t *)shmat(shmid, NULL, 0);
sem_init(&s->lock, 1, 1); /* pshared=1, binary semaphore */
s->counter = 0;
```

4. In each process, protect critical section:

```c
sem_wait(&s->lock);
s->counter += 1;   /* critical section */
sem_post(&s->lock);
```

5. Cleanup sequence:
- Each process: `shmdt(s)`.
- Owner after all children exit: `sem_destroy(&s->lock)`, then `shmctl(shmid, IPC_RMID, NULL)`.

## Notes

- `sem_t` for process-shared semaphores must be in shared memory.
- Compile with pthread support (for example: `gcc file.c -pthread`).
