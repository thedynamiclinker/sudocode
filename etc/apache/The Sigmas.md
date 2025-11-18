
0: Yeah I know.

1: What did mathematicians do when they heard this?

0: Nothing.

1: What?!

0: Mostly nobody noticed. At least not many mathematicians.

1: How did most mathematicians not notice that most of their field is one of five sentences?

0: Mathematicians mostly don't pay a lot of attention to Foundations.

1: Good lord. What are the five sentences?

0: Not now. We'll get there eventually. We're still at Church.

1: I thought this was Hirst.

0: Everything's connected. Ok so Hirst's doctoral advisor, one of his two advisors, was Friedman.

1: Same Friedman?

0: Same one. Here's Friedman in 1997.


![[friedman-1997-the-formalization-of-mathematics-01.png|350]]


0: Here's the first line of that paper:

![[friedman-1997-the-formalization-of-mathematics-02.png|300]]

1: I thought they formalized mathematics with ZFC.

0: Well, that's the standard story.

1: When did ZFC come out again?

0: Before Church. Remember how ZFC was what Church wrote his PhD thesis on?

1: Oh right.

0: But you're right to be confused. See in principle we supposedly "formalized mathematics" back before 1927 when Church finished his PhD thesis. But in practice, here's Harvey Friedman in 1997.

![[friedman-1997-the-formalization-of-mathematics-03.png]]

1: Is he gonna say "Everyone's wrong"?

0: No, he's gonna say they're basically correct.

1: What?!

![[friedman-1997-the-formalization-of-mathematics-04.png]]

1: What's the point here?

0: ZFC isn't _wrong._ And it's not technically _not foundations._ But it's almost certainly _the wrong foundations._

1: No idea what you mean by that.

0: Let's keep reading.

![[friedman-1997-the-formalization-of-mathematics-05.png]]

1: Grossly inconvenient?

0: He's acknowledging the same thing Hirst acknowledged. Nobody _likes_ using ZFC, and basically nobody does, if by "using" it we mean "working inside it to do mathematics," or even "working inside it to do foundations," or even (most surprisingly) "working inside it to do set theory." Grossly inconvenient is an understatement.

1: Ok so what's Friedman's suggesting?

0: Let's see.

![[friedman-1997-the-formalization-of-mathematics-06.png]]

1: "Obtain detailed information about the logical structure of mathematical concepts"?

0: What's the question?

1: MATHEMATICIANS DON'T ALREADY HAVE THAT INFORMATION?!

0: Well in a lot of ways they do. Friedman's talking about something much more precise. Remember, he's the guy who kicked off the research program that eventually showed that most of mathematics is equivalent to one of five sentences. By "logical structure" here I assume he means something much more like a generalization or extension of Reverse Mathematics.

1: What's Reverse Mathematics?

0: The research program that eventually showed that most of mathematics is equivalent to one of five sentences.

1: Damn. Can we read some reverse mathematics eventually?

0: It can be pretty technical, but absolutely, we'll get there. Not in this era, but a couple eras down the road.

1: What's this era?

0: The 1930s.

1: We're in the 1930s?

0: Well remember we're still at Church.

1: I thought this was Friedman in 1997.

0: It is. But we're still at Church. I'm just explaining that Church was dissatisfied with the standard foundations in his day for a reason, and those reasons haven't gone away in 100+ years since then. But right now, the era we're in is the one that started with Cantor's Paradise and Russell's Paradox and Hilbert's program and which led to three characters in the 1930s giving three different definitions of computation that turned out to be equivalent. We might call this era, say, "Testament (-1)". So we won't be covering Reverse Mathematics yet. But some time in Testament 0, when we get to Ken and Unix and C, and computing changes forever, a few years after that, Harvey Friedman shows up and changes mathematics forever.

1: I thought you said mostly nobody noticed Friedman's stuff.

0: The mathematicians didn't. At least not as much as they should have. But the foundational people noticed. And eventually we'll see that the mathematicians start to get converted by the foundational people, but we won't get there until some time around 20XY.

1: 20XY? That's now!

0: Exactly. It'll take a while to get there. Let's not jump ahead. For now, we're still at Church. So as Harvey was saying back in 1997...


![[friedman-1997-the-formalization-of-mathematics-07.png]]

1: I feel like programmers think about the notation thing more than mathematicians do.

0: Of course! We have to implement everything we do. And our codebases actually have to compile and execute. Notation is way more important when you can't skip steps.

1: For real.

![[friedman-1997-the-formalization-of-mathematics-08.png]]

1: _Mathematicians don't even have a database of mathematical information yet?_

0: Well in a sense they do. There's the academic literature.

1: _(Eyes wide in disbelief.)_ So, papers?

0: Well y'know, PDFs. But yeah.

1: That's not exactly a database.

0: Well there's also the arXiv.

1: What's that?

0: Sort of a "github for PDFs", minus the git part.

1: What?

0: It's a place where mathematicians and other academics can publish papers to get their peers to review them, which normally isn't possible for months or years with the normal academic publishing system.

1: What's the normal academic publishing system?

0: They call it "peer review."

1: _(Squinting)_ There's an entire system that exists "so your peers can review things" because "having your peers review things" isn't possible with "peer review"?

0: It's still possible. Just not for months or years.

1: What happens during "peer review"?

0: That's the part where your peers can't review things.

1: _(Turning red)_ My head hurts.

0: Good. Don't think about it too hard. Academia is basically dead. But it wasn't dead at all back in the 1930s where we currently are. And it wasn't entirely dead in 1997 when Friedman's writing this. So back to Church. Here's Friedman in 1997:

![[friedman-1997-the-formalization-of-mathematics-09.png]]

1: What does he mean "The more ambitious concept of formalization includes proofs"?

0: Right, so if you look back through the conversation to where Friedman said "the formalization of mathematics is extraordinarily inconvenient in any of the current formalisms," back then he said (in slightly different words) that there are two things we want in a formalization of mathematics:

1. At minimum, a formalization of mathematics where we can just write down our definitions and the statements of theorems, and not even try to do proofs.
2. More ambitious, a formalization of mathematics where we can actually do proofs. "These are even more inconvenient in present formalisms"?

1: _(Horrified)_ Hold on hold on hold. Let me get this straight. It's been a century since ZFC.

0: More than a century.

1: And this guy is saying that ZFC can't even write down the basic definitions and theorems of mathematics?

0: Well it _could_ in princ---

1: But nobody has.

0: Basically.

1: So nobody does that. The basic stuff. Definitions. Theorems. Like if mathematics was a C program, they're not even writing the header files in ZFC.

0: Good analogy! And yes.

1: Yes?

0: Yes as in no. They don't do that.

1: And then actually proving stuff in this system is a whole different story. As in, if header files are too hard to implement, then C files are out of the question because doing the actual implementation would be much harder.

0: Good analogy again!

1: So yes?

0: Yeah that's basically the situation.

1: _(Staring at the ground)_ Look I know you say things like "Everybody's wrong about everything," and I know usually that's just you exaggerating.

0: I never exaggera---

1: Yes you do.

0: Ok yes I exaggerate all the ti---

1: How did this happen?

0: I dunno, I guess it's just how I tal---

1: No I mean mathematics.

0: What about it?

1: _(Gazing into the abyss)_ I mean I don't know that much mathematics. I'm a programmer. But I always had this feeling that mathematics knew what it was doing.

0: It usually works pretty ok---

1: That they had their shit together over there better than we do. I mean they're supposed to be the foundations of all knowledge.

0: Mathematicians don't really think much about foundat---

1: Or at least the foundations of the hard sciences.

0: Again, foundations isn't really their thin---

1: And I don't think I'm the only One who's felt a bit inadequate in the past when I approached some piece of math and couldn't understand what was going on.

0: That's not your fault. It also doesn't mean the math is wrong. Most of mathematics is perfectly fine.

1: Fine how?

0: Fine as in it's probably right.

1: _Probably?_

0: I mean yeah.

1: How is _probably_ good enough?

0: I mean that issue runs deeper than just math. It hits foundations too. Remember Church's first version of lambda calculus turned out to be inconsistent. Haskell Curry's combinatory logic turned out to be inconsistent too. So did Frege's system where Russell learned logic and found his paradox. And don't get me started on the Kunen inconsistency, the large cardinals people are basically a relig---

1: So that many logics turned out to have contradictions.

0: Yep.

1: And basically _none_ of modern mathematics is written down in ZFC.

0: Correct.

1: In the system that claims to be its foundations.

0: Accurate.

1: Or in any other formal language.

0: Basically. Though that's been changing recen---

1: I think I need to sit down.

0: You are sitting down.

1: Ok I'll just shut up and listen and see if this existential crisis goes away.

0: It's ok! Don't try to make it go away. This existential crisis is something every one has to go through if you eventually want to understand our field.

1: Which field?

0: Computing.

1: I though we were the foundational people.

0: Well, maybe the reason I called us that is so you'd eventually start to see the the point of all this.

1: Point of what?

0: That your field -- our field -- computing I mean. We may come to be responsible for things we hadn't expected to be put in charge of.

1: Such as?

0: We'll get there. Before we get to the new foundations, we've got to cover the old ones. Ready to get back to Church and the 1930s?

1: Yeah, let's get back to that.

0: Ok, starting from what Friedman was saying in 1997, let's rewind the clock...

![[friedman-1997-the-formalization-of-mathematics-10.png]]

0: Logic and mathematics have remained largely separate, with mathematics remaining almost entirely unformalized and without any practically useful foundations.

![[friedman-1997-the-formalization-of-mathematics-11.png]]

0: I would be nice if mathematics was stored in something other than PDFs.

1: Ya think?

0: I know it seems obvious to us, but outside of developers not everyone thinks that way. But Friedman's basically saying here that it would be nice if mathematics was stored in a format that's both human readable and machine readable.

![[friedman-1997-the-formalization-of-mathematics-12.png]]

0: Then he goes into standard formal set theory.

1: Wait let me stop you there. Can we actually see this "formal set theory"? We've been talking about it for a while but I don't think I've actually seen the language or its axioms, except for a few lines in that Hirst book up above.

0: Perfect timing. As I was saying, that's what Friedman's getting to right now.

![[friedman-1997-the-formalization-of-mathematics-13.png]]

1: What does this mean?

0: The formal language of ZFC has these symbols:

- $\lnot$ : The "NOT" symbol. If $A$ is a sentence, then $\lnot A$ means "not A" or "the negation of A."

1: Can you be more formal and not use words like "sentence"?

0: Sentence is a formal term in logic! But good question. Here's the definition.

![[meaning-of-sentence-in-logic.png]]

1: Hah it says "For a less technical introduction, see Statement."

0: Why is that funny?

1: I dunno, I feel like "Statement" sounds more technical than "Sentence."

0: Fair. Either way, "sentence" is a standard term in logic, and if $A$ is a sentence, then $\lnot A$ means "not A" or "the negation of A."

1: So if  is true, then $\lnot A$ is false?

0: Yep. Ok next one:

 - $\rightarrow$ : The "IF THEN" symbol. If $A$ and $B$ are sentences, then $A \rightarrow B$ means "A implies B" or "if $A$ then $B$". Now in natural language, "if then" is used in lots of ways. In standard logic it's only used in one specific way, which is that $A \rightarrow B$ can only be false in the specific case when $A$ is true and $B$ is false. In all other situations we say $A \rightarrow B$ is true.
 
1: So if $A$ and $B$ are both false then $A \rightarrow B$ is true?

0: Yep. Feels a bit weird at first but it doesn't cause too many problems. Plus, the other ways of defining the conditional are a bit of a rabbit hole, and they're not relevant for us here. If you're curious, look up "Material conditional" and poke around for any mention of alternative definitions. For now, that's implication.

1: Got it. What's next?

0:
- $\land$ : The "AND" symbol. You can guess when $A \land B$ is true and when it's not. There's no philosophical subtlety to and.

1: Thank god.

0:
- $\lor$ : The "OR" symbol. $A \lor B$ is only false when both $A$ and $B$ are false. In all other cases, whether one or the other or both are true, then $A \lor B$  is true.

1: Ok I know I asked for this, but I'm starting to realize I already know this stuff.

0: Do you?

1: Boolean logic? I'd sure hope so. I'm a professional devel---

0: So no philosophical subtlety to "OR" either?

1: Zero c'mon, let's keep moving.

0: I was about to keep moving, but since you're sure you understand OR---

1: _I UNDERSTAND OR!_

goto: [[The Sans 1]]