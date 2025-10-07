## Church's Language

### Or: What Church was thinking
### Or: Church's First Try
### Or: Untyped λ-calculus



---

## Partially Cooked Materials

0: Church did this.

0 := λf. λx. x
1 := λf. λx. f x
2 := λf. λx. f (f x)
3 := λf. λx. f (f (f x))
4 := λf. λx. f( f (f (f x)))
succ := λn. λf. λx. f (n f x)

1: I'm not ready to hear what Church did.

0: You're not ready for the definition?

1: No.

0: What do you mean?

1: I mean that definition makes no sense to me. Back up to the part where they derive that.

0: Derive what?

1: The definition.

0: Church doesn't do that in this paper.

1: Ok can we find a textbook that does?

0: Sure, let's go look.

(Narrator: 0 and 1 go find some other textbooks on λ calculus.)

0: This one doesn't have it either.

1: Same with this one.

0: Y'know I've actually never seen the kind of derivation you're asking for before.

1: Well what did Kleene use as a repl? 

0: He didn't have a repl.

1: How did he know if something he tried worked or not?

0: I think Church was his repl.

1: Well we can't do that! He's not here. And his paper isn't finished.

0: Don't blame Church, this is just how mathematicians write.

1: I thought he was a foundational person.

0: He is. I just mean if you publish in academic journals you have to write their way.

1: Be my repl.

0: How so?

1: I'll write stuff. You tell me if it's a syntax error or not. Then when I plug things into functions, you evaluate them.

0: Ok.

1: x

0: (Says nothing)

1: So?

0: What do you want me to say?

1: I dunno, say yes if it's ok, or error if it's an error. Is that ok?

0: yes

1: x

0: yes

1: x y

0: hmm

1: That's not very repl.

0: I'm thinking.

1: About what?

0: I don't know if that's syntactically valid.

1: I thought you knew this system.

0: I mean, you have a free variable, and then you plugged it into another free variable. They're both functions. Cuz everything's functions. But neither of them has any lambdas in it. So idk. Whether or not we decide that that's syntactically ok, either way, we can't reduce it any further. It just sort of sits there.

1: Ok, what about this.

λx. x

0: That's ok.

1: What about λx: 3

0: There's no 3 yet.

1: Oh right. How about this?

λx. y

0: That's ok.

1: You're supposed to say yes

0: Ok

1: λx. λx. x

0: error

1: Why?

0: Try plugging something into it.

1: I thought there was no 3 yet.

0: Treat it like a variable.

1: What?

0: I just mean plug something into that thing you just defined. Something that doesn't feel like a variable, so you don't get confused.

1: 

(λx. λx. x)(3)

= λ3. 3

0: You can't do lambda of three.

1: Why not?

0: 3 isn't a variable.

1: I thought you said treat it like a variable.

0: Ok nevermind. Use a.

1:

(λx. λx. x)(a)

= λa. a

0: Now plug a into this: λx. λy. x

1: 

(λx. λy. x)(a)

= λy. a

(Continue)

---

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
2 := λf. λx. f (f x)λf. λx. f (f x)
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


---

## Raw Materials

0: We have only three syntactic forms:

1. Variables: `x`, `y`, `z` ...
2. Abstractions: `λx. t` (a function of one argument)
3. Applications: `t u` (apply `t` to `u`)

Reduction rule is β-reduction: 
`(λx. t) u → t[x := u]` (substitute `u` for free `x` in `t`).

We also allow α-conversion (rename bound variables) to avoid capture.

1: Show me a single, tiny, fully explicit reduction. No skipping.

0:  Take `((λx. λy. x) a) b`

- Step 1. Leftmost application reduces first (call-by-name illustration, but the β-step is standard):

```
((λx. λy. x) a) b
→ (λy. a) b          -- β: substitute a for x in (λy. x)
→ a                  -- β: substitute b for y in a (no y in a), so it stays a
```

1: Clear. Now show me booleans without pretending I already know encodings.

0: Define:

```
true  := λt. λf. t
false := λt. λf. f
if    := λb. λt. λf. b t f
```

Check `if true T F`:

```
if true T F
= (λb. λt. λf. b t f) true T F
→ (λt. λf. true t f) T F
→ (λf. true T f) F
→ true T F
→ (λt. λf. t) T F
→ (λf. T) F
→ T
```

Every step is a β-step.

1: Numbers now. From zero. No skipping steps.

0: Church numerals:

```
0 := λf. λx. x
1 := λf. λx. f x
2 := λf. λx. f (f x)λf. λx. f (f x)
3 := λf. λx. f (f (f x))
4 := λf. λx. f( f (f (f x)))
succ := λn. λf. λx. f (n f x)

1 says why not this?
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
```

Compute `(succ 1)`:

```
succ 1
= (λn. λf. λx. f (n f x)) 1
→ λf. λx. f (1 f x)
→ λf. λx. f ((λf. λx. f x) f x)
→ λf. λx. f ((λx. f x) x)
→ λf. λx. f (f x)   -- that's 2
```

1: Addition. Explicitly. Once.

0: Define:

```
plus := λm. λn. λf. λx. m f (n f x)
```

Compute `plus 1 2`:

```
plus 1 2
= (λm. λn. λf. λx. m f (n f x)) 1 2
→ (λn. λf. λx. 1 f (n f x)) 2
→ λf. λx. 1 f (2 f x)
→ λf. λx. (λf. λx. f x) f ((λf. λx. f (f x)) f x)
→ λf. λx. (λx. f x) ((λx. f (f x)) x)
→ λf. λx. f (f x)                      -- that's 2 + 1? Slow down.
```

1: Wait, we computed `1 (2 f x)` which indeed applies `f` once to `(2 f x)`, i.e. `f (f (f x))`.  
Fix the step-by-step carefully:

Re-do the last three lines more slowly:

0: Ok, let's go slower.
```
λf. λx. 1 f (2 f x)
= λf. λx. ( (λf. λx. f x) f ) ( (λf. λx. f (f x)) f x )
→ λf. λx. ( (λx. f x) ) ( (λx. f (f x)) x )
→ λf. λx. ( f ( (λx. f (f x)) x ) )
→ λf. λx. f ( f (f x) )
```

This is Church 3. Good.

1: Fine. Show me one example where α-conversion matters.

0: Reduce `(λx. λy. x) y` applied to `y`:

```
((λx. λy. x) y) y
→ (λy. y) y         -- WRONG if we substitute naively!
```

We must rename the inner `y` to avoid capturing the free `y` used as an argument:

```
(λx. λy. x)  ≡  (λx. λz. x)   -- α-convert inner y to z
((λx. λz. x) y) y
→ (λz. y) y
→ y
```

Without α-conversion we would have (incorrectly) gotten `y` bound by the wrong λ.

1: Recursion without names?

0:  The Y combinator:

```
Y := λf. (λx. f (x x)) (λx. f (x x))
```

Show the key equation `Y f → f (Y f)`:

```
Y f
= (λf. (λx. f (x x)) (λx. f (x x))) f
→ (λx. f (x x)) (λx. f (x x))
→ f ( (λx. f (x x)) (λx. f (x x)) )
= f (Y f)
```

That's the whole trick.

---
