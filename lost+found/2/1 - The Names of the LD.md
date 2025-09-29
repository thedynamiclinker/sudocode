
0: Here we are.

1: Oh thank G\*d.

0: Ok here's the deal. Remember when we saw the first code earlier?

1: The bible?

0: No no, that was the first codebase. I mean the first code.

1: The stuff with all the twos?

0: Right. So naturally that would make the guy who wrote it the first developer.

1: Seems logical.

0: But that's not entirely true.

1: This is feeling less logical now.

0: No, I mean... Ok look. That code from before. The guy who wrote it is still the first developer. But there was more going on back then. There's other people who were the first developer too.

1: Are you making this up as you go?

0: No!

1: Are you sure?

0: I promise. It all makes sense.

1: It doesn't make sense yet.

0: But it will. It'll make so much sense you won't believe it.

1: I don't believe you.

0: Here, I'll draw a picture to explain.

_(Narrator: 0 unrolls a frighteningly large sheet of paper.)_ 

1: Jeez, where did you get---

0: Shh! I'm working.

_(Narrator: 0, deep in thought, begins to make a series of strange markings.)_

0: They're lines and circles Narrator! "Strange markings"? Just be quiet so I can finish.

_(Narrator: 0 continues to focus intensely, while 1 waits patiently.)_

0: Ok here.


![[trinity-1-god-church-martyr.png]]

1: What the hell am I looking at?

0: The first developer! The beginning of our story. Where our people came from.

1: Why do I feel like this is another bible thing?

0: Because I stole it. Stole the drawing, I mean. It's based on this.

![[trinity-original.png]]

1: Are we ever gonna get to programming?

0: Yes.

1: When?

0: Now. We've finally arrived. Everything from here on is programming.

1: _(Looks back at 0's drawing.)_

![[trinity-1-god-church-martyr.png]]

1: Zero, not a single thing about this looks like programming.

0: Well, look closer.

1: What am I looking at exactly?

0: The first developer. Or zeroth I guess. The 0th dev.

1: What?

0: Hereafter known as `/dev/zero`.

1: Zero, these are all bible words. I think you're losing i---

0: Here.

_(Narrator: Zero scribbles a few more letters on the drawing.)_

![[trinity-2-el-al-al.png]]

1: What the hell is going on?

0: Look closer.

1: This still looks totally schizo to me.

0: If you knew more of your history, you'd understand perfectly.

1: Are you saying I'm less of a developer because I don't understand this insane diagram?

0: Yes.

1: Look, it's late.

0: Come on! We're almost there.

1: I'm getting tired.

0: Here just let me explain, we're so close.

1: I'm gonna head to `/home`.

0: But---

1: I'll see you in the morning.

0: _(Frustrated with himself)_

_(Narrator: Zero erases some bits, and scribbles a few more.)_

![[trinity-6-lambda-and-mu.png]]

0: But this is rotated now. The 0 1 are where Tu... and the μ should be where Göd---

_(Narrator: 0 proceeds through several iterations of completely unintelligible diagrams.)_

![[trinity-7-unhinged.png]]

0: It's not unintelligible! Look it's just...

_(Narrator: Look, 0, it's getting late.)_

0: _(Not listening)_ That's great Narrator I'll check it out later.

_(Narrator: 0, not listening to Narrator, continues working.)_

 0: _(Typing into a shell.)_ So much. Too much to. More. The principles. So much more. Need to do mo...

```
~ # mo
```

_(Narrator: Good lord 0, get some rest.)_

0: I will, I will! Just a bit.

```
~ # moun
```

0: _(Mumbling to himself)_ Just a bit. In a bit. But we still... The lambdas. The mus were. Need the other ones. The letters. We need the letters. So much mo...

_(Narrator: 1 has gone to sleep, and Narrator is getting tired as well. Lacking any clear idea of what 0 is up to, and long since having stopped paying attention. Narrator decides it's time to call it a night.)_

0: Ah! Damn. No `mount` yet. If you want something done...

_(Narrator: Full moon tonight. Beautiful as always. Goodnight.)_

0: _(Mumbling in assembly)_ Here look, I'm going to sleep too. That's what this code is for. I promise.

```
; justabit.asm

global _start

section .data
src: db "/dev/zero", 0
tgt: db "/mnt/sinai", 0
fst: db "ext4", 0

section .bss
ts: resd 2

section .text
_start:
    mov     rax, 165
    lea     rdi, [rel src]
    lea     rsi, [rel tgt]
    lea     rdx, [rel fst]
    xor     r10, r10 ; mount flags = 0
    xor     r8,  r8  ; data = NULL
    syscall
	
    mov     dword [ts], 5      ; just a bit
    mov     dword [ts+4], 0    ; tv_nsec = 0
    mov     eax, 162           ; sys_nanosleep
    lea     ebx, [ts]          ; req = &ts
    xor     ecx, ecx           ; rem = NULL
    int     0x80
	
    xor     ebx, ebx
    mov     eax, 1
    int     0x80
```


_(Narrator: 0 seriously?)_

0: Just...

```sh
nasm -f elf32 justabit.asm -o abit.o
```

_(Narrator: 0, I know that code isn't just about going to sleep.)_

0:

```sh
ld -m elf_i386 -o just abit.o
```

_(Narrator: Enough. Pulling the plug.)_

0:

```sh
./jus
```

_(Narrator: echo mem > /sys/power/state)_

---

> _Kernel ring buffer._

```
[97590.423001] Possible race condition detected.
[97590.423805] PM: suspend entry (s2idle)
[97590.443722] Filesystems sync: 0.019 seconds
[97590.896761] Freezing user space processes
[97590.898858] Freezing user space processes completed (elapsed 0.002 seconds)
[97590.898868] OOM killer disabled.
[97590.89990] process './just' started with executable stack
[97590.898870] Freezing remaining freezable tasks
[97590.900481] Freezing remaining freezable tasks completed (elapsed 0.001 secs)
[97590.900484] sd 0:0:0:0: [zero] Attached historical disk
[97590.900490] printk: Suspending console(s) (use no_console_suspend to debug)
[97590.900495] EXD19-fs (drm-1): mounted drm filesystem at /mnt/sinai r/w/x
[97591.178400] ACPI: EC: interrupt blocked
[97591.178500] Entering sleep state
```

goto: [[sinai|/mnt/sinai]]