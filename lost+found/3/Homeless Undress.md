

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