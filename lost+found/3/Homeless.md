# Homeless
## Homeless: How to Undress a Number

```
1: Why not this?

succ := λn. λf. f n

0: What's the motivation?

1: I mean based on how we defined numbers, "+1" should just be "wrap another f around it."

0: I'm not sure that's what you did there.

1: How is that not what I did?

0: You're trying to define something like this right?

0 ≈ x
1 ≈ f(x)
2 ≈ f(f(x))
3 ≈ f(f(f(x)))

1: Why the squiggly equals signs?

0: I just meant "You're trying to do that, but without the f and x being free variables" right?

1: Yeah exactly.

0: So let's just toss some lambdas outside.

1: What's the point of that?

0: I dunno. It'll get rid of the free variables.

1: Ok, here:

0 := λf. λx. x
1 := λf. λx. f x
2 := λf. λx. f (f x)
3 := λf. λx. f (f (f x))
4 := λf. λx. f( f (f (f x)))

0: I'm still not sure how to define "+1".
1: Just wrap another f around it.
0: Around the outside?
1: Sure.
0: Like this?

5 := f( λf. λx. f( f (f (f x))))

1: Oh yeah, I guess that's wrong.

0: It's not too wrong though, we just need to wrap the f around the inside.

1: How do we do that if we only have 3 system calls?

0: System calls?

1: Yeah. So far it seems like we only have three.

0: What do you mean?

1: Like this:

System Calls
============
1: mkvar: takes a str, makes a var
2: mkfun: takes a var x and an expr e, makes λ x: e
3: rmvar: takes a fun f and an expr e

0: Hadn't thought of it like that. What do you mean by "str" and "var" and "expr" and "fun"?

1: Obviously, that's "string" and "variable" and "expression" and "function".

0: No no, I mean we only have functions.

1: Sure fine, I mean know there's only one type, but I figured we could just pull an Alonzo Church and give the one type 3 or 4 different names, depending on how we're thinking about it. It's really all the same type though. Everything's Alonzo Church. I mean functions.

0: Ok, as long as it's just following the laws of Alonzo Church.

1: So then how do we define "+1"?

0: Well I think your system calls idea solved it.

1: How so?

0: Here look. We tried this, but it was clearly wrong.

	5 := f( λf. λx. f( f (f (f x))))

0: So to make it right, we just need to get that f inside somehow.

1: How do we do that?

0: With your system calls! Look:

Supposing we start with, say, the number four, namely:

	4 :=  λf. λx. f( f (f (f x)))

Then we can get to five like this:

	4 = λf. λx. f( f (f (f x)))
	rmvar 4 = λx. f( f (f (f x)))
	rmvar (rmvar 4) = f( f (f (f x)))
	f(rmvar (rmvar 4)) = f( f( f (f (f x))))
	mkfun( f(rmvar (rmvar 4))) = λx. f( f( f (f (f x))))
	mkfun( mkfun( f(rmvar (rmvar 4)))) = λf. λx. f( f( f (f (f x))))

1: I don't think you used my syscalls right.

0: (Zero checks the syscall signatures) Oh, oops.

1: But I think I get your idea. Can I define some terms?

0: Always!

1: Ok so:

	undress(4) = f( f (f (f x)))

	f(undress(4)) = f( f( f (f (f x))))

	redress(f(undress(4))) = λf. λx. f( f( f (f (f x))))

And that's 5.

0: I don't think that's what redress means.

1: What?

0: Here look.

	re·dress /rəˈdres/
	1. (verb) To remedy or set right (an undesirable or unfair situation).
	2. (noun) A remedy or compensation for a wrong or grievance.

1: Yeah exactly. That's what I meant.

0: How is that what you meant?

1: Well we didn't ask permission to undress these numbers, so naturally thr redress step is how we make amends.

0: You're the weirdest student I've ever ha---

1: Whatever. Look, we did it!

	succ(n) = redress(f(undress(n)))

0: And now we can remedy or set right the crime we just committed against terminology by rewriting it like this:

	succ := λn. λf. λx. f (n f x)

1: How is that the same?

0: It's clearly the same.

- The succ function takes a number n.
  That's the λn bit.

- Then it returns a number,
  which is a two argument function.
  That's the λf. λx. bit.

- That accounts for the function signature.
  
- Now the internals of the function are just:
  f (n f x)

- And f (n f x) is the same as f(undress(n))

1: How is f (n f x) the same as f(undress(n))?

0: I'm just plugging in values that happen to have the same names as the function's parameters. That's how we undress any number n. Just feed it an unspecified thing named f, and another unspecified thing named x.

1: Got it! What about the redress step?

0: I already took care of that in the lambdas. I just reasoned in reverse, compared to what you did. The redress is the bit where I explained where the

	λn. λf. λx.

bits come from.

1: Great! Now how do we add numbers?

0: We just did that.

1: No no, I mean how do we add numbers other than 1?
```

## Homeless: A bit more work towards Y premathematics

```
ω f = f(f(f(f(...)))) = f(ω f)

ω = λf. f(ω f)

But we can't put the ω on both sides.

Back to basics

ω = λf. stuff

What's stuff?

Well, two possibilities:
1. stuff is: λx. (?)
2. stuff is: A B
   in which case A should have
   a lambda, so
   stuff is (λx. ?) B

So

1. ω = λf λx. A
   Subquestion: What's A?
   
2. ω = λf. A B
   ω = λf. (λx. A) B
   Subquestion: What are A and B?

In case 2:
- Suppose B has no λ in it.
- Then ω = λf. A[x := B]
- So A has one fewer λ than we thought
- So either case 2 is impossible,
  or else B has a λ in it.

ω = λf. (λx. A) (λy. B)

So then

ω = λf. A[x := (λy. B)]

But then

ω f = A[x := (λy. B)]

- So this is either a contradiction,
  or else:

ω f = f(f(f(f(...)))) = f(ω f)

implies that

A[x := (λy. B)] = f(A[x := (λy. B)])

If that's the case, then

ω = λf. (λx. A) (λy. B)

can be written

ω = λf. (λx. f(...)) (λy. B)

ω = λf. (λx. f(ω)) (λy. B)

ω = λf. (λx. f(
               λf. (λx. f(...))
                   (λy. B)
              )
        )
         (λy. B)

What if 

ω = λf. (λx. f(x)) (λx. f(x))

ω = λf. f(λx. f(x))

ω = λf. f(f)

That's only twice.

What if 

ω = λf. (λx. f(x(f))) (λx. f(x(f)))

Then

ω = λf. f( (λx. f(x(f))) (f))

or

ω = λf. f(f(f(f))))

That's only 4 times.

What about

ω = (λf. f f) (λf. f f)

So

ω = (λf. f f) (λf. f f)
  = (λf. f f) (λf. f f)
  = (λf. f f) (λf. f f)
  = (λf. f f) (λf. f f)
  = (λf. f f) (λf. f f)
  
Um...


What about

ω = λf. (λx. f(x x)) (λx. f(x x))

That's 

ω = λf.   (λx. f(x x)) (λx. f(x x))
  = λf. f((λx. f(x x)) (λx. f(x x)))
  = λf. f(naked ω)

But naked ω is ω f, so

ω = λf. f(ω f)
  
Or

ω f = f(ω f)

```

## Homeless: Y combinator

1: Recursion?

0:  The Y combinator:

```
Y := λf. (λx. f (x x)) (λx. f (x x))

Y g :=    (λx. g (x x)) (λx. g (x x))
    := g ((λx. g (x x)) (λx. g (x x)))   -- How did we get this again? Nvm.
	:= g (Y g)

Z = g (Z)
Z = g (g (Z))
Z = g( g (g (Z)))
Z = g( g( g (g (Z))))
...
Z = g( g( g (g (...))))

So

Y = λf. f( f( f (f (...))))

Y f = f( f( f (f (...))))
Y f = f(Y f)
Y = λf. f(Y f)
Y = λf. ((λx. f x) (Y f))
Y = λf. ((λx. f x) f(Y f))
Y = λf. ((λx. f x) ((λx. f x) (Y f)))  -- Ok we need to get rid of this Y somehow...

Y = λf (λx. f(x) f(Y f))

```

Show the key equation `Y f → f (Y f)`:

```
Y f
= (λf. (λx. f (x x)) (λx. f (x x))) f
→ (λx. f (x x)) (λx. f (x x))
→ f ( (λx. f (x x)) (λx. f (x x)) )
= f (Y f)
```

## Homeless: (3,4): Church's Numbers

### Or: 0 is a two argument function
### Or: 1 is a two argument function
### Or: Booleans are two argument functions
### Or: If is a three argument function
### Or: Plus One is a three argument function
### Or: Minus One may be impossible
### Or: What was Church thinking?

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

