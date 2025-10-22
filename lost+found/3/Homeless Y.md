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
