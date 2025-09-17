Type: [[Legacy]], [[System]], [[Creation]], [[Parable]]

---

- How does good code become "legacy code"?
- What vices does code accumulate that makes us call it "legacy"?
- What virtues must "legacy code" possess to make us keep using it?
- How can we tell what wisdom is contained in a legacy codebase, and which of the decisions they made along the way were reasonable?

![[autotools-meme-in-xkcd-format.png]]

- Run through the Linux from Scratch project, and you'll see a shocking number of low-level open source projects use the same configuration and build system.
- That system is something called the GNU autotools.
- To a first approximation, the autotools are used by every project in the universe (bash, zsh, cpython, git, coreutils, etc.)

![[everyone-uses-the-autotools.png]]

- The autotools are a GNU era artefact, from the 80s-90s during the height of the free software foundation's influence. The era when python and linux were born.
- The autotools are widely recognized as being [crufty as hell](https://en.wikipedia.org/wiki/File:Autoconf-automake-process.svg "https://en.wikipedia.org/wiki/file:autoconf-automake-process.svg") 

![[bloated-autotools.png]]

- The autotools are implemented using something called m4, an ancient macro processor that is almost certainly installed on your machine right now, and which you've almost certainly never used directly.
- And m4 was written by Kernighan and Ritchie, authors of The C Programming Language, the first book to ever have a "Hello, world" in it.

![[die-gnu-autotools-tweet.png]]

- Ask yourself how the following state is possible:
	- No one loves the autotools.
	- Everyone uses the autotools.
	- Almost no one wants to re-implement whatever it is that the autotools do, even in open source where our culture is to have a near infinite number of reimplementations of any given part of the stack.

![[die-gnu-autotools.jpg]]

Why are the autotools still around, and why do they look the way they do?

Spend an hour trying to reimplement them, and you'll understand why.