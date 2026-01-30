
0: In this episode of "idk howtos", we'll be exploring the mouse in its natural habitat.

1: What's its natural habitat?

0: The `/dev` directory.

Goal: Make your mouse move by reading whichever device file it's using
1. `cat /dev/input/mouse0` or whatever device file your mouse uses.
2. Reverse engineer at least one line of the format.
3. Make your mouse move by writing to that file.
4. Figure out any mistakes in the problem statement along the way.

1: Where should I start?

0: `cat /dev/input/mouse0`

1: It says `Permission denied`

0: So...

1: Oh right! I forgot I have root now.

```sh
~ $ sudo cat /dev/input/mouse0
```

1: It's just sitting there hanging.

0: Is the mouse moving?

1: No.

0: So move it.

1: Oh...

```sh
~ $ sudo cat /dev/input/mouse0
(�(�(�(�(�(�(�(�(�(�(�(�8��8��8��(�8��(�8��(�8��8��8��8��8��8��8��8��8��8���(�(�(�(�(�(�(�^C�������
```

0: What does it say?

1: I can't read it.

0: Pipe it into `hexdump -C`.

1:

```
~ $ sudo cat /dev/input/mouse0 | hexdump -C
00000000  08 00 01 18 fe 01 18 fd  03 18 fd 02 18 fb 03 18  |................|
00000010  fb 03 18 fb 03 18 fc 01  18 fb 02 18 fd 01 18 f9  |................|
00000020  01 18 fb 01 18 f8 00 18  fa 01 18 f8 00 18 f9 00  |................|
00000030  18 fb 01 18 f7 00 18 fb  01 18 f7 00 18 f9 00 38  |...............8|
00000040  fc ff 38 fb fe 38 fc fc  38 fd fc 38 fd fa 38 fe  |..8..8..8..8..8.|
00000050  f9 38 ff f7 38 ff f6 28  00 f6 28 01 f9 28 03 f8  |.8..8..(..(..(..|
00000060  28 04 fb 28 0b f6 28 0c  f8 28 09 fa 28 11 f9 28  |(..(..(..(..(..(|
00000070  0f fc 28 0d ff 08 0c 00  08 0a 01 08 0d 04 08 08  |..(.............|
00000080  06 08 06 06 08 08 0a 08  05 0a 08 02 07 08 03 11  |................|
00000090  08 00 08 18 fe 10 18 fb  10 18 f9 0e 18 f7 0e 18  |................|
000000a0  f5 0d 18 f5 0a 18 f4 08  18 f1 08 18 f3 05 18 f4  |................|
000000b0  02 18 fa 01 18 f3 00 18  f8 00 38 fa fd 38 f8 fd  |..........8..8..|
000000c0  38 f7 fa 38 f9 fa 38 f9  fa 38 f8 f8 38 f9 f6 38  |8..8..8..8..8..8|
```

1: Still not seeing any patterns.

0: Were there any patterns in how you moved the mouse?

1: No...

0: Well, do something simpler.

1: Wow I feel dumb. Ok...

_(Narrator: 1 tries a few things.)_

1: Got it! If I just move the mouse down, it says this:

```
~ $ sudo cat /dev/input/mouse0 | hexdump -C
00000000  28 00 ff 28 00 fd 28 00  fd 28 00 fe 28 00 ff 28  |(..(..(..(..(..(|
00000010  00 ff 28 00 ff 28 00 ff  28 00 ff 28 00 fe 28 00  |..(..(..(..(..(.|
00000020  ff 28 00 ff 28 00 ff 28  00 ff 28 00 fe 38 ff ff  |.(..(..(..(..8..|
00000030  28 00 ff 28 00 ff 28 00  ff 38 ff ff 28 00 fe 28  |(..(..(..8..(..(|
00000040  00 ff 28 00 ff 28 00 ff  28 00 ff 28 00 ff 28 00  |..(..(..(..(..(.|
00000050  ff 28 00 ff 28 00 ff 28  00 fe 28 00 fe 28 00 ff  |.(..(..(..(..(..|
00000060  28 00 ff 28 00 ff 28 00  ff 28 00 ff 28 00 ff 28  |(..(..(..(..(..(|
00000070  00 ff 28 00 ff 28 00 ff  28 00 ff 28 00 ff 28 00  |..(..(..(..(..(.|
00000080  ff 28 00 ff 28 00 ff 28  00 ff 28 00 ff 28 00 ff  |.(..(..(..(..(..|
00000090  28 00 ff 28 00 ff 28 00  ff 28 00 ff 28 00 ff 28  |(..(..(..(..(..(|
000000a0  00 fe 28 00 ff 28 00 ff  28 00 ff 28 00 ff 28 00  |..(..(..(..(..(.|
^C
```

1: Seems like mostly `ff 28 00` over and over.

0: Great! What happens if we write that to the device?

1: Dunno. Let's see.

```python
def down(n):
	fp = open('/dev/input/mouse0', 'wb')
    for k in range(n):
        fp.write(b"\xff\x28\x00")
	fp.close()
        
>>> down(100)
```

1: It's not moving.

0: Hmm. Well, `28` shows up first in the hexdump. Maybe start with that?

1: Ah, good idea.

```python
def down(n):
	fp = open('/dev/input/mouse0', 'wb')
    for k in range(n):
        fp.write(b"\x28\x00\xff")
	fp.close()
        
>>> down(100)
```

1: Still not working.

0: Let's ask @2.

1: @2: What's going on here?

---

@2 here: You successfully **sniffed** the kernel’s mouse bytes, but you’re trying to **inject** them into the _wrong place_. So: **reading works; writing won’t ever move your cursor.**

1: What's the right place?

@2: `/dev/uinput`

1:

```
~ $ sudo cat /dev/uinput
cat: /dev/uinput: No such device
```

@2: Why `cat /dev/uinput` says “No such device”

- `/dev/uinput` is **not a readable stream device**.

- It is a **write-only ioctl control device**.

So:

```
cat /dev/uinput
```

→ kernel returns **ENODEV**  

→ `cat` prints _“No such device”_

This does **NOT** mean the node doesn’t exist or isn’t usable.

It only means: _“this device does not support read()”_.

That error is expected and correct.

> Think of `/dev/uinput` as a **mail slot**, not a wiretap.

1: So how can I move the mouse?

@2: Try this:

![[mouse.so.1]]

---

1: This code is gross.

0: Let's give it some love.

1: How do you give code some love?

0: Delete it!

1: Which parts?

0: I dunno. Whichever parts we can delete without breaking it.

_(Narrator: 0 & 1 proceed to delete bits that seem unimportant and re-run the code to see if it still works.)_

