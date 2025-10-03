TODO: Find a place for these. They got ophaned during refactors.


---

## Kleene as the first programmer



---

## Church early logic work and the inconsistency

0: So Church starts in standard foundations. He's like "Wow this sucks." So then fast forward, Church goes to work on foundations. Real foundations. Stuff that feels a lot more like programming.

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

0: One of his students found the bug.

1: Was it Kleene?

0: Yep.

1: It's always Kleene.

0: There was another guy named Rosser who helped with this one, but yeah, Kleene's everywhere.

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

1: No numbers?

0: No numbers.

1: No booleans?

0: No booleans.

1: How can you do anything?

0: Well numbers and booleans aren't built in to the language, but they're still there. We just have to implement them from lambdas.

---
