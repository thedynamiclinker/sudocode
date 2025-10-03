## Church's Numbers

### Or: 0 is a two argument function
### Or: 1 is a two argument function
### Or: True is a two argument function
### Or: False is a two argument function
### Or: If is a three argument function
### Or: Plus One is a three argument function
### Or: Minus One may be impossible
### Or: What the hell is going on?
### Or: What was Church thinking?

---

TODO: By the end of this file, 1 should think lambda calculus is insane.
TODO: Just show the definitions here and don't explain them.
TODO: Do this until 1 is convinced the lambda calculus is an abomination.
TODO: Then in the next file, start over from scratch.
TODO: In the next file, by actually _using_ it, 1 finally understands lambda calculus.
TODO: Then at the end of the next file, Kleene takes us to Godel.

---

0: Ok before we cover Church's language in detail, I need to warn you. It's pretty weird.

1: Weird how?

0: It's pretty bare bones.

1: How so?

0: It doesn't have most of the things you're used to.

1: Such as?

0: No numbers.

1: No numbers?

0: No booleans.

1: No booleans!?

0: No if.

1: No if!?!?

0: I mean it has numbers and booleans. It also has if and everything else you could want. Just not at first. We have to implement those things ourselves. Starting from functions.

1: What on earth would motivate a person to make a language where numbers and booleans have to be implemented from functions?

---

TODO: Explain the von Neumann encoding from ZFC and the S(S(S...(S(0))...)) implementation in Formal Arithmetic.

---

1: How do you implement numbers using lambdas?


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

---

TODO: 6:50. Church didn't think it would be possible to implement predecessor in lambda calculus. Kleene realizing how to implement predecessor at the dentist.

TODO: 7:15.
> Steve Kleene: So there was no idea at the beginning that this was going to be all effectively calculable functions.

TODO: 7:30.
> Steve Kleene: I kept taking it as a challenge and everything I tried I could work.

TODO:
> Steve Kleene: It was an unexpected fallout that this could represent all effectively calculable functions.

TODO:
> Steve Kleene: The basic work was done between January 1932 and the next 5 or 6 months.

TODO:
> Steve Kleene: Everything I tried, every kind of function I tried to define, every kind of effective operation that I tried to parallel by lambda definability, I probably knocked off within the first 5 months.

TODO:
> Steve Kleene: For us the first concept of lambda definability was after the fact, after having formulated the notion of lambda definable functions as simply the ones for which you could find formulas in this symbolism. And discovering that everything you thought of that you wanted to prove lambda definable you could!... But it was Church, I have to give the credit to Church, I can't take it myself, he said "Y'know, don't you think maybe we've really got ALL the effectively calculable functions?"

---


goto: [[5 - Church's Language]]