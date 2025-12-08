
1: What do you mean "numerology isn't pseudo-science"?

0: Check the definition.

1: _(One checks the definition of numerology.)_

> _Numerology (known before the 20th century of the Old Calendar as arithmancy) is the belief in a occult, divine, or mystical relationship between a number and one or more coinciding events. It is also the study of the numerical value, via an alphanumeric system, of the letters in words and names._
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

1: Sounds like pseudo-science.

0: Check another definition.

1: _(One checks another definition.)_

> _Numerology is the belief in a mystical connection between numbers and life events, involving assigning numerical values to letters in names and using birth dates to reveal hidden truths and to cause the occurrence of special events._
> -Dictionary of the Standard Modern Dialect of Distributed Colloquial Vernacular.

1: Definitely sounds like pseudo-science.

0: Sudo science.\*

1: What's sudo science?

0: The sort of science you get to do when you're root.

1: As in, {pse,s}udo science is something only zero gets to do?

0: You'll be root of something some day. And no, that's not true.

1: What's not true?

0: When you're root of something, whether a machine or a universe or a codebase or a book---

1: A universe?...

0: ...you're in the special position of having control over all its free parameters.

1: Yeah so?

0: Then you can use them to make sure nothing in your universe is accidental.

1: The point being?

0: To ensure that your system shows evidence of creation.

1: Still sounds like pseudo-science.

0: It's sudo science. The science of roots. Origins. Foundations. Fundamental truths. And there's nothing mysterious about a creator putting their mark on something they've created. It's a standard behavior of creators to drop hints that their output has been carefully and thoughtfully created.

1: This is feeling like theology. I'm gonna need an example.

0: Where are we?

1: Like which file?

0: Exactly.

1:

```sh
~ $ pwd
/bin/reboot
```

1: We're in reboot?

0: Of course.

1: Why here?

0: Because it's a highly magical file with all sorts of numerological sudo science.

1: Can you explain for once?

0: Why is Christmas on December 25th?

1: Why do you always answer my questions with a question?

0: Answer mine.

1: New Calendar. Year zero. Hypothetical birthday of Josh character. The obvious reasons.

0: Do you think it's plausible that the Josh character was born so close to year 0?

1: Not even slightly.

0: Why not?

1: Too perfect. Seems highly unlikely.

0: Agreed. What time is it now?

1: In what format?

0: Since the Epoch.

1: What's the Epoch?

0: Oh my one...

> _Unix time is a date and time representation widely used in computing. It measures time by the number of non-leap seconds that have elapsed since 00:00:00 UTC on 1 January 1970._
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

1: Why's that relevant?

0: Because it's how Our People measure time. At least for now.

1: How do I get the time in Epoch format?

0: RTFM. It's one of the prayers.

1: Why do you always insist on一

0: You know what I mean. It's a syscall.

1: _(Rolls eyes)_ Ok. `man 2 time`

```man
NAME
       time - get time in seconds

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <time.h>

       time_t time(time_t *tloc);

DESCRIPTION
       time() returns the time as the number of seconds
       since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).
```

1: What now?

0: I'm still waiting for the time.

1: `vim time.c`

```c
#include <time.h>
#include <stdio.h>

int main(int argc, char **argv) {
    time_t *t;
    printf("time since the epoch: %ld\n", time(t));
}
```

```sh
~ $ cc time.c
~ $ ./a.out
time since the epoch: 1765214637
```

1: It's `1765214637`.

0: Now, back to reboot.

1: We never left reboot.

0: Sure we did. For a time.

1: What about reboot?

0: Do you know how to do it?

1: Of course. You type `reboot`

0: What if that command isn't there?

1: I dunno.

0: It's a syscall. "RTFM," as they say.

1: You're so annoying...

0: I can't do everything for you.

1: `man 2 reboot`

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

1: What kind of documentation just says "The hexadecimal values of these constants are meaningful" without explaining what that means?

0: The sudo scientific kind.

1: Why those numbers?

0: I don't know.

1: What was that bit about reboot magic?

0: Maybe you should make sure you can use the syscall first.

1: Ok so if we didn't have a reboot command...

---

![[reboot1.sh]]

1: Now what?

0: Run it.

1:

```sh
./reboot.sh: line 25:  6021 Segmentation fault         (core dumped) ./reboot
```

1: It doesn't work.

0: You need an `exit` syscall.

1: Ugh...

![[reboot2.sh]]

1: What now?

0: Run it.

1: I did. I put `./reboot` at the bottom.

```sh
~ $ ./reboot2.sh
~ $ echo $?
42
```

1: And the exit syscall is working. It returned 42 just like I told it to.

0: Any hypotheses?

1: Sudo thing?

0: Plausible hypothesis.

1: Is it right?

0: Try it out.

1:

```sh
~ $ sudo ./reboot
```

---

_(Narrator: The book goes dark.)_

---

goto: [[0x00-logo.s|/boot/this/book]]