A hymn to the Unix method of data storage, by way of the `mount` command.

Consider what we see, when we type the command:

```
~ $ mount
```

We see the following output, and usually don't think much of it.

```
devtmpfs on /dev type devtmpfs (rw,nosuid,size=2045892k,nr_inodes=5110327,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=3,mode=620,ptmxmode=666)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
tmpfs on /run type tmpfs (rw,nosuid,nodev,size=10229460k,mode=755)
ramfs on /run/keys type ramfs (rw,nosuid,nodev,relatime,mode=750)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
/dev/nvme1n1p2 on / type ext4 (rw,relatime)
/dev/nvme1n1p2 on /nix/store type ext4 (rw,relatime)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime,nsdelegate,memory_recursiveprot)
none on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
efivarfs on /sys/firmware/efi/efivars type efivarfs (rw,nosuid,nodev,noexec,relatime)
bpf on /sys/fs/bpf type bpf (rw,nosuid,nodev,noexec,relatime,mode=700)
debugfs on /sys/kernel/debug type debugfs (rw,nosuid,nodev,noexec,relatime)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,nosuid,nodev,relatime,pagesize=2M)
tracefs on /sys/kernel/tracing type tracefs (rw,nosuid,nodev,noexec,relatime)
mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime)
tmpfs on /run/credentials/systemd-journald.service type tmpfs (ro,nosuid,nodev,noexec,relatime,nosymfollow,size=1024k,nr_inodes=1024,mode=700,noswap)
configfs on /sys/kernel/config type configfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /run/wrappers type tmpfs (rw,nodev,relatime,mode=755)
fusectl on /sys/fs/fuse/connections type fusectl (rw,nosuid,nodev,noexec,relatime)
/dev/nvme0n1p1 on /boot type vfat (rw,relatime,fmask=0077,dmask=0077,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro)
/dev/nvme0n1p2 on /home/jason/Desktop type ext4 (rw,relatime)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=4091780k,nr_inodes=1022945,mode=700,uid=1000,gid=100)
gvfsd-fuse on /run/user/1000/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,relatime,user_id=1000,group_id=100)
portal on /run/user/1000/doc type fuse.portal (rw,nosuid,nodev,relatime,user_id=1000,group_id=100)
```

But consider for a moment the brilliance of this format.

A few simple choices make the format above infinitely more pleasant than common storage formats like csv, json, or god forbid relational databases.

The choices that make this format so pleasant are precisely the choices that _sound_ to the naive ear like poor design.

Look again at the text that came down from the `mount` command.

What is this format?

Words are too blunt an instrument to do it justice.

To see how strange and beautiful this data format is, imagine proposing it to a committee of developers and managers at any company that develops software of any kind.

During the standard bikeshedding, as some propose MySQL and others suggest Postgresql, with others suggesting keeping it simple and just using pickle or json or csv;

Just as the bikeshedding has almost reached a crescendo,

A voice of One is heard, proposing the strangest thing of all.

At first the others misunderstand. They hear the suggestion and think this:

|                | On                   | Type     |                                                                     |
| -------------- | -------------------- | -------- | ------------------------------------------------------------------- |
| /dev/something | /path/to/mount/point | sometype | (A half tuple half dict is stored here, with no name in the header) |

After some back and forth, the One clarifies that they've misunderstood.

This One's absurd proposal is even stranger than they first thought.

This One is suggesting we store the data as a kind of structured English sentence;

With spaces as the field delimeters,

And simple English function words like `on` instead of technical terms like `mountpoint`.

This One suggests the format be pseudo-tabular.
The others ask what this means.

The One says that instead of storing the column names in a header like this:

| a   | b   | c   | d   |
| --- | --- | --- | --- |
| A   | B   | C   | D   |

We instead store the column names _on every line,_ in a wasteful display of underoptimization.

To store the column names _inline,_ right alongside the values!

The One insists that neither the field names nor the values should have spaces in them, and there must not be spaces after the commas in the parentheses at the end.

No one can agree on what this One means.

So the One stops trying to explain, walks to the whiteboard, and writes this:


```
/dev/something on /path/to/mount/point type sometype (mode,this,that,attr=value,etc)
```

The audience tilts its collective head in confusion.

The One is proposing that, instead of the standard tabular format like:

| device   | mountpoint  | readable | writable | suid  | relatime |
| -------- | ----------- | -------- | -------- | ----- | -------- |
| /dev/sda | /mnt/sinai  | True     | True     | False | True     |
| /dev/sdb | /mnt/horeb  | True     | False    | True  | False    |
| /dev/sdc | /mnt/olives | True     | True     | True  | False    |

We instead store a strange form of "pseudo-boolean" type,

in which `True` is represented as `type_name`,

and `False` is represented as simply not storing anything at all.

The strings `relatime` and `nodev` are pseudo-booleans of this type.

Everyone is opposed to this One's odd suggestion.

The Professional Developer -- those peddlers of mediocrity that they trumpet as Best Practices©®™ -- sees these decisions as amateurish, inelegant, and "not scalable."

So One agrees, and allows them to choose their preferred format.

But slowly over time, they notice that this One -- in making hundreds of small but equally odd decisions in One's private personal workflow -- has somehow reached a level of efficiency and speed in developing any POC for any task that no one else can keep up.

No one among the others understands that One's secret is not secret.

The secret was there all along, in the strange suggestion from before.

The secret is there for us, in the format of the `mount` command.

All we have to do is to open our eyes and see.
