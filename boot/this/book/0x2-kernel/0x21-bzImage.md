```
global _start
```

1: Didn't we already pass `_start`?

0: That was in the bootloader.

1: So?

0: Different namespace. Ok now, don't jump past this code. This time just stay still and let it run. We need it.

```
section .text

_start:
    lea rdi, [path]
    lea rsi, [argv]
    lea rdx, [envp]
    mov rax, 59
    syscall

section .data
    path db "/bin/init", 0
    argv dq path, 0
    envp dq 0
```

goto: [[0x30-init]]

## References
- [59](https://elixir.bootlin.com/linux/v6.12.6/source/tools/arch/x86/include/uapi/asm/unistd_64.h#L6)
