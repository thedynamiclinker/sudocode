
## /

### Before doing anything below this
- Clean up this file.
- Nearly everything below has either:
- Already been done, or
- Is irrelevant because we did something better, or
- Is irrelevant because the dialogues decided to go a different way.


### We
- During ld.so when the conversation moves into `/opt/art`, that should really be in `the-second-law` or something linked to it.
- Move this content later, so that we can more quickly get to the three members of the trinity, or what we'll call `/dev/zero`
- That is, the 0th developers:
	- (a) Alonzo Church, with the Lambda Calculus
	- (b) Kurt Godel, with general recursive functions, and
	- (c) Alan Turing, with Turing machines.
	- Stephen Kleene is the most central figure to showing that all these definitions are equivalent, and in many ways he was the first developer not including the language designers. He was the one implementing things in early lambda calculus that even Church didn't think were possible. Show the screenshots in `/var/include` where the Hirst book mentions that Kleene's book is only for those "with a frighteningly technical bent." Then show what that frighteningly technical bent is, and that it's essentially just doing something simple in a system where you can't skip steps: make the case that this is early programming. Programming isn't about machines, it's about systems that are sufficiently well-defined that their interpretation does not require a human mind. Mathematics is not this. It has never been this, even in the books devoted to its formalization and axiom systems, which have a persistent habit of _not working within those systems._ The reason for working within these systems is not the lack of intuition in the user, but the desire to create something that can be interpreted mechanically, and therefore can transcend the boundaries between minds, between species, and even between the living and non-living: computing machines or human minds can read the same code and execute the same sequence of steps, without the need for a high level undocumented mind to use outside knowledge about the world to fill in the missing pieces. In other words, programming is what mathematics becomes in the extremely rare cases when that mathematics is well defined.

### /boot
- The /boot dialogues were good, especially the bit with the binary loader we wrote in C.
- Need to find somewhere to put this, because it doesn't quite belong anywhere in the narrative yet.

### /usr/src/bash

We've got a bug in bash upstream related to "history" that's also somehow about being inside case. The fact that most people don't know bash is maintained by one guy is a different kind bug in our history, and it's also related to being inside case (Chet is at Case western reserve university.) Reach out to Chet, make him a character, have a dialogue where he helps 0 and 1 fix the bug, and make a who's-on-first style dialogue with the history history case case stuff above.

### /opt/art

- [ ] Need to explain eventually that:

- The art means "arithmetic run time."

- To be explained once we get to the man dialogue and see brt1 and brt2 in early Unix.

- Need to explain crt1.o, crti.o, crtn.o too.

- The crt files live in /lib. The brt files lived in /etc. No one seems to know where to put these, so the "a" files go in /opt.

- A good time to explain the crt files is probably somewhere around the babel dialogue. There we can cover the original hope of cross language code sharing at the object file and linker level, and show what happens if we do it naively.
- Much like crt gets linked into every C program, formal Arithmetic (and incompleteness) gets linked into any formal system strong enough to express Arithmetic.


![[man-001.png]]

### @world

Contact Chet Ramey, explain that you've found a bug, and would like to include it in a book. The book is called "sudo code", and it's a series of technical dialogues between two characters, 0 and 1. The 0 character is a sort of teacher figure, 1 is younger and more in touch with modern side of computing, but less aware of our shared history (Unix, C, GNU, and important things like who Chet Ramey is.)

I'm a former Basic Books author and I've already published a book that was translated into 6 languages by various publishers around the world, so I know enough of the process that I think the project is pretty realistic and within the achievable range given my personal set of skills && flaws, the latter of which is a larger set than the former, but at least I know enough of computing to write a book that might plausibly be something unique.

I'm sure you're busy so I don't want to bother you unnecessarily, but I'm also reasonably confident that you don't have a TON of requests coming in asking if you'd like to be involved in a dialogue with two abstract characters named 0 and 1 about the history of computing, so I feel confident enough to gently nudge you in the direction of saying "Hey Chet, do this."

Hey Chet, do this.


### /lib/ld.so

The "Foundational People" dialogue.

Possibly Cover:
- [L||D](https://en.wikipedia.org/w/index.php?title=Names_of_God_in_Judaism#Erasing_the_name_of_God:~:text=The%20words%20God%20and%20Lord%20are%20written%20by%20some%20Jews%20as%20G%2Dd%20and%20L%2Drd%20as%20a%20way%20of%20avoiding%20writing%20any%20name%20of%20God%20out%20in%20full.). Oh are you religious? What no read the link again. "...as a way of avoiding writing any name of God out in full." Why else would you avoid writing out the name of God in full? ...To save keystrokes. To save keystrokes? Why does anyone avoid typing anything in full? Because it's long. This is an ancient principle among our people. Who's our people? Unix. Well, not really. But they're the closest thing to our people's modern representatives. Mention i18n an l10n. Cover no vowels. Cover ld as "dynamic linker" and writing backwards. Cover the logo. 
- Well there's a lot of stuff in life that never makes sense unless you know how the original authors wrote. Show Bill Joy's vi keyboard with the arrows on the letter keys.
- Start to get into our history.

### /usr/share/man

The man dialogue.
- 0 shows 1 the first edition Unix man pages.

### /dev

- Add a constructivism directory with some talks by Andrej Bauer.### /use/share/dict

#### The ⟂-docs
Pronounced "Orthodox." The orthogonal documents. Refers to theoretical computer science, primary computability and complexity as elaborated in the decades since the lambdas and the mus split. Though it appears on the surface to be the same culture, it is mostly orthogonal to the history of our people.

#### antigist
1: What was the point of showing me all that code I didn't understand back in /opt/art? And why was it in a file calle---

0: Antigist.

1: What?

0: That's why I showed you. It's important in our field to give the Antigist of things whenever possible.

1: The... an---

0: Antigist. Exactly.

1: Is that like the opposite of Tigist?

0: What? No. Why would it be that?

1: You know, like anaerobic, anemia, anarchy. The "an" means "opposite."

0: ...Not here.

1: So it's not the opposite of Tigist?

0: What's Tigist?

1: I dunno.

0: Anti-gist.

1: Oh!

0: The opposite of gist.

1: Why would that be a good thing?

0: Are you kidding? It's a great thing! Especially important in our field. 

1: But wait, "gist" is like... the only part you need to understand, right?

0: Absolutely not.

1: You don't like the "gist" of things?

0: I never said that. I love "gist." The gist of things is usually the most important part.

1: I'm so confused. Isn't that what I said?

0: Not even a little.

1: Explain?


### babel


At this point, having emphasized the Optimize for Sharing principle, we begin the babel puzzle.

- Change hostname to world.
- And the whole world was of one language, and of one speech.
- What language?
- Machine language.
- How is that one language? There are plenty of different instruction sets.
- I said the world not the universe.
- (Show prompt)
- See?
- Oh.
- Language boundaries are a fiction. To the machine, they're all the same. Simply learn to use LD - the linker - and nothing we imagine will be impossible. We can build a stack to the heavens. Through LD, all things are possible.
- Never thought of it that way. I don't know much about LD. Teach me!
- Babel puzzle starts here.
- The first LD is the linker. The thing that offered the power to make all languages become one, but scattered the languages of the earth and reminded our people to remain humble.
- Humility leads to the other LD: ld.so. Code sharing through exec, for which ld.so is responsible, and this eventually leads to Unix and pipes.
- Two LDs, one is the elder LD from the babel story, the other is the Second Order LD, the loader, that performs a similar function to the elder LD at runtime, but does so to support a more humble and powerful method of code sharing: exec.

- Once we get exec, the babel puzzle is complete. We immediately start Genesis 12, which is a long begat list that leads to Abraham (aka Ken.)


### bbl1.o, bbli.o, bbln.o

TODO:
- Continue where the babel dialogue left off, explaining the "git blame" below and how the bible is more like a code base than any other genre.
- Mention that the boring parts are mostly by the bureaucrat (priestly source.) Same as codebases.
- Then at the end of this file, have 1 say this is fun and all, but I came here to study programming, not bibles.
- Use this to transition to bbli.o, aka "biblio" aka "bibliography" aka "previous research in computing bibles." In that file we cover PoC || GTFO.
- After bbli.o, do bbln.o, which explains what we won't be doing. In that file, cover "The Linux Bible," and also say we won't be doing a slavish repetition like for example: Then say "We won't be starting with hello world, and then saying something like The Python was the cleverest of all the creatures, humans acquired knowledge of best practices, this knowledge sentenced them to mortality. Soon after, two sons, Simplicity and Complexity. Complexity kills Simplicity, etc. Then we definitely won't be saying Ok what comes next and finding an excuse to insert something about Babel, and then putting in a begat list that takes us from Babel to Abraham, who is of course the ancestor of our people whose descendants are as numerous as stars in the sky, which is naturally Ken Thompson, then---"
- 1 says "That sounds like 80% of what we've been doing. Plus the new bits about best practices."
- 1 says "Look this is nice and all but I'd really prefer a true history."
- 0 says "Define true."
- 1 says "Like what actually happened? How was our field actually created? Obviously this stuff about the snake is a parable or something. And saying that complexity killed simplicity doesn't really teach me anything I didn't already know. Plus it's not true."
- Then switch to /bin/whoami and the history of computing from the early days of foundations and Church/Godel/Turing.

### visit databases as a location of a file system and be like this is a f****** abomination 


