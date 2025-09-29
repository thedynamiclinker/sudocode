## Numbers Called Nothing
### Or: Church Kleene
### Or: The Unnamed Number
### Or: The Unnumbered Name
### Or: The 💯th member of the 11nity
### Or: The increasingly inaccurately named trinity
### Or: The First Programmer
### Or: The First Standard Library
### Or: The First Critical Vulnerability
### Or: The First RTFM
### Or: Frighteningly Technical

---

![[kleene-1.jpg]]

---

> John Crossley: What did you do Steve? When you first started learning logic. You didn't have books did you?
> 
> Steve Kleene: We didn't have books.
> 
> Gerald Sacks: You had _Principia Mathematica._
> 
> _(Everyone laughs)_
> 
> Steve Kleene: Well, I never read _Principia_. Of course I thumbed it a little bit... Rosser I guess started his logic that way... But I learned logic by learning Church's system which was subsequently proved inconsistent.
> 
> _(Everyone laughs)_
> 
> Steve Kleene: And y'know, it all consists of abstract lambda definability. And uh, and it was only after I got my degree that I really began to read much of the litchrachoar.

1: What's "litchrachoar"?

0: Sorry, that's "literature."

1: Did he spell it like that?

0: No, this is an old audio recording.

1: So you spelled it like that?

0: I wanted to capture his accent.

1: Well don't.

0: Ok. Just imagine it. He's got a charming sort of unpretentious midwest thing going on.

> Steve Kleene: It was only after I got my degree that I really began to read much of the literature. Uh let me see. Hilbert Bernays, didn't the first volume of that appear in 1934?... Hilbert Bernays was around... I never read Lewis and Langford.

1: This is Church's student?

0: Yep. 

1: The one who that book called "frighteningly technical"?

0: That's him.

1: Doesn't seem too frightening so far.

0: How so?

1: Well he never read that one book, or that other one. Said he didn't read much of the literature during school. And you said he's got an unpretentious vibe. Can't be that frightening.

0: And he learned logic from a system that ended up being inconsistent.

1: So?

0: Well I imagine that sort of thing hammers it into a person that most of what we say about logic is wrong.

1: Not following.

0: The principle of explosion and all that. In standard logic, we always say a single contradiction makes the whole system useless. But it wasn't useless.

1: Wasn't useless how?

0: Well, Steve learned logic from it.

1: What system was that again?

0: Church's first attempt at the lambda calculus. Turned out to be inconsistent. And that means this Kleene guy, easily one of the best logicians of the 20th century, learned logic from an inconsistent system. So it can't have been entirely useless.

1: How did Church figure out his system was inconsistent?

0: From Kleene.

1: Damn.

0: And a friend. That guy from earlier called Rosser who actually read Principia Mathematica.

1: What's Principia Mathematica again?

0: That's Bertrand Russell's book.

1: The paradox guy?

0: Yeah. It's not super readable.

> Steve Kleene: And \[I read\] a lot of papers... _(Pauses.)_ For instance by Gödel. The first thing we knew of Gödel's paper was one time the mathematics colloquium speaker was gonna be von Neumann. And of course von Neumann had lots of things of his own to talk about but instead of that we got him there and found out he was telling us about Gödel's 1931 results.
> 
> Someone: This was at Princeton?
> 
> Steve Kleene: This was at Princeton and it was in the Fall of 1931. And whether he had the paper itself or not I don't know... 
>
> C. C. Chang: Was this the first you'd heard of Gödel?
>
> Steve Kleene: When we went into this meeting was the first that any of us heard of Gödel. Church was teaching a logic course, Rosser and I were among the students, it was the first that any of us had heard of Gödel. I don't know whether Church was aware of Gödel's 1928 paper on completeness, he never gave it in class, because I... I never had the classical form of the propositional or predicate calculi in my coursework, I learned them for myself afterwards.
> 
> Steve Kleene: So as soon as we heard the lecture, the paper was available. We hadn't noticed it, y'know, we didn't go looking at every journal that came into the library to search it through for papers that would interest us, maybe we should've but we didn't, so of course we went and we read the paper right off.
> 
> Steve Kleene: Church was convinced that there were sufficient differences in the way logic was formulated in his system that it would escape the theorem that you couldn't prove its completeness in the system itself. _(Pauses)_ And of course he was right.
>
> _(Everyone laughs)_

1: Why did everyone laugh there?

0: Church was right, but for the wrong reasons. He thought his system would be "good enough" to avoid Gödel's theorem and be complete anyway. Turns out early lambda calculus was complete, it could prove its own consistency, because it was inconsistent and could prove anything.

1: Logic is trippy.

---

TODO: Clean this up.

TODO: 6:50. Church didn't think it would be possible to implement predecessor in lambda calculus. Kleene realizing how to implement predecessor at the dentist.

TODO: 7:15.
> Steve Kleene: So there was no idea at the beginning that this was going to be all effectively calculable functions.

TODO: 7:30.
> Steve Kleene: I kept taking it as a challenge and everything I tried I could work.

> Steve Kleene: It was an unexpected fallout that this could represent all effectively calculable functions.

> Steve Kleene: The basic work was done between January 1932 and the next 5 or 6 months.

> Steve Kleene: Everything I tried, every kind of function I tried to define, every kind of effective operation that I tried to parallel by lambda definability, I probably knocked off within the first 5 months.

> Steve Kleene: For us the first concept of lambda definability was after the fact, after having formulated the notion of lambda definable functions as simply the ones for which you could find formulas in this symbolism. And discovering that everything you thought of that you wanted to prove lambda definable you could!... But it was Church, I have to give the credit to Church, I can't take it myself, he said "Y'know, don't you think maybe we've really got ALL the effectively calculable functions?"

0: He's being generous.

1: To Church?

0: Extremely generous.

1: What do you mean? I thought Church was one of the giants of this whole field.

0: He was. But even Church knew how incredible Kleene was. And Kleene gets ways less credit for all this than he deserves. Dude was clearly the first programmer. I mean sure, Church wrote the first language, Gödel wrote the first compiler, and Turing made what was arguably the first hardware design, but by that same standard, Kleene made:

- Wrote the first standard library.
- Found the first critical vulnerability (λ calculus inconsistency).
- First to have contact with all three of the above and to demonstrate their equivalence.
- First to clean up and popularize the ideas in his (frighteningly technical) _Introduction to Metamathematics_.

1: What do you mean "first standard library"?

0: Well we saw up above how lambda calculus doesn't even come with built-in booleans or integers. And Church didn't even think lambda calculus was powerful enough to express the function $f(x) = x-1$ where x is a positive integer. Kleene's the one who "implemented" all the types and functions that built things from that totally useless level all the way to what eventually became "all computable functions." So Kleene's definitely being humble.

1: Sounds like it. It's crazy I've never heard of this guy before.

0: For real. And from Church's perspective, imagine this grad student of yours who's never even taken a logic class before comes to work with you, learns your system, and then he just keeps knocking off one problem after another until the two of them ended up going from thinking $f(x) = x-1$ is too hard, all the way until Church himself got convinced that _all possible computations_ were representable inside this system.

1: How did Church get convinced?

0: Kleene won't admit this, but it was his "programming" that convinced Church. I mean sure Church designed the lambda calculus, but Kleene figured out how to use it like a frighteningly technical nerd.

1: How do you know?

0: Just read Church's papers. He makes it extremely clear. I swear he cites Kleene in one paper like a hundred times. Check it out.
