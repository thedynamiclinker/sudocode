
syscall (noun)
1. A prayer to the kernel to do magic on your behalf.
2. Everything in computing that's more like `mkdir` than `f(x) = x²`.
3. Everything in computing that we didn't hear about in `lost+found`, because syscalls don't exist until machines do.
4. Everything in computing you still need after you've got Turing completeness.
5. The most important lines in any codebase, after the bugs.

---

```sh
#!/bin/sh
SYS_REBOOT=169

### reboot ABI magic (documented in man 2 reboot)
LINUX_REBOOT_MAGIC1=0xfee1dead
LINUX_REBOOT_MAGIC2=672274793
LINUX_REBOOT_MAGIC2A=85072278
LINUX_REBOOT_MAGIC2B=369367448
LINUX_REBOOT_CMD_RESTART=0x4321fedc

###########################################################
# reboot (dangerous; requires CAP_SYS_BOOT)
# ABI magic required by kernel to prevent accidental reboot
cat >reboot.asm <<EOF
bits 64
mov edi, ${LINUX_REBOOT_MAGIC1}
mov esi, ${LINUX_REBOOT_MAGIC2}
mov edx, ${LINUX_REBOOT_CMD_RESTART}
mov eax, ${SYS_REBOOT}
syscall
EOF
```

1: What was that bit about reboot magic?

0: Let's see.

```man
reboot(2)                   System Calls Manual

NAME
       reboot

LIBRARY
       Standard C library (libc, -lc)

DESCRIPTION

		...

       This  system  call  fails  (with  the  error  EINVAL)
       unless magic equals LINUX_REBOOT_MAGIC1 (that is, 0xfee1dead)
       and magic2 equals LINUX_REBOOT_MAGIC2 (that is, 0x28121969).
       
       However, since Linux 2.1.17 also LINUX_REBOOT_MAGIC2A
       (that is, 0x05121996) and since Linux 2.1.97 also
       LINUX_REBOOT_MAGIC2B (that is, 0x16041998) and
       since Linux 2.5.71 also LINUX_REBOOT_MAGIC2C
       (that is, 0x20112000) are permitted as values
       for magic2. (The hexadecimal values of these
       constants are meaningful.)
```

1: That's a real man page?

0: For the most part.

1: Why those numbers?

0: Why is Christmas on December 25th?

1: Why do you always answer my questions with a question?

0: Answer mine.

1: New Calendar. Year zero. Hypothetical birthday of Josh character. The obvious reasons.

0: Do you think it's plausible that the Josh character was born so close to year 0?

1: Not even slightly.

0: Why not?

1: Too perfect. Seems highly implausible.

0: Agreed. What time is it now?

1: In what format?

0: Since the Epoch.

1: `man 2 time`

```man
NAME
       time - get time in seconds

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <time.h>

       time_t time(time_t *tloc);

DESCRIPTION
       time() returns the time as the number of seconds
       since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).
```

1: `vim time.c`

```c
#include <time.h>
#include <stdio.h>

int main(int argc, char **argv) {
    time_t *t;
    printf("time since the epoch: %ld\n", time(t));
}
```

```sh
~ $ cc time.c
~ $ ./a.out
time since the epoch: 1765214637
```

1: It's `1765214637`.

> _Unix time is a date and time representation widely used in computing. It measures time by the number of non-leap seconds that have elapsed since 00:00:00 UTC on 1 January 1970._
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

1: Why's that relevant?