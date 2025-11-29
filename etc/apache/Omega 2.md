## The Omegas

0: We were covering this:

![[friedman-1997-the-formalization-of-mathematics-13.png]]

1: We're still on this?

0: It's ok, let's be quick. So ZFC has "not", "implies", "and", "or"

1: I'm now traumatized by "or".

0: It's also got "If and only if" which is just two "implies" in opposite directions with an "and" between them. Then it's got variables. It's for "For all" and "There exists."

1: With one bad path each.

0: It's got a set membership symbol $\in$ so we can say $this \in that$ to mean "this" is an element of "that", and it's got an equals sign that we use to mean "these two sets have the same elements."

1: That's it?

0: Well that's the language. On top of that there's ZFC.

1: I thought this was ZFC.

0: That's the language of ZFC. The theory of ZFC is all that, plus ten commandments.

![[friedman-1997-the-formalization-of-mathematics-14.png]]


![[friedman-1997-the-formalization-of-mathematics-15.png]]

1: That was nine.

0: Hard problems of computing. Off by one errors. There's usually ten.

1: What does it mean up there where it says "infinitely many axioms"?

0: Those are sentences that can't actually be expressed in the language of ZFC.

1: What? Why not?

0: See how Axiom 3 and Axiom 7 say "For any formula in our language"?

1: Yeah.

0: Well the language of ZFC can't quantify over sentences in ZFC.

1: What does that mean?

0: It can only say "For all x" and "There exists x" when x is a set. It can't say "For all sentences" or "There exists a sentence."

1: Ok. But Axioms 3 and 7 aren't talking about sentences, they're talking about formulas. What's a formula?

0: A sentence.

1: WHAT?!

0: Right. ZFC can't say "For all sentences." But the mathematicians want to say that anyway. And they don't want to change the language to give it quantifiers that range over sentences. So instead they just sort of cheat and squeeze these two axioms into a language that can't express them by saying "We'll add infinitely many axioms for Axiom 3, one for each possible formula in the language." Then for Axiom 7 they do the same thing and add another infinity of axioms again.

1: Math is completely unhinged.

0: In this case it's not technically that bad. It's not too different from if they had implemented a parser that could parse valid formulas of ZFC. Then for any of the infinitely many axioms above, they could have the parser tell you whether or not a given sentence was an axiom that was talking about some specific formula using the axiom schema of 3 or 7.

1: Did they implement that parser?

0: No. But they imagine they could.

1: This makes me dizzy.

0: Well you asked to see the details of ZFC.

1: Nevermind, let's go back and talk about something else.

0: Ok so, the mathematicians' experience with ZFC is pretty similar to yours. They don't really like it. They don't really like talking about it. And they REALLY don't like working within it.

1: So why do they call it foundations?

0: Because they don't really like talking about foundations either.

1: Rock and a hard place.

0: So because of that, ZFC sort of ended up as an impotent figurehead type of ruler.

1: Impotent figure what?

0: Like a king with no power. Everyone points to ZFC and says "That's the foundations," but no one likes it, no one uses it, and it's basically just been sitting there for a century plus with a big crown on that says "I'm the foundations of mathematics and mathematics is the foundation of everything." Like this guy from the memes.

![[theoden-is-zfc.jpg]]

1: Damn, that sucks.

0: Fortunately that's been changing recently though.

1: How so?

0: We'll get there eventually. For now, pop the stack back to the Hirst book. Because mathematicians don't like ZFC, they tend to talk about it rather than working within it. Like this:

![[zfc-hirst-04.jpg]]

0: Feels like normal math right?

1: I guess? Not really sure.

0: That's the point. It's mostly words. Here's another example.

![[zfc-hirst-02.jpg]]

1: "We could"?

0: Yep. That's the standard mathematical approach to ZFC. They're not actually working inside the formal system. They're just sort of writing pseudo-code and English that talks about what the proof would be like if we actually did it. They call it "foundations," but they basically always keep it at arms length. Even the logicians and set theorists. There are a few solid exceptions though. For example:

![[zfc-hirst-03.jpg]]

0: Mendelson and Kleene. They do the formal stuff.

1: Who are they?

0: Mendelson is the book we saw earlier in /opt/art.

1: No way! The bit with the "hell code"?

0: Exactly. That's Mendelson's _Introduction to Mathematical Logic_. It's a pretty approachable introduction to the actually formal side of foundations.

1: The second book sounds fun!

0: The Kleene one?

1: Yeah! Is that the same Kleene?

0: Same guy! Why does it sound fun?

1:I mean if that "hell code" book was the easy one, I can't imagine what the one for "readers with a frighteningly technical bent" is like. Makes me want to read it.

![[zfc-hirst-06.jpg]]

0: Yeah Kleene's book is pretty great.

1: What's it actually called?

0: This:

![[zfc-hirst-15.jpg]]

1: What's so frightening about it?

0: It's code.

1: What's so frightening about code?

0: I mean, the book is from 1952, based on work from the 1930s and 1940s. So there's no "computer code" in there in the usual sense.

1: So how's it code?

0: Because Kleene doesn't skip steps or hand-wave or say "it can be shown." He works inside the formal system. He adds a ton of documentation -- English explanations of what's happening -- but the way he behaves as the author of that book is exactly how you'd behave if you were a programmer.

1: I am a programme---

0: I know. But that's an extremely unusual way to behave in a math book, when you're the author. I mean he behaves as if everything he claims actually has to be implemented. He doesn't write as if he's trying to convince a human mind where you can just handwave or say "obviously" or "exercise for the reader." He writes as if he's trying to convince a machine, and then documenting heavily so humans can read the code too. Kleene was pretty clearly the first programmer.

1: Wait, I thought the first programmer was Church and Gödel and Turing?

0: Exactly. They're the first. And Kleene is the glue. Like this.

$$3 = \{ 0, 1, 2 \}$$

1: Do you try to be confusing on purpose?

0: What's confusing about that?

1: Everything?

0: Ok so, in Cantor's set theory, the number N is defined to be the set of all the natural numbers less than it. So 3 is the set containing 0, 1, and 2.

1: That's weird. But ok.

0: And Kleene is the curly braces and commas. The bits that hold it all together and make the set be one thing. He's the glue.

1: That feels like a stretch.

0: It's not.

1: Anyways, can we read some of that book?

0: Not yet. We'll get to the bible eventually.

1: What? I didn't ask for more bible, I asked for the frighteningly technical book!

![[zfc-hirst-14.jpg]]

0: Oh sorry forgot to explain. The "frighteningly technical" book is also called Kleene's Blue Bible.

1: Oh ok. I'm down for that kind of bible. Can we read some now?

0: Nah, we're still at Church.

1: _(Looks back through the conversation.)_ I thought that book was by Jeff Hirst.

0: Right, this one is. But this situation has been going on since Church.

1: So?

0: So we're still talking about Church.

1: We haven't talked about Church in a while.

0: This is all about Church.

1: Are you sure this wasn't just a long digression?

0: I never digress.

1: I don't believe you.

0: I promise. We just need a reverse begat list to tie it back to Church.

1: What's a reverse begat list?

goto: [[lost+found/3/3]]
