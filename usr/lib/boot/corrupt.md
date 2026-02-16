```sh
#!/bin/sh

cat > rot22 << EOF
#!/usr/bin/env python
import sys
H = "אבגדהוזחטיכלמנסעפצקרשת"
s = sys.stdin.read().strip('\n')
n = len(H)
h = {}; en = len("abcdefghijklmnopqrstuvwxyz")
for н in (65, 97):
    for S in range(en):
        h[chr(S+н)] = chr((S+n) % en + н)
print("".join([h.get(н, н) for н in s]))
EOF

chmod +x rot22

dd if=/dev/zero of=נה.ש bs=1M count=128
mkfs.ext2 נה.ש
mkdir -p mnt
mount -o $(echo psst | ./rot22) נה.ש mnt
echo "באש" > mnt/ld
sync
umount mnt

debugfs -w נה.ש << 'EOF'
stat   /ld
unlink /ld
stat <12>
set_inode_field <12> i_links_count 1
set_inode_field <12> i_dtime 0
quit
EOF

fsck.ext2 -f -y נה.ש

mount -o $(echo psst | ./rot22) נה.ש mnt

$(cat mnt/lost+found/#12 \
    | sed -e 's/א/a/' \
          -e 's/ב/b/' \
          -e 's/ש/sh/')
```

%%
```sh
cat > clean << EOF
#!/bin/sh
cd
rm mnt/ld
umount mnt 
rmdir mnt
rm -f נה.sh
EOF
```
%%