
- NOTE
- This is a very bare bones skeleton of what eventually needs to go here.
- This file is closer to a set of notes than it is to a rough draft.
- If you're not one of the Authors of this book, ignore this file.

---

- In this era of prehistory, studies of foundational issues, of formal arithmetic and logic, appeared to be little more than grown adults in a sort of super advanced kindergarten. Little did they know that exactly three ingredients -- arithmetic and logic -- would turn out to be all that was needed to build an ALU. Add memory to an ALU and you've got a CPU. And with a CPU, the logic of every other discipline could be emulated. Why don't we have geometry or algebra or topology processing units? In a practical sense we do, any time we use GPUs for speed. But in principle, when it comes to what's required for computation, super advanced kindergarten turned out to be all we need.
- Say before we get to We dialogue: The problem with writing a history of any idea is that you can find the seeds of any big idea in writers almost arbitrarily far back in history, the end result of which (if taken seriously) is that you better learn hieroglyphs because you're gonna end up attributing basically everything to ancient Egypt. 
- To solve this problem, we need a creation myth. The creation myth should be designed to be as true as possible, while at the same time allowing an effectively infinite number of historical precursors to be treated as rounding errors or archaeology.
- To see the need for a creation story when it comes to the history of computing, we up here in the kernel will begin by demonstrating what would happen to the narrative if we tried to do without one. We will see that this attempt leads to an overemphasis on a wacky grab bag of partially cooked ideas and bizarre notations, some of which were legitimately brilliant and ahead of their time, but none of which are relevant enough to the history of computing to be worth mentioning In The Beginning.
- The Creation Story data type solves this problem. Properly executed, the Creation Story is a pragmatic truncation of history at a finite time in the past, before which all events are declared not to be relevant. This is, of course, in any literal sense, untrue, in no small part because the motivation for creating anything (whether a universe or a book) has as its cause a set of events that came before it. Nevertheless, the Creation Story is a pragmatic necessity. If history is a Taylor Series, the Creation Story is its truncation to finitely many terms.  The only alternative is the sort of history that Scott Aaronson pokes fun at in the title of his book "Quantum Computing Since Democritus."
- Therefore, in this file, being as we are in kernel space, safely in high memory well above the narrative below, we will sketch the prehistory of the field that became computing, to make the case that a proper Creation Story is the right solution to the problems in the narrative we tell in user space down below. What follows is a brief prehistory of the field, which will be rounded to zero and treated as nonexistent in the creation story that follows.

Logic in general.
- Logic faces an infinitely harder premathematics problem than any other part of mathematics. Creating a notation for geometry, numbers, or calculus needs only to talk about those areas. 
- Creating a notation for logic, however, needs to decide on a notation and set of basic definitions for the formalization of potentially ALL OF THOUGHT. It's therefore extremely difficult to decide up front which parts to exclude and include. You see this difficulty throughout the history of attempts to develop a notation for something like logic.
- This is why it shouldn't be surprising in retrospect to see how long it took for formal logic to get started as a field. Logic was an extremely late comer to mathematics, notwithstanding Aristotle's writing on logic, or semi-formal systems like Euclid which involved some embedded reasoning about a specific content domain.
- Quite a few well known mathematicians tried and failed to develop logic.

---

Intersperse with the images below:


- Leibniz's "Something like primes" idea where he tries to represent atomic concepts by prime numbers, composite concepts by composite numbers, and universal quantification by divisibility.
- Leibniz then goes on to use Cartesian notation to invent something vaguely like Boolean algebra with different notation.
- These attempts look like the behavior of a distinguished professor suggesting ideas to one of their grad students, hoping the grad student's youthful energy and need for publications will drive them to explore the ideas technically. The only problem was he didn't have anyone like that to talk to. Include his comments about "They have given it no more attention than if I had related a dream."
- The "ALU" point needs to be made much more clearly, early on.
- In Lambert's notation we see clearly the seeds of: constants, variables, types, universal and (possibly?) existential quantification, called universality and particularity. This very clearly mirrors the definition of modern formal languages as found in (for example) Mendelson or Kleene.
- Lambert's notation also contains the seeds of ideas like set theoretic complement.
- Lambert's > and < are a bit like universal and existential quantifiers, but he also introduces mA to mean "some A" and nA to mean (I think) "all A" and the _divides by the quantifiers!_ The richness of ideas you encounter when you see mathematicians doing proper premathematics is incredible, and often has a flavor a lot like programming, since definitions are the beginning of our implementations and we deal with the need to create our own definitions or compare the value of two definitions as developers much more often than mathematicians do.
- Lambert's "Fire is to Heat as Cause is to Effect" is an early example of embedding algebra. Connect this to the nu school.
- Quadrangles lol.
- Holland's objection to Lambert's notation makes a great point: A good notation should support the implicit affordances suggested by its structure. If you have a thing that looks like a fraction, you should expect users to assume that they can clear terms from the denominator by something like multiplication. If they can't, the fraction notation is failing to support its Implicit Affordances. Flesh this out. This needs to be a principle.
- In Castillion, we see "genus" and "species" concepts that show seeds of the concept of types and values.
- Gergonne is the first use of the backwards C notation for "is contained in."
- In Bolyai we see something like equality vs isomorphism, and also subset and superset. A(=)B as distinct from his "equal with respect to content" is unclear, but having three ideas here instead of two almost suggests that we have a distinction that's more like "is" vs `__eq__` in python, plus an additional concept of isomorphism.
- Bentham's notation covers equality of wholes or parts.
- DeMorgan uses parentheses, dot, colon, and juxtaposition to stand for various boolean algebra style relations.
- DeMorgan uses CASE for negation, a behavior we also see mirrored in modern regular expressions (though obviously not by direct inheritance of the idea.)
- DeMorgan also uses inverse notation for the converse of a statement.
- DeMorgan great quote: "First, logic is the only science which has made no progress since the revival of letters; Second, logic is the only science that has produced no growth of symbols."
- At this point we're in the mid 1800s, and we arrive at Boole, when things start to look more modern, though still very different in notation.
- Boole is more systematic than anyone before him. He uses the + - \* and / of ordinary arithmetic but gives them new meanings.
- Boole's choice of words makes it very clear that he's attempting to formalize thought itself, not some particular content domain.
- He shows that if we make the analogy of "or" with plus and "and" with times, then the distributive laws of algebra hold for concepts. Just noticing this seemingly trivial thing is a big step in the history of logic!
- The simple example of z(x+y) = zx + zy (where x is men, y is women, and z is European) is HUGE in that it shows the analogy of plus and times with "or" and "and" extends in at least some cases across linguistic categories! The z here is an adjective while the x and y are nouns, and the equality goes through just fine. In a sense that's obvious, because "European" here is just the noun phrase "European person," but at first glance it's a huge step toward the goal of formalizing the laws of thought.
- He then says that double application of adjectives in his system is the same as single application, which seems to be the thing that leads to the idea that the variables in the system should only take the values 0 and 1, aka "Booleans."
- "The equation x(1-x)=0 represents the principle of contradiction."
- AWESOME quote: MacFarlane 1879: The reason why Formal Logic has for so long been unable to cope with the subtlety of nature is that too much attention has been given to _pictorial notations._ Arithmetic could never be developed by means of the Roman system of notations; and Formal Logic cannot be developed so long as Barbara is represented by (holy shit insert picture wtf)... We cannot manipulate data so crudely expressed; because the nature of the symbols has not been investigated, and laws of manipulation derived from their general properties."
- Peirce has a totally wacky notation for e and pi, and ends up developing a "Logic of Relatives." 
- Peirce: Absolute terms are in Roman font, Relative terms are in Italic, and Conjugate terms are in a type face called Madisonian (seeing a spiritual ancestor of APL and K here.)
- Bertrand Russell said of Peirce "he was one of the most original minds of the later nineteenth century and certainly the greatest American thinker ever."
- "The contributions of C. S. Peirce to symbolic logic are more numerous and varied than those of any other writer—at least in the nineteenth century." For Peirce, logic also encompassed much of what is now called epistemology and the philosophy of science. He saw logic as the formal branch of semiotics or study of signs, of which he is a founder, which foreshadowed the debate among logical positivists and proponents of philosophy of language that dominated 20th-century Western philosophy. Peirce's study of signs also included a tripartite theory of predication. -Wikipedia
- Peirce: Additionally, he defined the concept of abductive reasoning, as well as rigorously formulating mathematical induction and deductive reasoning. He was one of the founders of statistics. As early as 1886, he saw that logical operations could be carried out by electrical switching circuits. The same idea was used decades later to produce digital computers. -Wikipedia 
- Peirce: Include the bit from his Wikipedia page about the "negroes syllogism" that shows the confederate context he came from.
- Need the "giver of a horse to a lover of a woman" example. It's too wacky and bizarre not to include.
- MacColl (pg 295) shows the seeds of either probability or modal logic.
- Frege's symbolism is called "repulsive" and it's said that he basically influenced nobody except Bertrand Russell.
- Wonderful quote from Frege about how to convince oneself that no intuition has accidentally ended up in an argument. The original desire of mechanistic reasoning.
- Frege's notation (or the history of logic notation section in general) is a perfect way to introduce the idea of the "Anti-Gist." There would be little value in trudging through every one of these books, but skimming a "best of" or "greatest hits" that _shows the technical details_ while giving less technical commentary is a much better way to summarize an entire era, subject, or author's writing style than simple describing the same things in the form of the standard "gist" in natural language.
- Pg 298, great quote by Schröder: In symbolic logic we have elaborated an instrument and nothing for it to do.
- Show Peano using backwards c for implication ("inverse contains"), upside down semicolons, and upside down square root for power.
- By volume 5, Peano is now writing in Latin instead of French.
- The quote from Russell and Whitehead here is fantastic.
- Include the line about "Paternal Aunt is the Relative Product of Sister and Father."
- Two lines below this they mention that "Peano and Frege showed that the class whose only member is x is not identical with x." The fact that they feel the need to CITE someone on this point, let alone someone so recent, really shows how _informal_ mathematics had been for the several thousand years of its history until then.
- At the top of 311 they mention that "types" are introduced to avoid contradictions.
- On 312, below the boobs, the thousand page book on the History of Mathematical Notations says of Russel and Whitehead's Principia Mathematica that: "We don't have enough space to list all the notations in this book." (LOL)
- On page 314, in the final page of the Logic section in the book, the author mentions that no topic in mathematics comes close to logic in terms of its ability to provide a universal language, no group has a harder notation problem to solve, and no group has thought about that problem more deeply. This fact continues today into the culture of programming, where the need to maintain large codebases which actually execute (unlike mathematics in a textbook) has led to intuitions about what constitutes a good notation that go so far beyond mathematics that it's scarcely possible to compare the two. Perhaps the most illustrative example is the fact that it was Unix, not mathematics, that finally had the sense to write function composition in the right order: f | g. 


---



![[history-of-logic-notation-01.png]]


![[history-of-logic-notation-02.png]]


![[history-of-logic-notation-03.png]]


![[history-of-logic-notation-04.png]]


![[history-of-logic-notation-05.png]]


![[history-of-logic-notation-06.png]]


![[history-of-logic-notation-07.png]]


![[history-of-logic-notation-08.png]]


![[history-of-logic-notation-09.png]]


![[history-of-logic-notation-10.png]]


![[history-of-logic-notation-11.png]]


![[history-of-logic-notation-12.png]]


![[history-of-logic-notation-13.png]]


![[history-of-logic-notation-14.png]]


![[history-of-logic-notation-15.png]]


![[history-of-logic-notation-16.png]]


![[history-of-logic-notation-17.png]]


![[history-of-logic-notation-18.png]]


![[history-of-logic-notation-19.png]]


![[history-of-logic-notation-20.png]]


![[history-of-logic-notation-21.png]]


![[history-of-logic-notation-22.png]]


![[history-of-logic-notation-23.png]]


![[history-of-logic-notation-24.png]]


![[history-of-logic-notation-25.png]]


![[history-of-logic-notation-26.png]]


![[history-of-logic-notation-27.png]]


![[history-of-logic-notation-28.png]]


![[history-of-logic-notation-29.png]]


![[history-of-logic-notation-30.png]]


![[history-of-logic-notation-31.png]]


![[history-of-logic-notation-32.png]]


![[history-of-logic-notation-33.png]]


![[history-of-logic-notation-34.png]]


![[history-of-logic-notation-35.png]]


![[history-of-logic-notation-36.png]]


![[history-of-logic-notation-37.png]]


![[history-of-logic-notation-38.png]]