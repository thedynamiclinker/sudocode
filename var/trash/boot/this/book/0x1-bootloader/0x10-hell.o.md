1: Um, zero?

0: What?

1: This is even worse than the last file.

0: We haven't reached the last file yet, this is still the bootloader.

1: No, not last as in final, I mean last as in previous.

0: Oh. Wow that's a pretty serious design flaw in English.

1: Yeah idk who made those two words mean the same thing.

0: I see the problem now though.

1: Is it the fact that we're in a file called `hell`?

0: No no, that's `hell.o`. It's an object file. That's not the problem. It's just the reason why things aren't entirely "readable" in here. Object files are never readable.

1: So what's the problem?

0: When I said `jmp past` in the last file we jumped into the past.

1: Last as in previous?

0: Of course.

1: Ok yeah that makes sense.

0: Here, just jump past this part with me. I'll make sure to be more clear this time.

```
jmp futr
```

---

```
/* You are not expected to understand this */

section .text

He||.o
 W||ld
 |OR       月
 ||          ⁱ
 三二一   φ @ l u x   曰
 .      .     ₙ
 .    .    日
 .  .
 ..
L||D
 && it was good;

// So sayeth the L||D.

cmp || OR

je _start
```

**⚠️ WARNING**
**⚠️ YOU MISSED A GOTO**

[You](https://en.wikipedia.org/wiki/A_Commentary_on_the_UNIX_Operating_System#%22You_are_not_expected_to_understand_this%22) [are](https://en.wikipedia.org/wiki/Phi) [not](https://en.wikipedia.org/wiki/At_sign#History) [expected](https://en.wiktionary.org/wiki/lux#Latin) [to](https://stackoverflow.com/questions/10285410/what-are-s-files) [understand](https://en.wikipedia.org/wiki/.sys) [any](https://en.wikipedia.org/wiki/Object_file) [of](https://wiki.osdev.org/Linker_Scripts) [the](https://en.wiktionary.org/wiki/日) [current](https://en.wiktionary.org/wiki/月) [section](https://en.wiktionary.org/wiki/曰) [yet](https://en.wikipedia.org/wiki/En_(Cyrillic)) [but](https://stackoverflow.com/questions/14836768/how-do-and-and-or-operators-work-in-bash) [we](https://en.wikipedia.org/wiki/Dynamic_linker) [promise](https://en.wikipedia.org/wiki/Heth) [it](https://en.wikipedia.org/wiki/Tetragrammaton) [will](https://en.wikipedia.org/wiki/Names_of_God_in_Judaism#Erasing_the_name_of_God) [be](https://en.wikipedia.org/wiki/Naming_taboo) [more](https://translate.google.com/?sl=en&tl=zh-CN&text=root&op=translate) [clear](https://en.wikipedia.org/wiki/Logos) [by](https://en.wiktionary.org/wiki/fiat_lux) [morning](https://en.wikipedia.org/wiki/Let_there_be_light)

**⚠️ IGNORE THIS PART**
**⚠️ WE KEEP TRYING TO REMOVE IT**
**⚠️ BUT THE BOOK WON'T COMPILE WITHOUT IT**
**⚠️ SINCERELY,**
**⚠️ LD**

```
_start:
```

goto: [[var/trash/boot-dialogues/this/book/0x1-bootloader/0x11-wor.ld]]

---

```
futr:
```

1: Um, zero? There's nothing down here.

0: Dammit, my fault again. Early boot is rough. Follow me.

```
jmp _start
```
