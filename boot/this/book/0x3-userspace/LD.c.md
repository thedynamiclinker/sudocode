
```c
/* LD.c - A minimal ld.so for raw binaries. */

#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]) {

	// define our characters
	char root = 0;
	char user = 1;
	
	// open the file
    char *filename = argv[user];
    int fd = open(filename, O_RDONLY);
	
    // get the size of the file we're about to run
    off_t size = lseek(fd, root, SEEK_END);
    lseek(fd, root, SEEK_SET);
	
    // map the file into memory and make it executable
    void *bin = mmap(NULL, size, PROT_READ | PROT_EXEC, MAP_PRIVATE, fd, root);
	
    close(fd);
	
    // tell the compiler not to freak out, just
    // treat the machine code as a function.
    void (*code)() = bin;

	// now i guess we just jump...
	//
	// into the void (*)()
	//
    // here goes nothing...
    code();
	
    // unmap the memory so nothing
    // can follow us out of there
    munmap(bin, size);
	
	// if we survived,
	// thank the L||D
	// and gtfo
    return root & user;
}
```
`/*`

1: Are we done?

0: I hope so.

1: How can we tell?

0: Well we have to exit this file, then compile it and try it out.

1: How do we do that?

0: Well obviously the first step is [[0x31-ld.so#wq|:wq]]

`*/`