## Numbers


(Later, when trying to define the natural numbers)

1: Why not this?

succ := λn. λf. f n

0 says I dunno, let's see how it works:
succ 2 = (λn. λf. f n)(λf. λx. f (f x))
       = λf. f (λf. λx. f (f x))
       oops I mean
       = λf. f (λg. λx. g (g x))

1: Ok that looks weird, I dunno how to think about what's going on here.

0: Let's start over. You're trying to define something like this right?

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

0: What's +1
1: Just wrap another f around it.
0: Around the outside?
1: No, around the inside.
0: How do we do that if we only have 3 system calls?

---

Lambda Calculus System Calls, since 1 insists.

There's only one type, but we're gonna pull an Alonzo Church and give the one type 3 different names below, depending on how we're thinking about it. It's really all the same type though. Everything's Alonzo Church. I mean functions.

1: mkvar: takes a string, makes a var
2: mkfun: takes a var x and an expr e, makes λ x: e
3: rmvar: takes a fun f and an expr e


succ := λn. λf. λx. f (n f x)

---

1: I don't think number having free variables inside them is any weirder than numbers having parameters that you can pass stuff into.
