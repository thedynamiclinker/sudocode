
```
# Table of Contents

0. The Book of Roots: /
1. The Book of Users: /usr
```
![[the-first-draft-of-anything-is-shit-wallpaper.jpg|300]]

## Summary

1. Write the five "repl" dialogues in lost+found.
2. Submit the bash bugfix.


## Before anything else
- [ ] Import video notes from what is mathematics vault.
- [ ] Get /etc/apache screenshots off of phone and onto laptop.
- [ ] Update "The Upsilons": The Fork, or the U turn. 

## Church

### 5
- [ ] Rewrite "The Little Lambda" from scratch.
- [ ] Church's definition from first principles: How would you come up with Church's idea if it didn't exist yet? So farwe'vegot formal Arithmetic from Peano, and formal Set Theory from Zermelo and friends. What if you thought everyone was doing it wrong? Or at least missing something? What's more fundamental in mathematics than natural numbers or sets? Well, it wouldn't be crazy to say "functions." So what if everything is functions? Now how would you come up with the Church numerals? Well in every formal system with one type, you always have to encode things. (1) The von Neumann encoding in ZFC because ZFC doesn't have built in integers. (2) Even first order arithmetic has to "encode" the integers in a sense: 0 is the only built in. 1 is S(0). 2 is S(S(0)). 3 is S(S(S(0))). So how do you encode the integers if all you have is functions? Well Peano Arithmetic already did it! We just saw it. 3 is "call a function 3 times." And voila, you've got the Church numerals. So we miss the point a little by calling it Lambda Calculus. We've got "Formal Number Theory" and "Formal Set Theory." We should call Lambda Calculus "Formal Function Theory."
- [ ] Kleene: Screenshots of "Church's Thesis" section of Introduction to Metamathematics.
- [ ] Kleene: Mention that Kleene invented regexes in a paper about neural networks and Ken cites him.


## Godel

### 1
- [ ] Gödel dialogue: "Mr Why."
- [ ] Gödel dialogue: The incomplete story of incompleteness: Definitely need to mention the rarely discussed side effect of the incompleteness theorems: If mathematics is more limited than we thought, suddenly it becomes a lot more plausible to define "computation." Even the space of "all possible computations" is potentially within the reach of a formal definition. Though many of the main players involved in the early theory of "effective calculability" didn't expect that they were capturing all possible computations in their definitions, it's probably not an accident that all 3 of our definitions of "computable" appeared within 5 years of Gödel's incompleteness theorems. In the years from 1900 to 1931, it simply didn't feel plausible to give a definition that might hope to capture all possible computations. In a very real sense, we may owe the origins of modern computing to the discovery of incompleteness.

### 3
- [ ] Start by giving the definition of General Recursive functions.
- [ ] 1 doesn't have any questions, this one makes perfect sense.
- [ ] Instead of questions about the definition, ask how it's equivalent to lambda calculus.
- [ ] Use Lectures on the Curry Howard isomorphism book to explain the equivalence.

### 5
- [ ] Gödel's definition from first principles: To get inside Gödel's head, we have to recognize his definition as a different approach to Formal Function Theory, one that's much more like a standard axiom system than Church's. After all, Church said he never had other mathematicians to talk to about his interests because he was the only one in his field. Church's work is much more "Ex Nihilo" than the other two, and much more minimal as a result.
- [ ] To derive this definition from first principles, show the definition of Gödel numbering, then work through enough of the encoding of formal arithmetic into itself that the definition of General Recursive Functions becomes clear.

## Turing

### 3
- [ ] Turing dialogue: Mention Turing becoming Church's graduate student.
- [ ] Turing dialogue: Include first page of Kleene's chapter on Computable functions.

### 5
- [ ] Turing's definition of computation is not inherently a "machine" any more than Church or Gödel's. But there is an important sense in which it's more fundamental than the others.
- [ ] Turing's "Formal Theory of Paper" and why it convinced the others: To get inside Turing's head, we have to recognize what he was doing as "Formal Paper Theory." Turing's theory is the axiomatic development from first principles of what can be done with paper and a pencil. Church and Gödel both made "Formal Function Theory." Turing made "Formal Mathematician Theory" by making "Formal Paper Theory," which is how he convinced the others that he (or all of them) had captured anything that could be computed by any means. Turing's paper is always described as being about computing machines. What no one says is that he actually formalized the theory of "Making marks on paper." That's how his result is in a sense more conceptually viral than the other two. If you formalize functions, it's easy to think you've missed something about computing in general. If you formalize the process of making marks on paper, it's very hard to worry that you've missed something.
- [ ] Turing's definition is literally just a finite number of case statements and three system calls: read, write, and move.
- [ ] Read takes no arguments.
- [ ] Write takes any single character as an argument.
- [ ] Move takes a 1 bit argument that says whether to move left or right.
- [ ] Turing writes these as: write: P0 writes 0, P1 writes 1, Px writes x, E writes a blank aka erases the square. Maybe this is a different system call. move: L moves left 1. R moves right 1. read: Turing doesn't express the read system call as code. The read is assumed to happen automatically, and be provided in a "machine register" of sorts that he calls the current symbol.

## 0 explains the tiger data sructure to 1

The Tiger: The Tora as a Data structure
Or: The Tiger's stripes: A generalized story schema about what it's like to create anything.

- Genesis: In the beginning, there was simplicity. Include background information and cultural context here.
- Exodus: Ok, begin story. Once upon a time life sucked and everything was way too complex so we left to make something new and simple. We started with simple code: ten rules, one line each. The people didn't like this and complained that the old way was better. Tl;dr: We tried simplicity and founder mode but the people didn't like it and complained that the old way was better.
- Leviticus: Every time something bad happened the people demanded we add new commandments. We ended up with eight million goddamn unhelpful laws. Our simple thing got complex just like the place we left.
- Numbers: That led to endless bitching and moaning and complaining by the normies about how things suck now and used to be better before, because they don't remember they were unhappy back then too so they're just blaming the new thing now cuz it's the thing. Tl;dr: We tried complexity and structure and bureaucracy mode but the people didn't like it and complained that the old way was better.
- The Second Law: The Leaders are getting old. The people aren't remotely capable of filling their shoes, and the first round of complainers is mostly dead. But their kids have now grown up in the new system, and it's time to pass on the lessons we've learned in this lifetime before we pass on. Kids hate complexity anyway, so "Turn the lessons into a kids book" is a great excuse to delete the complexity that accumulated over the years. So we refactor the complex pile that our simple idea became, and reiterate it in its simple form. Also bring along a small subset of the detailed complex stuff we learned along the way, but mostly return to where we were in step two so we don't become the thing we left in step two. Repeat until the lesson is forgotten and you become Egypt and it's just time to die.

## /lib/tor.a

- [ ] Use the best abridged excerpts from version of [[The Aspiring Bible Author's Guide to the Torah]] to show 1 what a strange writing style we're actually dealing with. This convinces 1 that the bible genre is hilarious and fun and we need one.

## shave and a haircut - two bits

![[shave-and-a-haircut.png]]

- Need to have 1 make this joke somewhere and 0 doesn't get it.
- Have 1 knock on the door of some directory in this pattern.



---

![[kill-your-darlings.jpg|300]]

## Eventually

- [ ] Mention: _Proofs are computations with partially defined values._
- [ ] /bin/bash: Church received an honorary Doctor of Science degrees from Case Western Reserve University in 1969!
- [ ] /bin/bash: Contact Chet Ramey, explain that you've found a bug, and would like to include it in a book. The book is called "sudo code", and it's a series of technical dialogues between two characters, 0 and 1.
- [ ] /dev/lunduke: Modern Lunduke has become exactly Isaiah and it's amazing. Needs to be part of the story. Need to also add Matthew Garrett.
- [ ] /bin/vi: Show Bill Joy's vi keyboard with the arrows on the letter keys. A lot of stuff in life that never makes sense unless you know how the original authors wrote.
- [ ] /usr/share/man: The man dialogue: 0 shows 1 the first edition Unix man pages.
- [ ] /dev/sigma: Add directory with some talks by Andrej Bauer.
- [ ] /bin/cc: Song of the C. Dead C Scrolls. Ancient Unix.
- [ ] /boot: The /boot dialogues were good, especially the bit with the binary loader we wrote in C. Need to find somewhere to put this, because it doesn't quite belong anywhere in the narrative yet.
- [ ] /usr/src/bash: We've got a bug in bash upstream related to "history" that's also somehow about being inside case. The fact that most people don't know bash is maintained by one guy is a different kind bug in our history, and it's also related to being inside case (Chet is at Case western reserve university.) Reach out to Chet, make him a character, have a dialogue where he helps 0 and 1 fix the bug, and make a who's-on-first style dialogue with the history history case case stuff above.
- [ ] /usr/share/dict: The ⟂-docs: Pronounced "Orthodox." The orthogonal documents. Refers to theoretical computer science, primary computability and complexity as elaborated in the decades since the lambdas and the mus split. Though it appears on the surface to be the same culture, it is mostly orthogonal to the history of our people.
- [ ] /var/lib/rectangles: At some point, in the course of explaining the /etc/groups, we visit a relational database as a location in the filesystem and be like "this is a fucking abomination."
- [ ] Make this point somewhere: The "ALU" field -- formal logic and formal arithmetic -- is unique among all technical fields in that it requires no outside prerequisites in order to understand the advanced results in the field and to read the original papers. To be sure, these original papers are often extremely technical, much more technical than most advanced mathematics, but they are far more precise and self-contained than standard mathematics. They typically do not assume the reader has a large amount of background provided elsewhere. The exceptions that prove the rule are confined mostly to informal or semi-formal set theory as found in for example Jech (Set Theory) and Kanamori (The Higher Infinite). Reading Jech feels as if one is reading a normal mathematics book that happens to be about sets. Reading Kanamori feels like one is reading an academic paper or series of them that mixes history with definitions and results that are very hard to understand the motivation of without "culture provided elsewhere." The ALU field is different. It's content is quite literally the arithmetic one learns in kindergarten, and the logic one barely has to be taught. Starting from these intuitive primitives, the subject creates formal languages designed to capture these most basic of notions, and this process is open to readers with no background whatsoever in the field. This is less true for monographs on model theory and proof theory, and it becomes less true for post-Kleene 1952 books on computability and eventually complexity, which often manage to read more like standard mathematics than like foundations. Nevertheless, the ALU field provides foundations in the realest sense of the word. It is the historical origin, the cultural origin, and the logical/technical/formal origin story of the field we now call computing. And its most technical results can be appreciated, with some work, by anyone who regularly reads or writes code in any language.
- [ ] Realization: The first law of mathematics: Semantics beats Syntax. Symbols aren't special. All mathematically meaningful quantities are invariant up to isomorphism, and isomorphism means renaming. The first law of foundations: Syntax beats Semantics. Any interpretation of the symbols is equally permissible, provided it's consistent with the syntax. Model theory results from this. This is not as diametrically opposed to the above law mathematics as it seems, but they are distinct approaches.
- [ ] The nus: Walter Pitts of McCullough and Pitts is a fascinating character. Used to crash Bertrand Russell lectures at age 15. Was homeless when he presented Carnap with an annotated copy of his book. Carnap looked around forever trying to find who this kid was. Pitts was extremely eccentric and avoided any situation that would require him to sign his name. He was aware of Leibniz's ideas about a universal language or universal computing machine, and he used that and Turing's ideas as the basis for the first ever paper on neural networks.

## Principles

Ideas for principles.

### Code
- Create from subtraction (unix, linux, python, Ken setting out to write a Fortran compiler and creating B instead.)
- Design by Implementation (Ken Fortran to B, Guido on Python.)
- Separate plumbing and porcelain (git).
- Fail like an escalator (Hedberg's Law.)
- Worse is Better (Unix, Git the stupid content tracker, Languages like Scilab that allow you to index past the end of an array and automatically expand it when you do. When a tool is too smart or too helpful, it becomes impossible for the user to reason about. When the user is technical, this usually makes the tool worse.)

### Documentation
- Write Executable Documentation (Linus's Documentation Always Lags Reality, Eelco's If you need a Readme.md to explain how to build a project you've already failed.)
- Don't test internals. (Related: Write executable documentation.)
- Don't document bad code, rewrite it. (Brian's law. Related: Writing is easier than Reading, Deleting is easier than Writing.)
- Metacommentary solves everything. (Narrator's law)

### Human Behavior
- Eat your own dogfood (Linus autodialing his Minix partition and being forced to use Linux until it was completely self hosting.)
- Adding people makes it slower (Brooks' Law)
- Motivation isn't Free (Landley's Principle. Stopped maintaining busybox because it stopped being fun.)
- Cultivate Laziness, Impatience, and Hubris (Larry's principle.)
- Laws Aren't Real (Or: Use constraints to change behavior. Or: Make undesirable states impossible. Or: Use commitment devices to avoid deals with the devil. Haskell's lesson that laziness forced them to be pure. Linus autodialing his Minix partition. Rust's use of this principle. Thomas Schelling's commitment devices from The Strategy of Conflict.)

### False gods
- Planning is Pretending (Linus has quotes about this somewhere. Related: Most Affordances are Implicit, Snowman imagining Summer.)
- Code is a liability not an asset (Diederich's law.)
- Early success is a curse: The child star principle (SPJ's example of haskell bug that deleted your source code and why it didn't matter. Guido's example of why you shouldn't want your code in the standard library. Guido's example of how difficult the Python 2 to Python 3 transition was, Perl waning in popularity before releasing Perl 6.)
- Avoid Shamans (Grug's Law)
- If nobody loves it, don't use it: The marketing firewall principle (Related: Motivation isn't free. Designed to avoid using tools you believe to be "industry standards" or "best practices" in the many cases where those tools will make your life worse. In practice these tools tend to be the ones with a lot of marketing effort behind them. Even if you're using a free version of a tool (e.g., a free database), the fact that databases as a category have more marketing energy directed toward them than (say) text files means that databases as a category should be regarded with greater suspicion. The cases when such tools are the right choice always depends on quantitative, not qualitative, details of the tradeoff.)
- Don't be too contrarian. Some of the things you think are mediocre popular shit are actually timeless truth. Listen.

## Questions

Q: How are The Root Enterprise and Hello Corporation and The Dynamic Linker and Doubleunix fit into the narrative of Sudocode?

A: The Root Enterprise is owned by the 0 character. Dialogue about how 1 has to go to work. Says that 0 doesn't seem to have a job. They talk about that. 0 says actually I'm quite the business type myself. 1 doesn't believe it. Thats when 0 walks 1 through The Root Enterprise. Shows 1 around Hello Corporation. KEY THING: 1 says these aren't businesses. 0 says what do you mean? 1 says "I mean to be a business you have to have a product or a service or a sales pitch or a store." 0 says "Those aren't businesses, those are ways of making money. A business has nothing to do with making money. A business is just a legal thing." Then import BWKH material directly into the story. Everything we've done is food for the book. Onward!

## The 2ⁿ

### The 64 Laws

- Model for the book: I didn't originally think of it like this, but this book is essentially the 48 Laws of Power for Computing. It's as broad in its coverage of Computing as 48 Laws is in its. It's similar in that it takes virtually all of its wisdom from "the greats," and cites them heavily. Put Joost Elffers on the list of publishers to contact. We'll also very likely need to commit to being published in color at least in a minimal way, like Robert Greene's books. Greene was 39 when the 48 Laws was published. I'll be 39 next year. It was his first book. I've published a book before with Basic Books, and it was translated into 6 languages. I'd propose that it's not unrealistic for us to achieve similar levels of acclaim for technical writing that Greene's books have for human nature.

- Robert Greene's 48 Laws are on average 42 characters long. That's a good length. We may be able to get to 32. Update: We're currently at 27.2. Keep this up!

### The 64 Bits

- The 64 Principles. The 32 Values. (May be only 16 or even 8. Determine empirically.)

- If you shoot for exactly 64 principles, you can use single 64 but ints as vectors to encode the relevance of arbitrary pieces of content to every single section of the book. We're absolutely doing this.

- NOTE: If we do "32 Principles, 32 Values" or "32 Principles, 16 Values, 16 Anti-Values" then we can get WAY more representational power out of each 64 bit int.

- The entire book should be representable as 64 bits\*64 ints of information, aka 512 bytes. In other words, this book can literally be dd'ed to a boot sector.

- STRETCH GOAL: Make it fucking bootable. Should be possible (maybe) by reordering things, but probably not on x86 without some domas magic, and then it wouldn't be the book, but still, do things like this whenever possible.

### The 2 Books

- The paper book will be statically linked, without a single url pointing outside of it. It will reference the outside world, but have no concrete pointers to it. Everything will be "in-housed" or "vendored." Links to webpages will be transformed into screenshots and placed in the archaeology section at the back. Videos will be turned into printed quotes (which requires us to limit ourselves to videos that are essentially pointers to human speech, not complicated visual scenes or songs.) This ensures a complete and self contained book. This is the correct approach when the outside world is maximally unstable.

- The digital book will be dynamically linked. Namely, it will reference the outside world using the universal mechanism of our age: the hyperlink, a reference to this universal human blob we call the web. This version will be subject to all the problems that come with it. 

### The 2 Rings

- The book has two modes: Kernel Space (Ring 0) and User Space (Ring 3).
- Kernel Space is rarely seen, but it's where the nameless Authors speak in an interleaved stream of voices without attribution, bible style.
- User Space is the vast majority of the book.
- User space consists of a linear narrative, in the form of dialogues between two characters: 0 and 1.
- The entire book and all its content must be representable linearly on the page, in printed word, in the form of a conventional book.


## In the end, remember


![[when-theres-nothing-left-to-take-away.png]]