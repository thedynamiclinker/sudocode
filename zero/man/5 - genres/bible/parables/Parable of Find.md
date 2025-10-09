Type: [[Painful]], [[System]], [[sys/kernel/Creation]], [[Parable]]

---

As early as 7th edition Unix,
the man page for `find`
contained the following section:

![[find-bugs-section-in-7th-edition-unix.png]]

Everyone agrees the syntax for `find` is odd.

How did it get that way?

Legend tells that one day the professor of a Unix sysadmin class went off on a rant, complaining about various things in Unix.

Along the way, he said

```
Here's another good example of this problem with UNIX.  Take the find
command for example.  WHAT idiot would program a command so that you have to say -print to print the output to the screen. What IDIOT would make a command like this and not have the output go to the screen by default.
```

That's the default now. It didn't used to be. But we digress.

The legend continues.

```
The next morning, one of the ladies in the class raised here hand, the
instructor called on her, and she proceeded to say something like this:

"The reason my father programmed the find command that way, was because he was told to do so in his specifications."
```

No one knows if the story is true, but [Dennis](https://doc.cat-v.org/unix/find-history) said it was consistent with what he knows.

We often don't know how things got the way there are.

But the legends that hint at what happened contain a timeless truth.

Moral:

- When implementation precedes specification -- when we create before we plan -- we developers are in charge of the design our tools. In this process, we all make bad decisions early on, but then we fix them once we and our code's early users feel the pain of bad design, and experience suggests a better way. This is bottom-up design, and it is The Right Way to create good code.

- When specification precedes implementation  -- when we plan before we create -- the imagination of the planner is in charge of the design. In this process, bad decisions come down from on high and become codified as gospel, and they persist even after experience suggests a better way. This is top-down design, and it is The Right Way to create code that either dies an early death, or ends up with man pages like this if it survives.

![[find-bugs-section-in-7th-edition-unix.png]]
