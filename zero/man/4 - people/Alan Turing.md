## Turing published the first Fixed Point Combinator

> Incidentally, in the course of his doctoral work Turing gave the first published
> fixed-point combinator, \[Turing, 1937b, term Θ\]. This was seen as only having minor
> interest at that time, but in view of the later importance given to such combinators
> (see §8.1.2 below), we digress here to discuss them.
> A fixed-point combinator is any closed term Y such that Yx converts to x(Yx).
> Turing’s was
> 
> (λxy.y(xxy)) (λxy.y(xxy)).
> 
> The next one to appear was in \[Rosenbloom, 1950, pp.130-131, Exs. 3e, 5f\].
> It was λx. W(Bx)(W(Bx)), which is convertible to λx. (λy.x(yy))(λy.x(yy)).
> The latter has often been called Curry’s Y; in fact Curry gave no explicit
> fixed-point combinator before \[Curry and Feys, 1958, §5G\], but the accounts
> of Russell’s paradox in \[Church, 1932, p.347\] and \[Curry, 1934a, §5\] both
> mentioned (λy.N (yy))(λy.N (yy)), where N represented negation, and Curry’s
> use of the latter term dated back to a letter to Hilbert in 1929.
> 
> -From Hindley 2006 The History of Lambda Calculus and Combinatory Logic

