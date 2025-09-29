## Church vs Choice
### Or: Church's Thesis (not that one)
### Or: Constructive Criticism
### Or: The C in ZFC
### Or: ZFC w/o the C
### Or: Church's two cents
### Or: Ȼurȼ's 2Ȼ
### Or: AC on AC

0: Yep. That's the C in ZFC. It's part of standard foundations. The machine code of mathematics. So Church writes his PhD thesis being like "Maybe we can delete this code guys, it's kinda sketchy."

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

1: That doesn't help.

0: I mean "three" is the idea "turn the crank three times."

1: The only crank I see around here is you.

0: Ok what's "three" to you?

1: What's three?

0: Yes, explain the concept to me.

1: Three is, well, thr---

0: You can't say "three" in the definition.

1: Ok, three is any time there are this many of something:

$$\circ \circ \circ$$

0: Does it matter what sort of things they are?

1: No. It's three if there's that many of anything.

0: Ok, what if you want to encode "three" in a language that only has verbs.

1: What do you mean?

0: Like Church's lambda calculus. Everything is functions. How do you encode three?

1: Put three functions next to each other?

0: How do you put them "next to" each other? We don't have lists or tuples yet.

1: Oh right.

0: Or strings, so string concatenation won't work either.

1: So what do we do?

0: Well, what do we have?

1: Functions?

0: Right.

1: What can we do with functions?

0: Let's go see what Church says.

![[church-19.png]]

1: What does this say?

0: It just says "We can plug stuff into functions and vice versa."

1: What's vice versa? Unplug stuff out of functions?

0: Exactly.

1: I'm not sure what I meant by that. What did you mean?

0: What's the opposite of turning `λx: x²` into `3²`?

1: Turning `3²` into `λ3: 3²` for any value of `3`?

0: Exactly.

1: I'm not sure what I meant by that. What did you mean?

0: I mean the 3 becomes a variable there.

1: I don't see Church doing that anywhere in this picture.

0: But that's the idea. He's just saying you can plug stuff into functions, and you can unplug things out of expressions to make functions. Nothing that any programmer hasn't done a thousand times. This isn't a deep thought. It just turns out to be deep as a non-thought.

1: Do you _have_ to talk like this? 

0: Like what?

1: What do you mean it turns out to be deep as a "non-thought"?

0: Well Church himself didn't actually think this was enough to capture ALL of computation! 

1: He didn't?

0: Hell no! You'd have to be insane to think that this was ALL of computation the first time you see it. I mean Church _came up_ with this idea and even HE didn't think that. 

1: How do you know?

0: From Steve.

1: Who's Steve?