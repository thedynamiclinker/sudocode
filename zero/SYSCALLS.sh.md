```bash
#!/usr/bin/env bash

### syscall numbers (x86_64 Linux)
SYS_EXIT=60
SYS_SYNC=162
SYS_GETPID=39
SYS_GETPPID=110
SYS_GETUID=102
SYS_GETGID=104
SYS_KILL=62
SYS_PAUSE=34
SYS_NANOSLEEP=35
SYS_UNAME=63
SYS_GETTIMEOFDAY=96
SYS_CHDIR=80
SYS_GETCWD=79
SYS_UMASK=95
SYS_TIMES=100
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
mov eax,${SYS_EXIT}
xor edi,edi
syscall
EOF

###############################################################################

# false(1): exit(1)
cat >false.asm <<EOF
bits 64
mov eax,${SYS_EXIT}
mov edi,1
syscall
EOF

###############################################################################

# sync(1): sync(); exit(0)
cat >sync.asm <<EOF
bits 64
mov eax,${SYS_SYNC}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# getpid(1): exit(getpid())
cat >getpid.asm <<EOF
bits 64
mov eax,${SYS_GETPID}
syscall
mov edi,eax      ; exit status = pid (truncated by shell)
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# getppid(1): exit(getppid())
cat >getppid.asm <<EOF
bits 64
mov eax,${SYS_GETPPID}
syscall
mov edi,eax
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# id -u (numeric uid via exit code)
cat >id-u.asm <<EOF
bits 64
mov eax,${SYS_GETUID}
syscall
mov edi,eax
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# id -g (numeric gid via exit code)
cat >id-g.asm <<EOF
bits 64
mov eax,${SYS_GETGID}
syscall
mov edi,eax
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# kill $$ SIGTERM
cat >kill-self.asm <<EOF
bits 64
mov eax,${SYS_GETPID}
syscall
mov edi,eax
mov esi,${SIGTERM}
mov eax,${SYS_KILL}
syscall
EOF

###############################################################################

# pause(1): sleep until signal
# returns only after signal handler or termination
cat >pause.asm <<EOF
bits 64
mov eax,${SYS_PAUSE}
syscall
EOF

###############################################################################

# sleep 1
# ABI: nanosleep takes two pointers: req, rem
cat >sleep1.asm <<EOF
bits 64
sub rsp,16
mov qword [rsp],1     ; tv_sec
mov qword [rsp+8],0   ; tv_nsec
mov rdi,rsp
xor rsi,rsi           ; rem = NULL
mov eax,${SYS_NANOSLEEP}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# uname (stores struct utsname; output discarded)
cat >uname.asm <<EOF
bits 64
sub rsp,390           ; sizeof(struct utsname)
mov rdi,rsp
mov eax,${SYS_UNAME}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# gettimeofday (obsolete but historically core)
cat >gettimeofday.asm <<EOF
bits 64
sub rsp,32
mov rdi,rsp           ; struct timeval*
xor rsi,rsi           ; timezone* = NULL
mov eax,${SYS_GETTIMEOFDAY}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# chdir /
cat >cd-root.asm <<EOF
bits 64
lea rdi,[rel path]
mov eax,${SYS_CHDIR}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
path db "/",0
EOF

###############################################################################

# pwd (probe only; no output)
# ABI: getcwd writes into user buffer
cat >pwd.asm <<EOF
bits 64
sub rsp,4096
mov rdi,rsp
mov esi,4096
mov eax,${SYS_GETCWD}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# umask 0
cat >umask.asm <<EOF
bits 64
xor edi,edi
mov eax,${SYS_UMASK}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# times (writes struct tms)
cat >times.asm <<EOF
bits 64
sub rsp,64
mov rdi,rsp
mov eax,${SYS_TIMES}
syscall
xor edi,edi
mov eax,${SYS_EXIT}
syscall
EOF

###############################################################################

# reboot (dangerous; requires CAP_SYS_BOOT)
# ABI magic required by kernel to prevent accidental reboot
cat >reboot.asm <<EOF
bits 64
mov edi,${LINUX_REBOOT_MAGIC1}
mov esi,${LINUX_REBOOT_MAGIC2}
mov edx,${LINUX_REBOOT_CMD_RESTART}
mov eax,${SYS_REBOOT}
syscall
EOF
```
