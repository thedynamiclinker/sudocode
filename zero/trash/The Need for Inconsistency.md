
## Logicians and Inconsistency

- Frege's system was inconsistent, Russell learned logic from it.
- Church's first system was inconsistent. Kleene learned logic from it.
- Haskell Curry's combinatory logic was inconsistent. I don't know if any logicians learned logic from it, but it's not implausible to suppose some did.

According to our standard informal reasoning about inconsistent formal systems, this should be impossible.

In practice, inconsistent formal systems have surprised us not by their uselessness, but by their usefulness. Not by their triviality, but by their similarity to consistent systems.

Of all facts in logic, no other is more important and less explored.

## Our blindspot

To a first approximation, the view on inconsistency in mathematics and logic has been that it is the worst thing a system can possess.

In rare cases when an alternate view is expressed, it is typically shrouded in mysticism, naivete, imprecisely defined terms, and the general sense that we're not having a serious conversation about mathematics or logic.

While there have been fascinating explorations into the topic of paraconsistent logics (Graham Priest) and that mathematics that can be developed on top of those systems (Mortensen), the mathematical community at large has neither explored nor embraced these results, and our point here is not to suggest they do so.

The aim of this file is to argue that any sufficiently robust formal system for representing mathematical truth must eventually reject the principle of explosion, while at the same time preferring more consistent to less consistent states.

Consider a large formal mathematics project like the Lean prover community's Mathlib.

Consider the following thought experiment, and ask how we would like the resulting system to behave.

Suppose we were able to inject a contradiction into the Mathlib repository.[^1] 

This might be done, for example, by formalizing the definition of Reinhardt cardinals and adding an axiom that such a cardinal exists.

This fact implies the Kunen inconsistency due to its incompatibility with AC, but suppose somehow (for the sake of argument) the definitions to carry out the proof of the Kunen inconsistency have not been formalized.

For that or any other reason let's assume we've got a Mathlib with Reinhardt cardinals and Choice.

This is an inconsistent system.

Question: Would we actually notice?

[^1]: While unbounded comprehension bugs used to be an easy way to get root on mathematics in past centuries, mitigations in the years since 1900 have made such exploits impractical, primarily due to type systems and restrictions on comprehension.
