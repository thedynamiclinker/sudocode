
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

0 uses the Church encoding. 

0 = λaλb.b
1 = λaλb.a(b)
2 = λaλb.a(a(b))
3 = λaλb.a(a(a(b)))

1 uses the simpler encoding:

0 = λa.a
1 = λa.a(a)
2 = λa.a(a(a))
3 = λa.a(a(a(a)))

Without deciding which of these two to use, they attempt to define `succ n`. They do so by reasoning like the following.

0 starts by saying "I'm gonna start here":

succ = ?

1 says "Is that really a good place to start?"

0 says: Gotta start somewhere.

Then 1 says "Don't we just want to wrap the function around one more time? Like if

3 = λa.a(a(a(a)))

Isn't succ n just

succ n = a(n)

So like

4 = a(3)

Or for your definition, since

3 = λfλx.f(f(f(x)))

Wouldn't we just have

4 = f(3)?

Like wrap one more copy of the function around it?

Then 0 says I dunno, substitute in the definitions of 3. Then 1 goes:

4 = a(λa.a(a(a(a))))

and gets confused, because 1 isn't sure if having the lambda inside like that is allowed, and 1 also realizes the scope is wrong.

Then 0 says "Hey 1, I made progress!" And writes:

succ n = ?

1 doesn't think this is progress.

1 says "Hey 0 I made progress," (sarcastically) and writes 

succ n = m

0 is like "Fantastic!" (Not sarcastically.)

1 thinks 0 is acting strange and asks why that's fantastic.

Then 0 says "Well we haven't agreed on which definition of numbers to use yet, but we each have our own definition, so I can do this:

succ = λn λ? λ?. (stuff)

Because succ takes an number n.

Then I can do this:

succ = λn λf λx. (stuff)

Because succ returns a number too, and my numbers are functions that take two arguments.

Now we just have to implement the stuff!

1 says "Isn't that the entire problem? How is this progress?"

0 says "Or course it's progress! Now we know how to undress the numbers!"

1 says "Undress the what now?"

0 says "You had a good idea about wrapping the function around one more time, but you were wrapping it around the outside. Now that the numbers are naked, no more lambdas wrapped around them, maybe we can add the extra copy of f down here."

1 says like how?

0 says watch:

succ = λn λf λx. f(n)

1 says "Wait I think this has the same problem as mine. That n has lambdas on it."

0 goes "Show me?"

1 goes: Look

3 = λf λx. f(f(f(x))

So

3 g y = g(g(g(y)))

0 asks what g and y are.

1 says I used different letters bc I wasn't sure if I'm allowed to plug f and x into a thing that already has those. 0 says I think it should be ok. Then 0 rewrites this as:

3 f x = f(f(f(n)))

Or in general 

n f x = naked n

So now

succ = λn λf λx. f(naked n)

Or

succ = λn λf λx. f(n f x)

And 1 realizes that in 1's version, we have

succ = λn λa. a(naked n)

Or

succ = λn λa. a(n a)

Then, without yet deciding on how to define the natural numbers, they proceed to define:
- addition
- multiplication
- exponentiation, and finally
- the predecessor function x-1

Interleave Kleene's dialogue about Church when it's relevant.

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

---


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

(one rewrites this with pipes)

F T true | λb. λt. λf. b t f
F T | λt. λf. true t f
F | λf. true T f
true T F
F T | true
F | λf. T
T
```

Every step is a β-step.

1: Numbers now. From zero. No skipping steps.

0: Church numerals:

```
0 := λf. λx. x
1 := λf. λx. f x
2 := λf. λx. f (f x)
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
3: rmvar: takes a fun f and an expr e, makes f e (plugs it in)


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
