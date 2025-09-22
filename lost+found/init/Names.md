## 0b10111 problems but a bit ain't one.

1: I need to see a doctor...

0: Exactly.

1: _(Nauseous)_ What?

0: They needed a doctor. Mathematics was sick. So they called this guy.

![[david-hilbert.jpg]]

0: Doctor Herr Professor the esteemed David Hilbert. See him?

1: _(Still a bit disoriented)_ Yeah.

0: There's your doctor.

1: _(Silently recovering)_ ...

0: The perfect one for the job. They called him and he called everyone. Called them together. All the mathematicians. A call to arms, in 1900. He was the sort of guy who could just come up with a list of questions for an entire field to work on, and then everyone would agree that's the agenda. He said "Ok every one here's the deal. We've got some problems and I want you all to solve them. Here's the list." And then he reaches under that big hat and pulls out the following list:

![[hilberts-problems.png]]

1: _(Feeling a bit better)_ Which one is the one about how mathematics is broken?

0: Look closely and see if you can find it.

1: Oh! The first one. About Cantor.

0: Nope. Not that one.

1: Hmm... I don't see anything about comprehension or Russell's paradox. How is 4 on there? Math is weird. 6 sounds hard. I don't know, I don't see anything about mathematics being broken on here.

0: It's 2.

1: What?

0: And also 10.

1: How is it---

0: They're basically the same.

1: How are 2 and 10---

0: Y'know. Binary.

1: No bad puns please. I'm still a bit dizzy from all the gotos.

0: Yeah those are considered harmful. That's why I swapped out the most recent one for a call.

1: _(Looking sick again)_

0: Anyways, naturally, 2 and 10 are basically the same thing and this would soon lead to the creation of computing as a field.

1: Woah really?

0: Yep.

1: How did THAT happen?

0: Ok so, problem 2 is the one that was motivated by Cantor and Russell. Everyone knew there were some serious bugs in the foundations. But just like in software, you can't just stop the world to fix a bug. Mostly, people just ignored it.

1: Ignored the bugs?

0: Exactly. But folks like Hilbert cared about the foundations.

1: Was Hilbert the first of the Foundational People?

0: Not really. I mean it wouldn't be so wrong to put him in that camp. He cared about the foundations, but he cared about everything. He was very much a mathematician's mathematician. He fit in well with the crowd. So much so that he sort of became their leader. He was sort of like the CEO of mathematics. And in the legends about this period, he's made out to be more of the kind of guy who'd get accused of doing "theology" (i.e., vague mathematics) than the type who'd get accused of being too concerned with foundations. He was both. Here's a clip from a paper that explains some background.

![[hilbert-theology-myth-1.png]]

![[hilbert-theology-myth-2.png]]

1: I almost fell asleep. Did I miss anything?

0: Not much. Just that Hilbert was sort of the Director General in mathematics, plus the bit at the end. "Without actually finding these systems, Hilbert proved... they exist." That's a non-constructive existence proof, and it's very much a signal that he's a classical guy. A mathematician's mathematician. Not someone who would choose foundational concerns over mathematics. Faced with a choice, Hilbert chooses mathematics first. Even in ways that made the old timers suspicious.

![[hilbert-theology-myth-3.png]]

0: See non-constructive existence proofs weren't always a common thing. But once they started, it was hard to stop. They made mathematics so much easier. And Hilbert would always choose mathematics.

1: Is there a point to this story?

0: Getting there. Ok so in his big list of problems, Hilbert mostly listed standard mathematical questions. But he threw a bone or two to the foundational questions too. Specifically, 2 and 10.

> Problem 2: Are the axioms of arithmetic consistent?
> Problem 10: Something about "Diophantine equations" that seems totally irrelevant.

1: I was about to say I don't see why 10 is relevant.

0: Good. It's not clear at first glance. But here's problem 10 expanded out in more words:

![[hilberts-10th-problem-1.png]]

0: See the relevance yet?

1: Not really.

0: Can't blame you. Here's a hint:

![[hilberts-10th-problem-2.png]]

1: Ooh, ok. Starting to sound like computing. But wait, mathematicians had been providing algorithms for computing stuff for like thousands of years hadn't they?

0: Of course. The problem here was that no such algorithm existed, though nobody knew that at the time.

1: Why is that a problem?

0: Well there had been cases of mathematicians proving that "No such X exists" in response to questions of the form "Find an X that does such and such." For example, the solvability of the quintic. Basically if you make high school algebra problems more and more annoying for a couple centuries until you're trying to solve $x^5 + ax^4 + bx^3 + ... = 0$, eventually a French kid shows you can't solve stuff like that and then gets shot in a duel over a girl.

1: You lost me.

0: Don't worry. Different story. Definitely not one we'll be covering here. The point is that mathematicians had run into questions that sound like "Solve X" and had managed to respond "That's impossible" just fine in the past. This time was different.

1: How is this different? This tenth problem sounds like it's about polynomial equations too.

0: See where it says "a general algorithm"?

1: Yeah, you highlighted it.

0: How do you prove that "no algorithm whatsoever can exist such that \[blah\]"?

1: I dunno.

0: What's the first step?

1: The first step of showing no algorithm exists such that \[something\]?

0: Yeah, what's step one?

1: I have no idea. Look I came here to learn computing, I don't know why we're still talking about ma---

0: Define algorithm.

1: You want me to defi---

0: No. I mean that's the first step.

1: Define algorithm?

0: Exactly. Hilbert's 10th problem didn't sound interesting on the surface. Maybe it is to mathematicians, but not to the Foundational People.

1: How _do_ you define algorithm by the way?

0: Great question.

1: You're not gonna answer me are you.

0: Not yet, but we're getting there.

1: Why do I feel like that's your answer to everythi---

0: You can prove that there's no real number that solves $x^2 + 1 = 0$ because the search space is just the real numbers. You can prove there's no solution to the quintic because the search space they cared about what stuff you can do in high school algebra: namely solutions that can be expressed in terms of $+$, $-$, $*$, $/$, and fractional powers like taking square roots, cube roots, $n^{th}$ roots, etc. For the quintic, the search space was a very limited kind of function.

1: Sort of following. So what?

0: What's the search space of possible solutions you have to check if the question asks you to find a general algorithm?

1: All algorithms?

0: All algorithms.

1: Oooooooh.

0: So thanks to Cantor and Russell, the effective CEO of mathematics has now put a bounty on the following two problems:

Problem 2: Prove that arithmetic is consistent.
Problem 10: A question that asks you to find _any algorithm_ that does a thing.

Problem 2 is definitely about the Foundations of Mathematics.

Problem 10 _might be_ about the Foundations of Mathematics.

1: Might be?

0: It's not clear from the problem statement. Think about it.
- If some solution exists to Problem 10, then Problem 10 is just normal mathematics.
- If no solution exists for Problem 10, then you somehow have to say something about _the space of all possible algorithms._

It turned out that Problem 10 didn't have a solution.

It wasn't solved until 1970.

But already by 1935, it had started a revolution in the foundations of mathematics that would eventually become our field.

1: Ok, I'm awake. Can we be done with the math stuff and get to computing now?

0: Perfect timing. That's exactly where we're heading.

1: Where?

0: To a place with so many restrictions and constraints that you'd expect it to be completely devoid of fun.

1: School?

0: More rules than that.

1: Work?

0: Way more rules than that.

1: I dunno, where?

0: Formal systems.

1: Huh?

0: Formal languages, and the formal theories built on top of them. Those objects studied by a strange culture we mentioned in passing a while back.

1: The ones with infinitely many axioms?

0: Those ones exactly. Rule after rule after rule after rule.

1: Sounds like a pain.

0: Usually that sort of thing is a pain! But it turns out these formal systems, despite all their restrictions, don't have the typical feel of a system with lots of restrictions. They don't feel like some high priest standing up and saying:

- You may eat any animal that has a divided hoof and that chews the cud.
- There are some that only chew the cud or only have a divided hoof, but you must not eat them.
- The rabbit, though it chews the cud, does not have a divided hoof; it is unclean for you.
- The pig, though it has a divided hoof, does not chew the cud; it is unclean for you.

1: What is this, some kind of logic puzzle?

0: No that's Leviticus.

1: What's Leviticus?

0: The part of the Old Testament that's just rules rules rules over and over and over and over and over and---

1: I got it.

0: Formal systems seem to have an equally prohibitive number of restrictions. I mean when you first try to use one, it feels like everything you want to do is illegal.

1: Sounds hard.

0: It's actually not. I think you'll enjoy it.

1: What makes you think that?

0: We've already seen some of it.

1: When?

0: The first code.

1: Ooooh that!

0: But things are gonna feel pretty unfamiliar once we're there.

1: I think I can handle it. I'm a professional devel---

0: Whenever you're ready.

1: Are we heading to another file?

0: Yep! Time to leave.

1: Can we stay here? I'm still feeling a bit sick from all the context sw---

0: If you need to. Let me just think of a section heading.

1: Why?

0: Well it's time to leave. That's kinda the point of this file. And naming things is one of those "hard problems." Nothing's accidental here. We need a good excuse to stay here in a file whose name is about leaving.

1: _(Unwell)_ How is "Names" about leaving?

0: What?

1: What?

0: Nevermind. Forget I said anything. Just follow me.

1: But you prom---

## Exodus Sicks: Name(s) of the L||D

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

goto: [[sinai|/山/月]]