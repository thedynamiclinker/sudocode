1: I need to see a doctor...

0: Exactly.

1: _(Nauseous)_ What?

0: Mathematics was sick. They needed a doctor. So they called this guy.

![[david-hilbert.jpg]]

0: Doctor Herr Professor the esteemed David Hilbert. See him?

1: _(Still a bit disoriented)_ Yeah.

0: There's your doctor.

1: _(Silently recovering)_ ...

0: The perfect one for the job. They called him and he called everyone. Called them together. All the mathematicians. A call to arms, in 1900. He was the sort of guy who could just come up with a list of questions for an entire field to work on, and then everyone would agree that's the agenda. He said "Ok everyone here's the deal. We've got some problems and I want you all to solve them. Here's the list." And then he reaches under that big hat and pulls out the following list:

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

0: Formal systems seem to have an equally prohibitive number of restrictions. I mean when you first try to use Formal Arithmetic, it feels like everything you want to do is illegal.

1: Sounds hard.

0: It's actually not. I think you'll enjoy it.

1: What makes you think that?

0: We've already seen some of it.

1: When?

0: The first programming language.

1: Ooooh that!

0: But things are gonna be pretty different once we're there.

1: I think I can handle it. I'm a professional devel---

0: Whenever you're ready.

1: Are we heading to another file?

0: Yep. This is the last one of the five. I don't want to startle you this time, so take your time and just let me know when you're re--- 1: [[We#The second law|pop rip]]
