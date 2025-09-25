
- Suppose you stumble upon a manifesto written by a charismatic set of developers.

- It proclaims "Every programming language is an ethno-state."

- "We are tired," it continues, "of every language segregating itself behind the walls of its own separate community. We aim to create a language that allows all the languages of the world to cooperate freely, in one program, erasing the barriers between language communities and finally creating a global culture of all developers."

- The goal of this language, they state, is not to become One Language to Rule Them All, but rather to allow true diversity of language choice while supporting communication between them all.

- In this utopian world, each developer on a team could write code in whatever language they prefer.

- You're on a team of Python developers. Want to spend a week writing C instead? Go ahead. Or learning Rust? That works too. The code you write will be usable, just as if it were a normal function, in the meta-language they aim to design.

- The language's most basic "function call" primitive would be to pass control to code written in other languages.

- In this language, you would be able to call `r(p(c(x))`, where `r` is written in Rust, `p` in Python, `c` in C.

- The developer team spearheading this project says "If we fail to support even a single programming language, past present or future, our project will have failed."

- You check the date, to see if this is an April Fool's joke.

- The ambition of a global "language-agnostic developer culture" is as close an analogy as you'll ever find to the Tower of Babel. It's almost just the Babel story copy-pasted, with some minor rewording.

- Like the tower in that ancient story, this utopian project would seem to be a cautionary tale about the dangers of unbounded ambition.

- Implementing such a language sounds like a multi-decade project at best, and doomed to failure at worst.

- This naive dev team is sure to learn before long, that to support the long tail of obscure languages (which they claim is their goal) they'll need a foreign function interface to every language they support, requiring tireless maintenance on behalf of their core developers.


That utopian language exists.

It was created back when the "print" command literally printed on physical paper, and it's on your machine today.

It's the Unix shell.

And after half a century we still do not fully appreciate how strange and ambitious a programming model it is.

Small minds love to complain about the shell for superficial reasons. It's not great at numerical computation. It has a pathetic excuse for a type system. By default when a command fails it keeps going to the next line unless we explicitly tell it to exit.

These complaints are small minded because they completely misunderstand the nature of this language.

The shell is not a programming language.

It is a meta-language, higher level than Haskell, more succinct than Perl, better for rapid prototyping than Python.

When Guido van Rossum created Python, he described it as a mid-level system programming language to bridge the gap between C and the shell.

In other words, the creator of Python agrees that the shell is a higher level language.

Early commits to the python language show the influence of the Unix shell: the python `string.join()` method was originally called `string.cat()`. (You can see this in an old cpython commit whose commit message is "Too many changes to describe.")

So back to the shell.

What is this odd language, and where did it come from?

Many readers will have heard of Steve Bourne as the creator of the shell. This isn't true.

The original shell was created by none other than Abraham himself: Ken Thompson.

![[thompson-shell.jpg]]

TODO: Decide on the moral of this parable and how to end it.

See Also: [here](https://v6sh.org/)