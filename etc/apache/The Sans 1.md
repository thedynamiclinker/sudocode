## Constructive Criticism
### Or: OR

0: Exactly. But it turns out there are some questions I have, questions that are related to Church's thesis (the PhD one) and also to the axiom of choice. But my questions are more basic than that. Just some simple questions about "or." So since you're sure you understand "or," then maybe you can teach me some things about which I'm not sure.

1: Is this a game?

0: No, I'm serious.

1: I don't believe you.

0: Ok so, for any sentence $A$, is the following always true?

$$A \lor \lnot A$$

1: Is this a trick?

0: Not a trick.

1: And these are booleans?

0: Let's call them "propositions."

1: Is that a fancy word for boolean?

0: Sort of. A proposition is a bit more like a pre-boolean.

1: Wtf is a "pre-boolean"?

0: I mean $A$ is a sentence that can either be true or false, and it can't be half-true and half-false.

1: How is that not a boolean?

0: Well, suppose we don't know its value.

1: So we know $A$ is of type $Bool$, but we don't know its value?

0: Basically.

1: Zero that's a boolean, don't be stupid.

0: I'm trying as hard as I can not to be stupid, but I'm still not convinced it's a boolean.

1: You said this wasn't a game.

0: It's not!

1: Then what's your hang-up?

0: Well look, we're programmers, and if we were programming in a typical language, I'd have zero hang-ups and no worries.

1: So how is this different?

0: This is mathematics.

1: Fair. I mean I'm as convinced as ever that mathematics is a bit wacky. But how is OR tripping you up exactly?

0: Not OR per se. Just this:

$$A \lor \lnot A$$

1: So you're fine with that sentence in programming?

0: Of course.

1: How is that sentence any different in math?

0: Well, I have a strange feeling that it requires... how can I put this... omniscience.

1: Omniscience?!

0: Omniscience. And I'm not god, so I'm not sure I can handle it.

1: Is this just an excuse to bring up bible stuff again?

0: Not at all.

1: Then explain why you're being weird.

0: Suppose I hand you a sequence $a_n$ of natural numbers. For simplicity, let's say they're all $0$ and $1$.

1: Define your terms so I know this isn't a trick.

0: I just mean a function from $\mathbb{N}$ to $\{0, 1\}$.

1: I get the idea but I need more details because I'm assuming this is a trick.

0: Ok, good point. Math terminology is nowhere near precise enough to explain what information you actually have and don't have. Let's be precise. Imagine it's a python generator.

1: Ok.

0: And further, imagine I don't give you the source code to the generator.

1: What do I get?

0: All I give you is the ability to call `next()` on the generator.

1: Ok, how's this related to the thing where you're pretending not to understand "OR"?

0: Well, I've been thinking about what happens when $A$ is a sentence like this:

> $A$ = The python generator I just handed you always yields $0$, and will never yield $1$, no matter how many times you call `next()`.

or equivalently

> $A$  =  The sequence $a_n$ is always zero.

or equivalently

$$A \; \equiv \; \forall n \in \mathbb{N}, \; a_n = 0$$
1: What's your problem with that sentence?

0: Nothing. My problem is with this sentence:

$$A \lor \lnot A$$
1: You have a problem with the sentence "A or not A"?

0: Not for all sentences. Just for sentences like that one.

1: I'm still not following.

0: Ok, suppose you think $A$ is false, and I think it's true. How would you convince me you're right?

1: $A$ being false means what again?

0: $A$ being false means that eventually the generator will spit out a $1$.

1: Well obviously in that case I'd just keep calling `next()` until I got a $1$. Then I'd show you the $1$ and that would prove I was right.

0: Good point. What about the other case? Like what if our beliefs were swapped, but you were still right?

1: You mean what if I think $A$ is true, and you think $A$ is false?

0: Right.

1: And $A$ is actually true, so I'm right?

0: Right. How would you convince me then?

1: _(Looking back over the definitions.)_ Ok so if $A$ is true then the sequence is always zero. Or the generator keeps yielding zero whenever I call `next()`.

0: But I don't believe that.

1: Right. And I do.

0: I need to be convinced.

1: And I don't. But I'm right.

0: Right.

1: So what's the question?

0: How would you convince me?

1: I don't know.

0: Well I've given you an awful lot to work with.

1: Have you?

0: Absolutely? I've been more than generous here. We've assumed that you're _actually_ correct and I'm incorrect. We've assumed that $A$ will always return $0$ no matter how many times we call `next()` to see what the next number in the sequence is. And we've assumed you believe that. And we've assumed I don't believe that. I'm just some ignoramus who has trouble with "OR", at least in this particular manifestation. Surely that's more than enough for a proof that I'm wrong.

1: I'm having trouble, can you give me a hint?

0: No.

1: Zerooo.

0: I'm not in a position to offer hints. I'm the confused one here. Plus I'm also incorrect. And worst of all, I'm finite. That's what I was saying before about $A \lor \lnot A$.

1: What's what you were saying before about $A \lor \lnot A$?

0: Omniscience. I'm not god, so I'm not sure I can handle it. And I'm not sure you can handle it either.

1: What does not being god have to do with $A \lor \lnot A$?

0: Well not in every case, but at least in the case of our sequence above, I'm not sure how you'll ever convince me.

1: Are you being dense on purpose?

0: No, I'm being a mathematician. But that's a fair point. If I was being a programmer, or a statistician, or a normal human being, I'd definitely be more and more convinced as we saw more zeros and gathered more evidence. But if I'm being a mathematician, then I would object and say no amount of evidence counts as a proof.

1: Ok I'm not sure what just happened, but I feel like it's more about the sequence being infinite than it is about "OR".

0: In mathematics, those are the same thing.

1: HOW ARE THOSE THE SAME THING?

0: Well if you tell me you believe the statement:

$$A \lor \lnot A$$

is always true, for any well-formed mathematical sentence $A$, then all I'll say is that a very large fraction of all mathematical sentences that $A$ might stand for, when unwrapped, look something like $\forall x P(x)$.

1: So?

0: And if that $\forall$ is quantifying over an infinite set, which (again) is the case for a very large fraction of all mathematical sentences, then I'm just saying I'm not sure how I feel about the claim that

$$A \lor \lnot A$$
1: Ok well even if convincing a skeptic works different in the two cases above, the sentence's possible truth values are still just booleans right?

0: I'd call them propositions.

1: What was the point of calling them propositions again?

0: I just felt that they're a bit more like pre-booleans.

1: I don't understand the distinction.

0: Well if they were booleans, then as a programmer, you should be able to write code like this:

```python
if A:
	do thing 1
else:
	do thing 0
```

1: Why can't I write code like that?

0: Well, we've assumed A is true, correct?

1: Right.

0: But you don't have the source code to the generator $a_n$.

1: I wasn't super clear on the reason for that assumption.

0: I mean you can't do some fancy static analysis or metaprogramming or introspection to determine how the code for $a_n$ works from the outside. You can only run $a_n$ and use its outputs to determine the truth value of the (pre-)boolean $A$.

1: I still think "pre-boolean" in an unnecessary term.

0: Ok, then, tell me what happens in the code block above.

1: This one?

```python
if A:
	do thing 1
else:
	do thing 0
```

0: Right.

1: Well if we call `next()` in a loop and eventually get a $1$, then we know $A$ is false, so we take the `else` branch and do thing 0.

0: Right.

1: And if we never get a $1$, then we take the `if` branch and do thing 1.

0: So you never do thing 1.

1: Why?

0: Because you never get a 1.

1: Oh Christ, I feel dumb. I see the problem now.

0: Don't. Most mathematicians agree.

1: I must be getting sick or something. Why didn't I see the problem before? Agree with what?

0: That there's absolutely no problem with the statement

$$A \lor \lnot A$$

under any circumstances.

1: There's OBVIOUSLY a problem!

0: Obviously? Just two minutes ago you were arguing there wasn't.

1: Sure but I had the wrong mental model.

0: How so?

1: I assumed that because these sentence things were boolean valued that they were... well... booleans.

0: Aren't they?

1: Yes! But not yet.

0: Yet? Is their type a function of time?

1: No! But I mean if your sentence is about an infinite set and you don't have the source code, or if you don't have any information that lets you reduce it to something simpler, or just in the general case I guess, if your sentence says "For all x" and you have to evaluate that boolean by checking all the x, then even if your sentence is true, you can't take the "true" code path.

0: Is it always a problem with "For all" type sentences.

1: I think so. The branch that worked was when a "1" existed somewhere in the sequence. If it exists we can find it, so we can eventually take that branch.

0: What about situations like this?

> Suppose A is the sentence "There exists a 1 in this sequence", or "This generator will eventually yield a 1."

1: Isn't that the first example up above? The one that didn't have problems?

0: Right, same example.

1: So what's the problem?

0: I want to write this code:

```python
if A:
	do thing 1
else:
	do thing 0
```

1: Are we assuming A is true or false?

0: Do both cases.

1: Ok if A is true, then there's a 1 in the sequence eventually, so eventually we find it, and then A turns from a pre-boolean to a boolean and we can take the first branch and do thing 1.

0: You're using the term pre-boolean now?

1: I understand the problem now.

0: Great. Then you can do case two.

1: Ok if A is false, then there doesn't exist a 1 in the sequence, so we're back in the case of all zeros, and the pre-boolean never becomes a boolean and we can never take branch two. Damn this is a serious problem. How did I not see this before?

0: Now that you get the idea, mind summarizing it for me?

1: Ok so...

- Both "For all" sentences and "There exists" sentences have a good path and a bad path.
- The good path of "For all" sentences occurs when they're false.
- The good path of "There exists" sentences occurs when they're true.
- The bad path of "For all" sentences occurs when they're true.
- The bad path of "There exists" sentences occurs when they're false.
- The good path is always executable, whether the domain is finite or infinite, no matter how much information we have about the domain being quantified over.
- The bad path _may_ be executable in certain highly structured special cases when we have enough information to infer something about the whole domain at once.
- If we have enough information that we can handle a "For all" sentence when it's true, or a "There exists" sentence when it's false, then we can use something like a "proof" to make the bad path executable.
- In all other cases, the only way to turn these propositions into booleans is to use the information we have.
- In those cases, if we only have finite means at our disposal, like checking values and iterating, then bad paths are bad, and generally will not be executable.
- In other words, whenever we can't reduce a statement about an infinite set to a finite sequence of steps, "For all" statements require omniscience to execute when they're true, and "There exists" statements require omniscience to execute when they're false.

0: _(Applause)_

1: Is that sarcastic applause?

0: No! That was fantastic.

1: I forget how we got here.

0: You said you understand "OR."

1: Jesus. I'm never gonna say I understand anything ever again.

0: Please do! You understand a lot.

1: Where were we?

goto: [[The Omegas 2]]