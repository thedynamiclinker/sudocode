
The education of user, uid 1, in /usr, through the format of _Idk Howtos._

## /usr/bin/*

1. [[mouse|/usr/bin/mouse]], using code from [[mouse.so.1|/usr/lib/mouse.so.1]]

2. Make a hello world display server by reading whichever device file it's using (/dev/fb0), reverse engineering the format, and then writing to that device file.

3. Reading an image file out of memory.
	1. Open a browser, and open any image in that browser.
	2. It's now somewhere in your machine's memory.
	3. Given no other information, figure out how to write code to read that image out of memory.

4. Reading a GET request in transit.
	1. Open a browser, click on a link.
	2. Figure out the request it sent when you clicked, in sufficient detail that we can replay the same request and get the same result.

5. Write a Hello World filesystem.
	1. Get a USB key, and fill it full of zeroes. No filesystem, no nothing.
	2. Don't format it. That's cheating.
	3. Now write code that'll let you store a file on it, and then read the file back after the USB key is unplugged and plugged back in.
	4. Now write code to "delete" the file (overwrite the table of contents entry).
	5. Now write code that lets you "undelete" the file and recover it.
