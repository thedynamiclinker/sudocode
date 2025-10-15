1: What's that?

0: Looks like a man page.

1: Woah, does that say 1971?

0: Yeah, we'll get there eventually. `call import`

1: To the man pages?

0: To 1971. And to the man pages. `call import`.

1: We aren't even in 1971 yet?

0: No, we're a bit earlier than that at the moment. `call import`

1: When are w---

0: A bit earlier. `call import`. More urgent problem right now. There's an image coming up. Don't try to execute it or you'll get an invalid opcode exception and god knows if they set up the IDT yet. Jump past it with me.

```
jmp a_bit_later
```

![[ld-man-page.png]]

```
a_bit_later:
```

1: Who's they?

0: What?

1: You said "god knows if they set up the IDT yet." Who's they?

0: Whoever wrote this code.

1: You don't know who wrote it?

0: No. I thought this directory would be empty. `call import`.

1: You thought `/boot` would be empty?

0: Yes. `call import`.

1: How did you think the book got started?

0: I sort of thought it was up to me to explain that.

1: You said this directory was going to be about what it means to write a bible.

0: That was the intention but we haven't got there yet. So far I'm just trying to avoid all this code that was already here without blowing up the boot sector past 512 bytes.

1: It's already past 512 by---

0: I mean 512 bytes of instructions. We're still fine, but we need to be conscious about space. `call import`. Here jump past the rest with me.

```
jmp trampoline
```

根. (noun).
1. root
2. radical
3. genesis
4. foundations
5. a unicode character, pronounced in modern mandarin as [gen](https://en.wiktionary.org/wiki/%E6%A0%B9), and in the oldest known versions of the language as [ken](https://doc.cat-v.org/bell_labs/utf-8_history).
6. goto: [[0x20-initrd]]

```
trampoline: jmp 6
```

---

```
import:
	mov eax, 4   ; sys_write
	mov ebx, 1   ; stdout
	mov ecx, msg
	mov edx, len
	int 0x80
	ret
msg: db  "No time to explain. We have important things to do."
len: equ $ - msg
```

---
