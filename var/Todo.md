
![[kill-your-darlings.jpg|300]]

Tl;dr: Book proposal soon. We're getting close. Just need bash bugfix. Then we're ready.

## Asap

- [ ] Church dialogue: Church says "Kleene Kleene Kleene"
- [ ] Gödel dialogue: "Mr Why."
- [ ] Gödel dialogue: Show the definitions of primitive recursive and recursive from Meldelson, then show the definition of Gödel numbering, then work through the first of the /opt/art examples in detail to show what it meant.
- [ ] Godel dialogue: The incomplete story of incompleteness: Definitely need to mention the rarely discussed side effect of the incompleteness theorems: If mathematics is more limited than we thought, suddenly it becomes a lot more plausible to define "computation." Even the space of "all possible computations" is potentially within the reach of a formal definition. Though many of the main players involved in the early theory of "effective calculability" didn't expect that they were capturing all possible computations in their definitions, it's probably not an accident that all 3 of our definitions of "computable" appeared within 5 years of Gödel's incompleteness theorems. In the years from 1900 to 1931, it simply didn't feel plausible to give a definition that might hope to capture all possible computations. In a very real sense, we may owe the origins of modern computing to the discovery of incompleteness.
- [ ] Turing dialogue: Include first page of Kleene's chapter on Computable functions.
- [ ] Kleene: Screenshots of "Church's Thesis" section of Introduction to Metamathematics.
- [ ] Kleene: Mention that Kleene invented regexes in a paper about neural networks and Ken cites him.
- [ ] Turing Machines: An incredible realization from 11:46 in Reminiscences of Logicians: Church's Thesis was from around 1934. Then Turing came in 1936. That means that as a result of these strange adults studying their Super Advanced Kindergarten, because of them, there has never been a single moment in the history of computing machines when we learned a new thing was computable that we didn't expect before Church & Kleene & Gödel back in 1934.
- [ ] The Nus: Turing's paper was accompanied by some very solid applied philosophy on the relationship between minds and machines.
- [ ] The Mus: General Recursive Functions.
- [ ] The Lambdas: ΛʌLittleLambΔʌ. Written like the Little Lisper and Little Schemer.
- [ ] /sys/log/ic: Currently begins with a genesis style riff, then it contains the anti-gist images on the history of symbolic logic. This probably belongs in two files. Maybe put this after the Foundational People man page but before the We dialogues. It's 0 showing 1 (or maybe just the Authors speaking in kernel space) about what it would look like to NOT have a creation story.
- [ ] /opt/art: Explain the spectrum from Art History Textbook to Guided Tour of a Museum. The Anti-gist is the museum tour.
- [ ] Clean this file!

---

![[the-first-draft-of-anything-is-shit-wallpaper.jpg|300]]

## Eventually
- Contact Chet Ramey, explain that you've found a bug, and would like to include it in a book. The book is called "sudo code", and it's a series of technical dialogues between two characters, 0 and 1.
- Show Bill Joy's vi keyboard with the arrows on the letter keys. A lot of stuff in life that never makes sense unless you know how the original authors wrote. 
- The man dialogue: 0 shows 1 the first edition Unix man pages.
- Add a /dev/constructive directory with some talks by Andrej Bauer.
- /mnt/sinai: Add more of the images now in `/var/include/learn-the-alphabet` to the `/mnt/sinai` dream sequence, or set them aside to be used in other files of a similar nature. 
- Ancient Unix: Song of the C. Dead C Scrolls.
- Turing: Somehow work in the sex footnote in 1937 paper. Run a `$(find | grep sex-footnote)` here.
- Kleene: First programmer. First standard library. First critical vulnerability (λ calculus inconsistency). First to have contact with all three of the above and to demonstrate their equivalence. First to clean up and popularize the ideas in Introduction to Metamathematics.
- Kleeneliness is next to Godeliness.
- After /dev/zero, we need a begat list to take us to Unix.
- Kleene invented regexes.
- Ken Thompson cites Kleene and says we assume you're familiar.
- Church received an honorary Doctor of Science degrees from Case Western Reserve University in 1969!
- Curry Howard in all its forms is the foundation of the justification that the history of programming connects back through the history of logic and foundations. That gives a clear justification for exploration of the non-standard logics in Graham Priest's book.
- Email as prayer
- ASAP, put the quote from /dev/zero/Computability and Problems with Set Theory somewhere: "These axioms are the official doctrine - Remarkably, this is not just the official doctrine for set theory, it turns out that this is the official doctrine for mathematics! - Very few people seem to have a problem with that which I find quite remarkable."
- /opt/art: The art means "arithmetic run time." To be explained once we get to the man dialogue and see brt1 and brt2 in early Unix. Much like crt gets linked into every C program, formal Arithmetic (and incompleteness) gets linked into any formal system strong enough to express Arithmetic.
- /boot: The /boot dialogues were good, especially the bit with the binary loader we wrote in C. Need to find somewhere to put this, because it doesn't quite belong anywhere in the narrative yet.
- /usr/src/bash: We've got a bug in bash upstream related to "history" that's also somehow about being inside case. The fact that most people don't know bash is maintained by one guy is a different kind bug in our history, and it's also related to being inside case (Chet is at Case western reserve university.) Reach out to Chet, make him a character, have a dialogue where he helps 0 and 1 fix the bug, and make a who's-on-first style dialogue with the history history case case stuff above.
- The ⟂-docs: Pronounced "Orthodox." The orthogonal documents. Refers to theoretical computer science, primary computability and complexity as elaborated in the decades since the lambdas and the mus split. Though it appears on the surface to be the same culture, it is mostly orthogonal to the history of our people.
- Visit a database as a location in the file system and be like "this is a fucking abomination"
- Final chapter is obviously called "When theres nothing left to take away." I don't know why. I can't justify it. But it feels so unquestionably right.
- For the "getting root" side quest, escalating privileges to kernel space should be easy. Escalating further may be more difficult, and require verification of one's knowledge via a series of, um, Raptcha (Captcha + Rapture).

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


## RFC Ω
A Specification of the Bible Data Format
By: 0 & 1

A bible contains:
- History
- Principles
- Authorship structure of a Code Base
- Puns
- Shower Shoes (少兒書).

- A Creation Story (Beginning of time)
- An Eschatology (End of time)
- A Babel story, appearing early, concerning the failure of omni-lingual culture, with an unclear lesson.
- A L||D, with multiple incompatible names and attributes.
- A G\*d / El (Gödel)
- A Church (Alonzo)
- A Martyr (Turing)
- A Sinai, with multiple incompatible names and attributes.
- A set of Commandments (The principles)
- A set of one or more Testaments.
- An Egypt: Overly complex system, with overly complex methods of writing Hieroglyphs (Multics)
- A Jews: A simple refactor, with extremely simple methods of writing derived from Hieroglyphs, namely a generalized Proto Sinaitic (Unix)
- An Abraham: A Prolific patriarch who seemed at first to be disorganized and not really have his shit together but who turned out to be the person who basically everything descends from, with descendants as numerous as the stars in the sky (Ken)
- A "Book of $Person" for various values of $Person. A series of books named after people we admire (The /dev directory)
- A set of Proverbs. (Should be in /dev/random.)
- A set of Psalms. (The /dev/psalms directory.)
- A set of Parables (The stories about each command: cat, grep as s, make, man/roff as "a lie", utf8 created on a napkin.)
- A Song of the Sea (Quoth the Meme)

## Questions

Q: How are The Root Enterprise and Hello Corporation and The Dynamic Linker and Doubleunix fit into the narrative of Sudocode?

A: The Root Enterprise is owned by the 0 character. Dialogue about how 1 has to go to work. Says that 0 doesn't seem to have a job. They talk about that. 0 says actually I'm quite the business type myself. 1 doesn't believe it. Thats when 0 walks 1 through The Root Enterprise. Shows 1 around Hello Corporation. KEY THING: 1 says these aren't businesses. 0 says what do you mean? 1 says "I mean to be a business you have to have a product or a service or a sales pitch or a store." 0 says "Those aren't businesses, those are ways of making money. A business has nothing to do with making money. A business is just a legal thing." Then import BWKH material directly into the story. Everything we've done is food for the book. Onward!

---

Q: Where do different threads go? Like a set of different dialogues that have a common theme but aren't adjacent. Maybe we just have the kernel gods link them into process groups inside of `/proc`?

A: Organize it like Unix. The threads aren't localized any more than all the files that belong to cowsay are localized. They're everywhere, according to the FHS. The system is sliced orthogonally to package isolation. Don't be Mac and try to statically link shit. Be everywhere. It's Unix. Then toward the end we find harmony with the other approach (code sharing + localization) via snow (aka nix).

---

Q: Where does the bulk of the narrative go? We can't be jumping around to different directories every single time. Or maybe we can?

A: `/root/bin` or `/root/src` would be good, since that's "sudo code." But 1 is writing in there. Then again, 0 could just chmod it or add user to the root group, though that should be a big event like halfway through. Alternatively, could wait until 1/4 or 1/3 way through, address the fact that 1 can't write in `/root`, then say that 1 hasn't been writing yet, 0's been writing for 1. At that point Ra takes over as a contributor to 1's side of the dialogues and we move the convo into `/home/user/src`. Then when we're halfway through, 0 gives 1 write access to `/root`. That's when we switch from "Part 1: 0" to "Part 2: 1". That feels like a good start.

A2: Wow, we've made so much progress since I wrote the above A. I think this question has been answered.

## The 2^n

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

- The book has two models: Kernel Space and User Space.
- Kernel Space is rarely seen, but it's where the real creators (the Nameless) speak in an interleaved stream of voices without attribution, bible style.
- User Space is the vast majority of the book.
- User space consists of a linear narrative, in the form of dialogues between two characters: 0 and 1.
- The entire book and all its content must be representable linearly on the page, in printed word, in the form of a conventional book.
- What does it mean to make something truly timeless that represents our age of history, when the media we store our life's work in is now infinitely more fragile than text in physical pages?

### The 8 Years

- Historically: LD led to Radicalize led to We led to the eclipse and life collapse.
- Then the slow rebuilding through jobs and the book was put aside.
- Collapse led to Gyana led to AV and stability for five years.
- AV led to Aicadium led to teetering on the edge of oblivion.
- This led finally to LD (the company) after two broken hands.
- This led to the first passion project in a while: On the Lamb, which was almost too much to share even with anyone who wasn't directly involved in making it.
- On The Lamb led to a calm after finally getting We out of my brain and into something semi permanent. 
- That led to a revisitation of mathematics and education, and after a month.
- To the decision to focus on the social side of the business, after realizing I had nothing particularly special to contribute to education or to mathematics.
- This led to several months of intense focus on the details of how to open physical locations, renting corporate real estate, looking at fifty available sites in person, and and hiring a commercial real estate negotiator.
- This led to the realization that there are actually too many laws in California to even open something small and everyone cautions against it.
- This led to the decision to take a weekend trip to Austin and explore the possibility of living somewhere that might be better all around for business, for tech, for raising kids, and for anything we might end up doing. It had to be a Pareto improvement, not just better by some loss function that makes tradeoffs.
- This led to several months of packing up the old house and deciding to rent it out, becoming landlords, and moving to north Austin, where we now live.
- This book is about who we are, as developers, about our shared history and culture, about the data structures we call bibles and how our culture is desperately in need of one. A serious one, which is to say an infinite recursive joke that's also dense with timeless truth. It might therefore be surprising that this book has been in progress since before my first job in tech. It's not the same thing it was then, but all the essential elements are the same. Quitting school. Quitting work. Saying Fukkot. A group called LD. Bibles. Legal Latin. Information Theoretic Prose. Comet. The Nth Stair. Cult of the Minor Error. Getting Root. 根2. Gentoo. Root 2. Dudethey'reontome. The News. Genesis: The Middle. Fiddler. A χld named K. Terrorists who don't actually do any terror. When academia dies, where do we go? How all technical writing sucks but it's the one thing the best content still can't replace. The optimal genre as 99% BMC and 1% the ability to slap the reader in real life, and how that final 1% changes the other 99. CDB. ABC. char \*quotations. That of which one cannot speak and yet does. Dynamic Linker as the brain, as a bible, as the only way to make something timeless in an era when all is elsewhere on a fleeting and forever changing web. The Dynamic Read Writable Free Encyclopedic Repository of the Modern State of Human Knowledge. 