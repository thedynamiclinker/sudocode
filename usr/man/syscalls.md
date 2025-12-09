
syscall (noun)
1. A prayer to the kernel to do magic on your behalf.
2. Everything in computing that's more like `mkdir` than `f(x) = x²`.
3. Everything in computing that we didn't hear about in `lost+found`, because syscalls don't exist until machines do.
4. Everything in computing you still need after you've got Turing completeness.
5. The most important lines in any codebase, after the bugs.

---


```sh
#!/bin/sh

### syscall numbers (x86_64 Linux)
SYS_PAUSE=34
SYS_NANOSLEEP=35
SYS_GETPID=39
SYS_EXIT=60
SYS_KILL=62
SYS_UNAME=63
SYS_GETCWD=79
SYS_CHDIR=80
SYS_UMASK=95
SYS_GETTIMEOFDAY=96
SYS_TIMES=100
SYS_GETUID=102
SYS_GETGID=104
SYS_GETPPID=110
SYS_SYNC=162
SYS_REBOOT=169

### signals
SIGTERM=15

### reboot ABI magic (documented in man 2 reboot)
LINUX_REBOOT_MAGIC1=0xfee1dead
LINUX_REBOOT_MAGIC2=672274793
LINUX_REBOOT_MAGIC2A=85072278
LINUX_REBOOT_MAGIC2B=369367448
LINUX_REBOOT_CMD_RESTART=0x4321fedc

###############################################################################

# true(1): exit(0)
cat >true.asm <<EOF
bits 64
mov eax, ${SYS_EXIT}
xor edi, edi
syscall
EOF

###############################################################################

# false(1): exit(1)
cat >false.asm <<EOF
bits 64
mov eax, ${SYS_EXIT}
mov edi, 1
syscall
EOF

###############################################################################

# sync(1): sync(); exit(0)
cat >sync.asm <<EOF
bits 64
mov eax, ${SYS_SYNC}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# getpid(1): exit(getpid())
cat >getpid.asm <<EOF
bits 64
mov eax, ${SYS_GETPID}
syscall
mov edi, eax      ; exit status = pid (truncated by shell, use a write syscall here)
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# getppid(1): exit(getppid())
cat >getppid.asm <<EOF
bits 64
mov eax, ${SYS_GETPPID}
syscall
mov edi, eax
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# id -u (numeric uid via exit code)
cat >id-u.asm <<EOF
bits 64
mov eax, ${SYS_GETUID}
syscall
mov edi, eax
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# id -g (numeric gid via exit code)
cat >id-g.asm <<EOF
bits 64
mov eax, ${SYS_GETGID}
syscall
mov edi, eax
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# kill $$ SIGTERM
cat >kill-self.asm <<EOF
bits 64
mov eax, ${SYS_GETPID}
syscall
mov edi, eax
mov esi, ${SIGTERM}
mov eax, ${SYS_KILL}
syscall
EOF

###############################################################################

# pause(1): sleep until signal
# returns only after signal handler or termination
cat >pause.asm <<EOF
bits 64
mov eax, ${SYS_PAUSE}
syscall
EOF

###############################################################################

# sleep 1
# ABI: nanosleep takes two pointers: req, rem
cat >sleep1.asm <<EOF
bits 64
sub rsp, 16
mov qword [rsp], 1     ; tv_sec
mov qword [rsp+8], 0   ; tv_nsec
mov rdi, rsp
xor rsi, rsi           ; rem = NULL
mov eax, ${SYS_NANOSLEEP}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# uname (stores struct utsname; output discarded)
cat >uname.asm <<EOF
bits 64
sub rsp, 390           ; sizeof(struct utsname)
mov rdi, rsp
mov eax, ${SYS_UNAME}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# gettimeofday (obsolete but historically core)
cat >gettimeofday.asm <<EOF
bits 64
sub rsp, 32
mov rdi, rsp           ; struct timeval*
xor rsi, rsi           ; timezone* = NULL
mov eax, ${SYS_GETTIMEOFDAY}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# chdir /
cat >cd-root.asm <<EOF
bits 64
lea rdi, [rel path]
mov eax, ${SYS_CHDIR}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
path db "/", 0
EOF

###############################################################################

# pwd (probe only; no output)
# ABI: getcwd writes into user buffer
cat >pwd.asm <<EOF
bits 64
sub rsp, 4096
mov rdi, rsp
mov esi, 4096
mov eax, ${SYS_GETCWD}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# umask 0
cat >umask.asm <<EOF
bits 64
xor edi, edi
mov eax, ${SYS_UMASK}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

# times (writes struct tms)
cat >times.asm <<EOF
bits 64
sub rsp, 64
mov rdi, rsp
mov eax, ${SYS_TIMES}
syscall
xor edi, edi
mov eax, ${SYS_EXIT}
syscall
EOF

###############################################################################

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