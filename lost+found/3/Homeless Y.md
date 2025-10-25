## A bit more work towards Y premathematics

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

## Y combinator

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

That's the whole trick.
