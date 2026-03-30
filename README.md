# Cheatsheets

This repository stores my learning notes and code-heavy cheat sheets in Markdown.

## Structure

```text
.
├── README.md
├── AGENTS.md
├── archive/
└── C/
    ├── headers.md
    ├── pointers.md
    ├── shared-memory.md
    └── typedef-struct.md
```

## Organization Rules

- Each programming language gets its own top-level folder (for example: `C/`, `Python/`, `Cpp/`).
- Notes are written in Markdown (`.md`) by default.
- Inside each language folder, files are grouped by topic.
- Keep examples practical: include what an API does, key arguments, and end-to-end usage flow.

## Current Focus

- `C/headers.md`: quick reference for important C/POSIX headers.
- `C/shared-memory.md`: System V shared memory (`shmget`, `shmat`, `shmdt`, `shmctl`) and usage flow.
- `C/typedef-struct.md`: practical syntax patterns and common pitfalls for `typedef struct`.
- `C/pointers.md`: comprehensive pointer reference (`*`, `**`, arrays, function pointers, memory/lifetime pitfalls).
