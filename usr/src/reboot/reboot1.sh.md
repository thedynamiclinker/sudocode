```sh
#!/bin/sh

### reboot ABI magic (see man 2 reboot)
SYS_REBOOT=169
LINUX_REBOOT_MAGIC1=0xfee1dead
LINUX_REBOOT_MAGIC2=0x28121969
LINUX_REBOOT_MAGIC2A=0x05121996
LINUX_REBOOT_MAGIC2B=0x16041998
LINUX_REBOOT_MAGIC2C=0x20112000
LINUX_REBOOT_CMD_RESTART=0x4321fedc

# reboot
cat > reboot.asm << EOF
global _start
_start:
mov eax, ${SYS_REBOOT}
mov edi, ${LINUX_REBOOT_MAGIC1}
mov esi, ${LINUX_REBOOT_MAGIC2}
mov edx, ${LINUX_REBOOT_CMD_RESTART}
syscall
EOF

nasm -f elf64 -o reboot.o reboot.asm
ld -o reboot reboot.o
```
