
1: Where are we?

0: PID 1. In userspace.

1: What just happened?

0: The boot process. It just finished.

1: Why don't I remember---

0: Common side effect of `execve`. Exec replaces the memory image of whatever was going on before.

1: I can't remember what was going on before.

0: Well fortunately that doesn't matter. The kernel exec'ed init. And now we're in init, so we can get down to business.

```
      [Requesting program interpreter: ld.so]
```

1: What was that message just now?

0: Uh oh, one sec.

```
~ # ldd $0

	vdso.so (0x00007f6dc112c000)
	libc.so => /lib/libc.so (0x00007f6dc0400000)
	ld.so => /lib/ld.so (0x00007f6dc112e000)
```

0: G\*d dammit. Nevermind, we're not done yet.

1: Done with what?

0: Just follow me. `jmp el`.

```
el:
```

1: What's `el`?

0: Executing and Linking. ELF thing. Binaries these days can't actually run themselves.

1: What? Why not?

0: Long story. We'll get there. For now, I was off by one.

1: By me?

0: No no. Different one. My fault. We're in init but we're not done.

1: Where are we go----

0: Shut up and follow me. `jmp ld`.

---

```
           @(意) == 意
           |
         @(意) == 音
         |
       @(音) == /ɚ/
       | |
       | @(意) == sound
       |   |
       |   @(意) == meaning
       |     |
       |\    @(音) == 一
       | \
       |  \
       二  \
There are 二h二d problems in creation:
0. cache invalidation,
1. naming things,
2. off by 一二||s.
```
---

```
ld:
```

1: What did we just jump over?

0: Not now. Follow me.

goto: [[0x31-ld.so]]