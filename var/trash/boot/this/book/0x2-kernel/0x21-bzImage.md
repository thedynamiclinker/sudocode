```
global _start

section .data
    path db "/bin/init", 0
    argv dq path, 0
    envp dq 0

section .text

_start:
    lea rdi, [path]
    lea rsi, [argv]
    lea rdx, [envp]
    mov rax, 59
    syscall
```

goto: [[0x30-init]]

## References
- [59](https://elixir.bootlin.com/linux/v6.12.6/source/tools/arch/x86/include/uapi/asm/unistd_64.h#L6)
