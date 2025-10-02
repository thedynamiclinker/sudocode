## Old Laws No One Uses
### Or: The Old Foundations
### Or: The Standard Foundations
### Or: These Hell Torments
### Or: Numbers are sets
### Or: Booleans are sets
### Or: ZFC

> _These axioms are the official doctrine - Remarkably, this is not just the official doctrine for set theory, it turns out that this is the official doctrine for mathematics! - Very few people seem to have a problem with that which I find quite remarkable._
> -NJ Wildberger


![[zfc-hirst-01.jpg]]

1: "These hell torments"?

0: Yeah that's axiomatic set theory.

1: What's this book about?

0: Axiomatic set theory.

1: What?!

0: That's the point. No one within mathematics really "likes" ZFC. Even set theorists who chose axiomatic set theory as their favorite area to focus on. Now to be fair, that book isn't entirely about ZFC. But a third of it is devoted to set theory and "standard foundations," and the guy who wrote this part is a super competent logician. Intensely smart guy named Jeff Hirst. Not intending to single out the author. This is just sort of how ZFC is viewed. That "paradise" is pretty clearly the "paradise Cantor created" that David Hilbert's always quoted talking about. That's informal set theory, the kind that uses standard mathematical reasoning and eventually leads to paradoxes. And "these Hell torments" are axiomatic set theory.

1: And this is a book _about axiomatic set theory?_

0: Yep. At least this part is. This book is extremely good at choosing quotes for section headings. A lot of the quotes in this section are about hell. Or L, which is a thing Gödel invented in the course of studying, well, axiomatic set theory.

![[zfc-hirst-07.jpg]]

1: Damn, seems like mathematicians really don't like axiomatic set theory.

0: Yeah, there are a bunch of dog whistles throughout this part about how mathematics probably needs some new foundations. Can't disagree.

![[zfc-hirst-10.jpg]]

1: Why not just come up with new axioms?

0: People have. This guy Harvey Friedman in the image below kicked off a revolution that completely changed our understanding of what mathematics is. Turns out most of mathematics is equivalent to one of five sentences. But mostly nobody noticed. At least not many mathematicians.

![[zfc-hirst-13.jpg]]

1: Most of mathematics is WHAT?!

0: Equivalent to one of five sentences.

1: HOLY F---

0: Yeah I know.

1: What sentences?

0: Not now. We'll get there eventually. We're still at Church.

1: Wait though, how did most mathematicians not notice that most of their field is one of five sentences?

0: Mathematicians mostly don't pay a lot of attention to foundations.

1: Jesus.

0: And because of that, ZFC sort of ended up as an impotent figurehead type of ruler.

1: Impotent figure what?

0: Like a king with no power. Everyone points to ZFC and says "That's the foundations," but no one likes it, no one uses it, and it's basically just been sitting there for a century plus with a big crown on that says "I'm the foundations of mathematics and mathematics is the foundation of everything." That's been changing recently though.

1: How so?

0: We'll get there eventually. For now, just notice that the following is pretty typical of how mathematicians "use" ZFC, even in books that are supposed to be "about" axiomatic set theory.

![[zfc-hirst-04.jpg]]

0: Feels like normal math right?

1: I guess? Not really sure.

0: That's the point. It's mostly words. They're not actually working inside the formal system. They're just sort of writing pseudo-code and English that talks about what the proof would be like if we actually did it. 

1: Isn't that what we're doing?

0: Exactly! Here's another example.

![[zfc-hirst-02.jpg]]

1: "We could"?

0: Yep. That's the standard mathematical approach to ZFC. They don't use it. They call it "foundations," but they basically always keep it at arms length. Even the logicians and set theorists. There are a few solid exceptions though.

![[zfc-hirst-03.jpg]]

0: Mendelson and Kleene do the formal stuff.

1: Who are they?

0: Mendelson is the book we saw earlier in /opt/art.

1: No way! The bit with the "hell code"?

0: Exactly. That's Mendelson's _Introduction to Mathematical Logic_. It's a pretty approachable introduction to the actually formal side of foundations.

1: The second book sounds fun!

0: Kleene?

1: Yeah! I mean if that "hell code" book was the easy one, I can't imagine what the one for "readers with a frighteningly technical bent" is like. Makes me want to read it. Who's Kleene?

0: Church's #1 student.

1: No way!

0: Which brings us back to Church.


![[zfc-hirst-06.jpg]]

0: We'll meet Kleene pretty soon.

![[zfc-hirst-14.jpg]]

0: And yeah, the "frighteningly technical" book is also called Kleene's Blue Bible.

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

0: It's not. The best way to explain Kleene is to get back to Church. So Church's PhD dissertation was about ZFC. Standard set theory. Specifically the C. The Axiom of Choice is a sort of "constructor" for sentences that look like $\exists x P(x)$ that doesn't require you to provide an example of an $x$ that makes it true.

1: I know what a constructor is. What's the $\exists$ thing?

0: That means "There exists." Think of the Axiom of Choice as a function that you can call in standard mathematics. That function returns a sentence that says "Something exists." And you're allowed to take that sentence that says "Something exists" and use that sentence in your proofs. It's controversial because you can call that function without passing in an example of an actual Something that makes the sentence true.

1: I'm like 50% following. Rephrase?

0: It lets you prove that something exists without requiring you to give any examples.

1: WHAT?!

