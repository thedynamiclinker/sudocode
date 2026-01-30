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
