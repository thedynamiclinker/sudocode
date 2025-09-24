
- NOTE
- This is a very bare bones skeleton of what eventually needs to go here.
- This file is closer to a set of notes than it is to a rough draft.
- If you're not one of the Authors of this book, ignore this file.

---
## Naming Things

0: Once upon a time, there was a guy named Sam.

1: Ooh I love story time.

0: Sam had an unusual family tree.

As a child, during that earliest stage of life when we're looking around the world for the first time and learning what things are called, Sam learned the following:

1. Your Name: Sam
2. Your Father: Alonzo Church
3. Your Brother: Alonzo Church
4. Your Grandfather: Alonzo Church

1: That's a lot of Alonzo Church.

0: For real. And Sam wasn't Alonzo Church. He was the only one who wasn't.

1: Must be rough to get excluded from being Alonzo Church when everyone you know gets to be that.

0: Exactly. So when it came time for Sam to have a son, he pulled a fast one on his brother -- the first born -- and added an item of his own to own the family's family tree. So now, thanks to Sam, the family tree looked like this.

1. Your Name: Sam
2. Your Father: Alonzo Church
3. Your Brother: Alonzo Church
4. Your Grandfather: Alonzo Church
5. Your Son: Alonzo Church

1: Damn Sam. That's cold.

0: "Take that, Alonzo Church," I imagine him saying to his brother Alonzo Church, when he named his son Alonzo Church.

1: Did he actually say that?

0: No idea. But eventually Sam's son would have a son of his own. And he called---

1: I wonder what he's gonna call it.

0: Drumroll.

1. Your Name: Sam
2. Your Father: Alonzo Church
3. Your Brother: Alonzo Church
4. Your Grandfather: Alonzo Church
5. Your Son: Alonzo Church
6. Your Grandson: Alonzo Church

1: Why are we talking about this?

0: Because trinities are known to be full of mysteries. And Alonzo Church is the first member of our trinity.

1: All five Alonzo Churches are members of the trinity?

0: No. Just one.

1: Which one?

0: Sam's son. The one who wasn't supposed to be Alonzo Church.

1: I'm glad it was that one. He seemed like the underdog.

0: Alonzo Church would go on to do a lot of things, but he's most well known for one thing.

1: What one thing?

0: For inventing the first programming language.

1: Woah seriously?

0: Before computers. Before the field even had an agreed upon definition of "computation."

1: What did it run on?

0: Paper.

1: Woah.

0: It was a strange programming language with only one type.

1: Only one type?

0: Only one type. In terms of built-in types, the language has no numbers.

1: No numbers?!

0: No booleans.

1: No booleans?!?!

0: No `if` or `for` or `while`.

1: This language sounds insane.

0: There's only one built-in type.

1: Is it Alonzo Church?

0: Nope. But Alonzo Church had a lot of experience with systems where everything is one type.

1: Like his family?

0: Yep. So when he grew up and went into the foundations of mathematics, and even more deep into the foundations of logic itself, he came up with a system where everything is functions.

1: Numbers are functions?!

0: Numbers are functions.

1: Booleans are functions?!?!

0: Booleans are functions.

1: Such an Alonzo Church thing to do.

0: It's not as crazy as it sounds. It's actually an incredibly powerful idea. He just didn't realize that at the time.

1: HE didn't realize that?

0: Nope. No one did.

1: Can I have some more details?

0: Of course. Let's go take a tour.

## The Collected Works of Alonzo Church

![[church-01.png]]

1: Woah you weren't just making that up?

0: Of course not. I would never lie to you.

![[church-03.png|400]]

1: Hey there's another one!

0: Told ya. They're all over the place.

![[church-02.png]]

1: Damn look at that handsome guy.

0: For real. Could have gone into Hollywood.

1: Why didn't he?

0: Well he's a foundational person. So naturally, he went into foundations.

![[church-04.png]]

0: Did his dissertation on the Axiom of choice.

1: What's that?

0: Well remember, by this time, it's been about 50 years since Cantor, and almost 30 years since 1900 when Hilbert announced his list of problems. So there's been a reasonable amount of work on the foundations of mathematics since then.

1: Why aren't we including those people in "The foundational people"?

0: Good point. Some of them probably deserve to be included too. But every story has to start somewhere, and for a bible on the history of computing, Church is a pretty good place to start.

1: What was going on in the 30 years before this?

0: Well there had been some work on axiomatic set theory. Mostly on a system called ZFC, or Zermelo Fraenkel (with the Axiom of) Choice. That system is still considered the "official" foundations of mathematics by mathematicians today, but it's never really been _used_ as foundations in any real sense.

1: What do you mean "used as foundations."

0: I mean nobody uses it.

1: What?!

0: Or almost nobody. They usually just talk about it or assert that ZFC proves such-and-such. It's extremely rare to see mathematicians actually working _within_ ZFC as a formal system.

1: That doesn't seem so bad. I mean we programmers don't really write in machine code, like ever. But it's sort of the "foundations" of any language that compiles to it, in a sense.

0: No no, I mean even books about ZFC don't work within ZFC.

1: WHAT?!

0: Here I'll show you.

## Standard "Foundations"

![[zfc-hirst-01.jpg]]

1: "These hell torments"?

0: Yeah that's axiomatic set theory.

1: What's this book about?

0: Axiomatic set theory.

1: What?!

0: That's the point. No one within mathematics really "likes" ZFC. Even set theorists who chose axiomatic set theory as their favorite area to focus on.  Now to be fair, that book isn't entirely about ZFC. But a third of it is devoted to set theory and "standard foundations," and the guy who wrote this part is a super competent logician. Intensely smart guy named Jeff Hirst. Not intending to single out the author. This is just sort of how ZFC is viewed. That "paradise" is pretty clearly the "paradise Cantor created" that David Hilbert's always quoted talking about. That's informal set theory, the kind that uses standard mathematical reasoning and eventually leads to paradoxes. And "these Hell torments" are axiomatic set theory.

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

0: Church's best student.

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

0: Exactly. They're the first. And⁰ Kleene is the glue. Like this.

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

0: Yep. That's the C in ZFC. It's part of standard foundations. The machine code of mathematics. So Church writes his PhD dissertation being like "Maybe we can delete this code guys, it's kinda sketchy."

![[church-38.png]]

1: Ok I'm not following the mathematics but that definitely sounds sketchy.

0: So fast forward, Church goes to work on foundations. Real foundations. The kind where you actually have to construct or compute something to show it exists. Stuff that feels a lot more like programming.

1: Show me.

0: Ok so here's one of his early papers. If you read it, he's clearly bothered by "free variables" for some reason. But the sense in which he's using the term "free variables" means something a bit more like "information that we didn't include in the formal system." The bits we have to add in English after the symbols.

![[church-20.png]]

1: "Without the addition of verbal explanations." Love it!

0: That's what he's working on. Getting all the vagueness and natural language out of mathematics, at least in principle.

1: Y'know it's weird. I sort of assumed mathematicians solved that problem like... thousands of years ago.

0: Nope! Mathematics has always been a mixture of formal and informal. Church wants to see if it's possible to fully specify all the missing bits. If you read the part below closely, what he's calling "free variables" are really more like _type variables._ Notice how he starts with the sentence $a(b+c) = ab + ac$ and says the $a$, $b$, and $c$ are "free variables." Then he shows what it would mean to fix that sentence.

![[church-21.png]]


1: What's the bit with the $R(a)$s and the $\supset_{abc}$ ?

0: I think the notation is based on some old stuff Peano did. But it's not complicated.

1: Looks complicated.

0: Read it.

1: "Where $R(x)$ has the meaning '$x$ is a real number' and"... oh nevermind I feel dumb.

0: So what's Church saying here?

1: He's just saying we should add types to the variables so we know what kind of thing they are.

0: Exactly. And that tendency carried through from the 1930s to modern functional programming and why their languages tend to be strongly typed.

1: Seriously?

0: Yep. Functional programming languages are all descended from Church's first language.

1: The language where every type is Alonzo Church?

0: Functions, but yeah exactly.

1: Nice! Is that language in this paper?

0: Sort of...

1: What do you mean "sort of"?

_(Narrator: 1 flips ahead through the paper)_

![[church-collage-1.jpg]]

1: Holy F---

0: Yeah.

1: Why does it hurt my eyes?

0: Because you skipped ahead.

1: This is traumatizing. I changed my mind. I don't think I'm cut out for this "frighteningly technical" stuff after all.

0: Don't worry, a lot of that turned out to be inconsistent.

1: What?

0: Here look. About halfway through the stuff you just flipped through, Church shows up and goes "Ok guys, so, this is awkward. Um, that first formal system from a little while back was inconsistent."

![[church-27.png]]

1: Inconsistent how?

0: Like totally broken. You can prove anything. 

1: Hahahahahaha all that hell math for nothing?

0: Not for nothing! Church ends up fixing the bug by adding "types." Which after all was sort of the thing he was on about in the introduction to the first paper.

1: How do you do all that hell math and then realize the whole system is broken?

0: One of his students found the bug. But then he and the student go on to do some pretty amazing stuff together.

1: Who's the student?

0: Kleene.

1: Same guy?

0: Same guy.

![[church-37.png|400]]

1: This is even more "frighteningly technical" than the hell math from earlier.

0: Definitely. Kleene's way easier to read than this, in my opinion.

1: What's the point of all this? I mean if we're gonna be reading and writing this level of hell math there'd better be a good reason.

0: Ok well remember how the Axiom of Choice lets you prove something exists without actually, like, computing it or constructing it?

1: Yeah that seemed like cheating.

0: Ok so the point of the hell math above was that Church had gotten interested in how to define "computability." Back then they called it "effectively calculable" or "an effective procedure." But it just meant "Anything you can actually DO without cheating like how the Axiom of Choice cheats."

![[church-06.png]]

1: When are we gonna get to the programming?

0: Right now.

1: Really?

0: Really. Read this next part carefully.

![[church-15.png]]

1: Didn't he start by saying "We need to get rid of free variables" in the other paper?

0: Yeah.

1: But he just introduced free variables into his system.

0: Good catch. He'll get rid of them soon. That's what the lambda is for.

1: It would help if there was more motivation.

0: Yeah, reading Church is sort of a joy and a pain in the ass at the same time. But this funny $\{F\}(X)$ notation is just a reverse-abbreviation for $F(X)$.

1: What are the curly braces for?

0: In case you want to put the implementation of the function in there instead of just its name.

1: Implementation how?

0: That's what the lambda thing is doing. Same lambda as in modern programming languages.

1: OH, no way.

![[church-16.png]]

1: Ok I sort of get this now. So this is just lambdas? Like "lambda" lambdas?

0: Yep.

1: No numbers? No booleans?

0: Not by default. We have to implement those from lambdas.

1: How do you implement numbers using lambdas?

0: Weird idea right? Here's one implementation. They're called Church numerals.

![[church-18.png]]

1: What's going on here?

0: The number 1 is a function that takes two variables. Then it calls the first variable passing the second.

1: Excuse me?

0: The number 2 is the same idea, but it calls the first variable twice.

1: I'm so confused.

0: Here I'll show you. In python it would look like this:

![[church-numerals-in-python-1.png]]

0: Make sense yet?

1: No.

0: Wait, I should correct that. There aren't really any two argument functions in Church's system. It should be more like this.

![[church-numerals-in-python-2.png]]

1: That's worse.

0: Oh and zero would be this.

![[church-numerals-in-python-3.png]]

1: This is insane.

0: Would it make more sense if I wrote it like this?

![[church-numerals-in-python-4.png]]

1: What are `verb` and `noun`?

0: Think of it like a crank. 

---

_RESUME HERE_

---

![[church-numerals-in-python-5.png]]

1: What on earth could possible motivate a person to do something like this?

(Cover von Neumann encoding of natural numbers in ZFC and explain that it's a side effect of any system that only has one type.)

![[church-19.png]]


RAW MATERIALS FOR LATER

This just says "We can plug stuff into functions and vice versa"

What's vice versa? Unplug stuff out of functions?

Exactly.

I'm not sure what I meant by that. What did you mean?

What's the opposite of turning λx: x² into 3²?

Turning 3² into λ3: 3² for any value of 3?

Exactly.

I'm not sure what I meant by that. What did you mean?

I mean the 3 becomes a variable there.

I don't see Church doing that anywhere in this picture.

But that's the idea. He's just saying you can plug stuff into functions, and you can unplug things out of expressions to make functions. Nothing that any programmer hasn't done a thousand times. This isn't a deep thought. It just turns out to be deep as a non-thought.

Do you have to talk like this? 

Like what?

What do you mean it turns out to be deep as a "non-thought"?

We'll Church himself didn't actually think this was enough to capture ALL of computation! 

He didn't?

Hell no! You'd have to be insane to think that this was ALL of computation the first time you see it. Church came up with this idea and HE definitely didn't think that. 

How do you know?

Ok so...