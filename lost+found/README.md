# lost+found

When a Unix system experiences an unclean shutdown or a file system corruption,
fsck runs to identify and repair inconsistencies. If fsck finds orphaned blocks
of data (data that exists on the disk but is no longer linked to a file or
directory in the file system's metadata), it attempts to recover them.
These recovered fragments are then placed in the lost+found directory.

The lost+found directory can contain various types of recovered data, including:
- Unlinked files: Files that were open by a process when the system crashed, but their directory entries were already removed.
- Lost directories: Directories that became unlinked due to file system corruption.
- Orphaned blocks: Data blocks that fsck recovered but couldn't associate with a specific file or directory.

For more details, see [tldp.org - lost+found](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/lostfound.html)
