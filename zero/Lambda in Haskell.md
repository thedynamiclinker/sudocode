```haskell
ghci> let troo = \a b -> a
ghci> let fals = \a b -> b
ghci> let ifte = \a b c -> a b c
ghci> ifte troo fals troo

<interactive>:31:1: error: [GHC-39999]
    • No instance for ‘Show (p10 -> p20 -> p20)’
        arising from a use of ‘print’
        (maybe you haven't applied a function to enough arguments?)
    • In a stmt of an interactive GHCi command: print it

ghci> (ifte troo fals troo) 3 4
4
ghci> (ifte troo fals troo) 3 4
4
ghci> (ifte fals fals troo) 3 4
3
```

