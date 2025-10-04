
---

Above all else, you must do this:

## N + P = Complete

Thought: The N and P volumes.

- Volumes: N & P

- Testaments: (-1), (0), (+1)

- Explanation: If one volume is too few, and three is too much, and we have to do two volumes despite the existence of three testaments, then call volume 1 "N" (Negative), and volume 1 "P" (Positive), reach Ken and Unix and the BC/AD changeover where Unix time hits zero at precisely the moment we switch from one volume to the next, and then maybe THAT'S the optimal way to divide this. I actually like this idea. The BC / AD division. Consider this seriously. May work for publishers (less importantly) and (more importantly) for The Narrative.

- IMPORTANT: This also lets you place Ken at the center where the 0AD date/time changeover is, rather than just placing him somewhere less important.

- This is it.

- This is the way.

---


![[the-first-draft-of-anything-is-shit-wallpaper.jpg|300]]

Tl;dr:
- Book proposal soon.
- Just need to submit the bash bugfix.

Soon:
- Add "sign of the dollar" password hint somewhere in or around /etc/group. Phoenician Qoph, Phoenician Giml.
- Need to draw this in Excalidraw or by hand. Fonts aren't good enough to do it properly.

Fundamentally Important and Will Also Be Fun To Write:
- /mnt/sinai needs to be a dialogue.
- The little lambs can't absorb raw information without a shepherd, aka entertainment, aka a dialogue.
- Write one.
- And give the ~~Authors~~ Λ vibes.

## Church
- [ ] Import video notes from what is mathematics vault.
- [ ] Rewrite "The Little Lambda" from scratch.
- [ ] Friedman 1997 "The Formalization of Mathematics" actually belongs here. After Hirst, say Hirst's advisor was Friedman, and cover the opening of The Formalization of Mathematics. In this paper, he lays out the problem with current foundations, and describes what we need instead. Everything he describes sounds exactly like what Lean started to become around 20-25 years later. But at this point, don't mention that. At this point, just mention that Hirst's advisors were Friedman and Simpson, and both Friedman's and Simpson's advisor was Gerald Sacks, whose advisor was Rosser, whose advisor was Church. Here we can see Sacks talking to Kleene about Church.
- [ ] Kleene Rosser paradox ALSO showed that Haskell Curry's combinatory logic from 1930 was inconsistent! The lambdas definitely have more severe bugs while they're getting up and running, but fewer as they mature. Curry simplified this paradox in 1942, and it has also been called Löb's paradox.

## Turing

- Turing's definition of computation is not inherently a "machine" any more than Church or Gödel's. But there is an important sense in which it's more fundamental than the others.
- Turing's definition of computation is quite literally just a finite number of case statements and three system calls: read, write, and move.
- read takes no arguments.
- write takes any single character as an argument.
- move takes a 1 bit argument that says whether to move left or right.
- Turing writes these as:
- write: P0 writes 0, P1 writes 1, Px writes x, E writes a blank aka erases the square. Maybe this is a different system call.
- move: L moves left 1. R moves right 1.
- read: Turing doesn't express the read system call as code. The read is assumed to happen automatically, and be provided in a "machine register" of sorts that he calls the current symbol.

## Constructivism
- _Proofs are computations with partially defined values._


## lost+found

- [ ] Finish lost+found. It doesn't need to be perfect. We're close enough to satisfying the 2D constraints that I think it's worth sticking with it. The "corruption" analogy seems to work well as an excuse to make that directory a bit anarchic. Anything that's unclear after lost+found should be clarified with a commentary on it in `/lib/tor.a` or `/usr/share/doc/tor.a`

- [ ] Church's definition from first principles: How would you come up with Church's idea if it didn't exist yet? So far we'vegot formal Arithmetic from Peano, and formal Set Theory from Zermelo and friends. What if you thought everyone was doing it wrong? Or at least missing something? What's more fundamental in mathematics than natural numbers or sets? Well, it wouldn't be crazy to say "functions." So what if everything is functions? Now how would you come up with the Church numerals? Well in every formal system with one type, you always have to encode things. (1) The von Neumann encoding in ZFC because ZFC doesn't have built in integers. (2) Even first order arithmetic has to "encode" the integers in a sense: 0 is the only built in. 1 is S(0). 2 is S(S(0)). 3 is S(S(S(0))). So how do you encode the integers if all you have is functions? Well Peano Arithmetic already did it! We just saw it. 3 is "call a function 3 times." And voila, you've got the Church numerals. So we miss the point a little by calling it Lambda Calculus. We've got "Formal Number Theory" and "Formal Set Theory." We should call Lambda Calculus "Formal Function Theory."

- [ ] Gödel's definition from first principles: To get inside Gödel's head, we have to recognize his definition as a different approach to Formal Function Theory, one that's much more like a standard axiom system than Church's. After all, Church said he never had other mathematicians to talk to about his interests because he was the only one in his field. Church's work is much more "Ex Nihilo" than the other two, and much more minimal as a result.

- [ ] Turing's "Formal Theory of Paper" and why it convinced the others: To get inside Turing's head, we have to recognize what he was doing as "Formal Paper Theory." Turing's theory is the axiomatic development from first principles of what can be done with paper and a pencil. Church and Gödel both made "Formal Function Theory." Turing made "Formal Mathematician Theory" by making "Formal Paper Theory," which is how he convinced the others that he (or all of them) had captured anything that could be computed by any means. Turing's paper is always described as being about computing machines. What no one says is that he actually formalized the theory of "Making marks on paper." That's how his result is in a sense more conceptually viral than the other two. If you formalize functions, it's easy to think you've missed something about computing in general. If you formalize the process of making marks on paper, it's very hard to worry that you've missed something.

- [ ] /mnt/sinai: Maybe this contains a dialogue, and the point of it is for the Authors to show 0 that the same thing can have different names (Sinai and Horeb maybe being the same mountain), or different things can have the same name (El and YHWH being called "Lord"). 0 then realizes how to structure the creation story of computing from the source documents.
- [ ] /mnt/sinai: There needs to be enough in here or elsewhere to allow for the privesc via /sbin/sudo. Some hints are in here. Others can be elsewhere. The images now in /var/include/learn-the-alphabet are relevant.

## /lib/tor.a

- [ ] Use Richard Elliot Friedman's "Commentary on the Torah" to show the reader what a strange writing style we're actually dealing with.
- [ ] In this file, make it clear that lost+found was our first attempt at the lost art of bible authorship.


- [ ] Harvey Friedman "formalization-of-mathematics.pdf" needs a chapter SO BAD that I think it maybe matters more than anything else in the book. This is a revolution larger than Gödel that has been entirely ignored because people don't notice things when they matter. People notice things when noticing them makes their life better somehow. We'd like to clarify that this isn't a criticism and we remain agnostic about the "somehow." But people noticed Gödel because it made their lives better, and people haven't noticed Friedman because it doesn't. But he loves mathematics, at least as much as Gödel. He's more extroverted than Gödel in none of the obnoxious ways and all the positive ways. And he's completely not a public figure in any way, even though he's an incredible teacher. In other words there's a man who falls into all the cracks that allow a person to be maximally valuable to history while being minimally noticed. So fuck that shit. He gets a chapter in the bible. Several probably. Because he matters more than docker or postgresql or any of the dumb shit we in computing focus on. So here's Harvey. He belongs in our history. He's already made a place for himself in some history. But it's the history of foundations of mathematics, and nobody pays attention to foundations of mathematics these days. Here's Harvey. (Begin commentary on "The Formalization of Mathematics." Take the screenshots on your phone. It's a masterpiece, all in monospace, and it looks better in phone format. Get this published. Otherwise no one outside the obscure foundationals is gonna hear.)

- [ ] Walter Pitts of McCullough and Pitts is a fascinating character. Used to crash Bertrand Russell lectures at age 15. Was homeless when he presented Carnap with an annotated copy of his book. Carnap looked around forever trying to find who this kid was. Pitts was extremely eccentric and avoided any situation that would require him to sign his name. He was aware of Leibniz's ideas about a universal language or universal computing machine, and he used that and Turing's ideas as the basis for the first ever paper on neural networks.

- [ ] Gödel dialogue: "Mr Why."
- [ ] Gödel dialogue: The incomplete story of incompleteness: Definitely need to mention the rarely discussed side effect of the incompleteness theorems: If mathematics is more limited than we thought, suddenly it becomes a lot more plausible to define "computation." Even the space of "all possible computations" is potentially within the reach of a formal definition. Though many of the main players involved in the early theory of "effective calculability" didn't expect that they were capturing all possible computations in their definitions, it's probably not an accident that all 3 of our definitions of "computable" appeared within 5 years of Gödel's incompleteness theorems. In the years from 1900 to 1931, it simply didn't feel plausible to give a definition that might hope to capture all possible computations. In a very real sense, we may owe the origins of modern computing to the discovery of incompleteness.
- [ ] Gödel dialogue: General Recursive Functions: Show the definition of Gödel numbering, then work through enough of the encoding of formal arithmetic into itself that the definition of General Recursive Functions becomes clear.

- [x] Kleene: Kleeneliness is next to Godeliness.
- [ ] Kleene: Screenshots of "Church's Thesis" section of Introduction to Metamathematics.
- [ ] Kleene: Mention that Kleene invented regexes in a paper about neural networks and Ken cites him.

- [ ] Turing dialogue: Mention Turing becoming Church's graduate student.
- [ ] Turing dialogue: Include first page of Kleene's chapter on Computable functions.

- [x] The Lambdas: ΛʌLittleLambΔʌ. Written like the Little Lisper and Little Schemer.
- [ ] Clean this file!

## Outline of the Testaments
Testament -1
- Begins: Jan 1 1930
- Ends: Jan 1 1970
- Church: Untyped and Simply typed
- Gödel: General Recursive Functions.
- Turing: Automatic Machines.
- After dev zero we do etc group.

Non-Testament (-½)
- Begat list.
- Mention McCarthy.
- Mention Lisp and Scheme.
- Mention various systems.
- Begat to Ken.

Testament 0
- Begins: Jan 1 1970
- Ends: Sept 17 1991
- The μ part of 0 Testament: Unix & BSD era, C.
- The λ part of 0 Testament: ML, System F.
- Reverse Mathematics founded by Harvey Friedman in 1975, 1976. Gerald Sacks (from Reminisces of Logicians) was his advisor.
- Genesis is Bell Labs Unix.
- Exodus is BSD.
- Leviticus is ???.
- Numbers is Unix wars.
- Deuteronomy is GNU.
- GNU Project, and was publicly announced on September 27, 1983, on the net.unix-wizards and net.usoft newsgroups by Stallman. Software development began on January 5, 1984, when Stallman did his own Exodus from his job at the Lab so that they could not claim ownership or interfere with distributing GNU components as free software.
- GNU never got a functioning kernel (despite lots of hype about Hurd) so GNU software existed in diaspora, forming the core of the userspace of other systems, but never reimplementing the kernel from scratch.
- When Ken Thompson was asked how he learned to program, Thompson stated, "I was always fascinated with logic and even in grade school I'd work on arithmetic problems in binary, stuff like that. Just because I was fascinated."

Non-Testament (+½)
- Begat list.
- Everything that will be relevant in (+1) that we didn't cover in (0).
- MS-DOS was initially released on August 12, 1981, with the release of PC DOS 1.0 for the IBM PC. Microsoft's version, titled MS-DOS 1.25, was released in August 1982, after Microsoft licensed and adapted the 86-DOS operating system from Seattle Computer Products in July 1981.
- Microsoft released Windows in 1985, a year before moving its headquarters to Redmond, Washington. By the late 1980s, Microsoft was the world's largest personal-computer software company.
- Python began Dec 1989.
- Guido first released it in 1991.
- This was Python version 0.9.0.
- The "Unix wars" occurred roughly between 1985 and 1995, a period of intense conflict and fragmentation among competing vendors trying to establish a standard for the Unix operating system. The period was marked by numerous Unix variants and the inability to agree on a unified standard, ultimately leading to commercial difficulties for many participants and setting the stage for the rise of free Unix-like systems like Linux.
- The Unix shell Bash was launched on June 8, 1989 by Brian Fox as part of the GNU Project. It was created in 1987 as a free software replacement for the Bourne shell (sh). 


Testament +1
- Begins: Sept 17th 1991
- End of Time (Date): 19 Jan 2038
- End of Days (Date): 03:14:07 UTC
- End Prediction: World continues.
- End of Era: Not specified.
- The μ part of (+1) Testament: Linux, Python.
- The λ part of (+1) Testament: Haskell, Coq, Lean, Nix.
- Reverse Mathematics (1999). Stephen Simpson's Subsystems of Second Order Arithmetic. Gerald Sacks (from Reminisces of Logicians) was his advisor.

- Constructive school mentioned.
- Eventually we get to now.
- The lambdas create Dependent Types.
- The Lambdas create Nix.
- Now Lambdas & Mus reuniting.
- Lots of the Mus who care are lost.
- The Lambdas kept our history alive.
- Perfection is achieved not when there's nothing more to add, but when there's nothing left to take away.

---

![[kill-your-darlings.jpg|300]]

## Eventually

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
- [ ] When theres nothing left to take away.

- [ ] Put these "document fragments" somewhere or reimplement them in Excalidraw.

![[lost-and-foundations.jpg]]


## begat list

If it helps - The "begat" list - How to fast forward the story to 20XY

- [ ] Cantor: Shows vulnerability.
- [ ] Russell: Exploits vulnerability.
- [ ] Hilbert: Organizes bounty.
- [ ] Trinity: Church, Göd, Martyr.
- [ ] Apostles & Epistles:
  - [ ] Steve Kleene (next to Gödeliness). Cleaned up Gödel's "first code ever written" and disseminated the Gödel and Turing senses of computation to the world. Original programmer in Lambda calculus under Church.
  - [ ] John νon Neumann (Neumann János Lajos) the superhuman. Gave a definition of Ordinals that superseded Cantor's definition. Axiomatized Cantor's set theory for his PhD thesis. Studied under David Hilbert. Persistent self doubts, thought Gödel would be remembered with Pythagoras while he would be forgotten. Nobel Laureate Hans Bethe said "I have sometimes wondered whether a brain like von Neumann's does not indicate a species superior to that of man." Go to Accolades on Wikipedia page. Quote: von Neumann "was the first to have a vision of the boundless possibilities of computing, and he had the resolve to gather the considerable intellectual and engineering resources that led to the construction of the first large computer"
- [ ] Trinity begets three spirits: λ, μ, ν.

- [ ] λ thread: Language, Large, Lisp.
- [ ] Church & Steve influence McCarthy.
- [ ] MacCarthy creates Lisp (λ, ν)
- [ ] Lisp inspires ISWIM and ML. (λ)
- [ ] ML inspires the Haskell group (λ)
- [ ] Haskell group: Simon, Philip. John Backus as God. The New Testament of the lambda.
- [ ] Coq, Idris, Agda: the theorem provers.
- [ ] Finally: λμν merge in: Lean. The foundational people begin to reach the mathematicians. Mathlib is born. Kevin spreads the word to the normal mathematicians. Tao converted, begins to use @2 (ν) in Lean (λ) to explore pure mathematics founded on a non-human mind (μ).

- [ ] μ thread: Metal, Micro.
- [ ] Göd & Martyr influence Von Neumann. Martyr is Turing with bits of Post and Gödel. Mental illness and madness mixed with brilliance.
- [ ] ENIAC built in 1945. "However, instead of the stored-program computers that exist today, ENIAC was just a large collection of arithmetic machines, which originally had programs set up into the machine by a combination of plugboard wiring and three portable function tables (containing 1,200 ten-way switches each)."
- [ ] Von Neumann meets Herman Goldstine, creator of ENIAC, in 1944. Writes " First Draft of a Report on the EDVAC." Builds IAS machine from 1946 to 1951. The μ family is now under way.
- [ ] Unix thread and Ken live here.
- [ ] Most of the book probably takes place here.
- [ ] Finally: λμν merge in: Nix and Wnix. The classical μ system (Unix) meets the lambda school to become NixOS and combined with @2 creates Wnix.

- [ ] ν thread: Neuro, New.
- [ ] Began with Turing's paper on the Imitation game.
- [ ] Led to McCullough and Pitts (Pitts was a logician). Pitts was an amazing character and should be covered. See personal life and death section of wikipedia page. He's clearly one of the Foundational People.
- [ ] Rumelhart and McClelland PDP.
- [ ] Geoff Hinton's 40 years in the desert.
- [ ] Finally: λμν merge in: Unclear. We have the clear meeting of μ and ν with Alexnet, transformers, and GPT, once it becomes practical to run these programs on conventional machines with the addition of GPUs. Tensorflow is now moving in a more functional direction with Jax, but not sure how to make that timeless. To be continued.


## shave and a haircut - two bits

![[shave-and-a-haircut.png]]

- Need to have 1 make this joke somewhere and 0 doesn't get it.
- Have 1 knock on the door of some directory in this pattern.


---

## Mathematics vs Foundations

The mathematicians are puzzle people. That's not fair, that also have theory builders which are a form of foundational people who are also very much mathematicians. But we're not that. Since the beginning, our people have been focused on studying, formalizing, automating thought. We've been focused not on groups or rings or fields or Banach spaces or simplicial homology but on _the mind._ Some have gravitated more toward the brain as hardware, others have been drawn to the computational structure of the emotions and motivations, others to the formalization of the more precise forms of reasoning that the mind is capable of and how to abstract them and pull them out of the mind and into the printed word or into the operations of a physical machine. But this culture is and always has been a distinct culture from mathematics. We are not puzzle solvers, though we solve many. We are not focused primarily on any content domain except that domain that is the mind and all of its operations and capabilities. From ancient greek logic to modern artificial intelligence, there is one type of mind that has been drawn to these field for the same reasons throughout time. The foundational people. And our object of study is every operation of the mind. From mundane tasks at unremarkable programming jobs to the purest and most exalted examples of our field, from Church Gödel Turing to the modern transformer architecture, we have always looked inward and fought to pull that which is inside of us out. Every truth inside us, every computation, every emotion, that is the internal that we seek to make external. From our tendency to metacommentary to the most formal logical systems, we are the children of the mind. The mind is our foundation. And all the methods by which the mind might be pulled out of the brain and transpiled in whole or in part onto the media of paper or machines is the reality we want to understand. What is this thing inside of ourselves and inside the people we love? Humanity, the mind, and people, is our foundation. And we are the foundational people.

---

## RFC Ω
### A Specification of the Bible Data Format, by 0 & 1

#### Required Authorship
- Unclear Authorship.
- Authorship structure of a Code Base.
- A division into multiple testaments.

#### Required Style
- A bombastic and serious writing style with zero humor.
- A playful and unserious writing style with a frequent use of humor, especially puns.
- A verbose and bureaucratic writing style that skips no steps even when it would considerably improve the flow.
- A brief and vague writing style that often skips steps to improve the flow.

#### Required Genres
- Nonfiction history.
- Fiction nonhistory.
- Type 1 Morality: Practical principles for everyday life, delivered calmly.
- Type 0 Morality: Rants, Jeremiads, and Denunciations of behavior considered unwise, immoral, or destructive. (e.g., Isaiah)
- Epistles: Letters to a specific person or group.
- Compilation: A series of books named after people we admire (The /dev directory)
- Proverbs: A collection of assorted wisdom by various authors.
- Psalms: Poems, songs, prayers.
- Parables: Brief memorable stories with a lesson. (The stories about each command: cat, grep as s, make, man/roff as "a lie", utf8 created on a napkin.)

#### Required Content
- A God / El (Gödel)
- A Church (Alonzo)
- A Martyr (Turing)
- A L||D, with multiple incompatible names and attributes.
- A Sinai, with multiple incompatible names and attributes.
- A Horeb, see above.
- A Babel story, appearing early, concerning the failure of the ambitions of an omni-lingual culture, with unclear lesson.
- An Egypt: An overly complex system, with overly complex methods of overly complex writing (Multics)
- A Jews: A simple refactor, with extremely simple methods of writing derived from Hieroglyphs, namely a generalized Proto Sinaitic (Unix)
- An Exodus: A story in which the generalized Jews find themselves unhappy in the generalized Egypt, and then eventually leave in search of a generalized Promised Land, once the higher-ups kill their children (Exodus 1, Bell Labs killing Multics).
- An Abraham: A Prolific patriarch who insists he doesn't want to job, seems at first to be disorganized and not really have his shit together but turns out to be the person who basically everything descends from. Descendants as numerous as the stars in the sky. (Ken)
- A Lucifer: A fallen angel, with a name meaning something universally positive, and a personality marked by an abundance of pride. (Best Practices)
- A Creation Story or beginning of time, containing a narrative in which everything began.
- A Beginning of Time at which calendars are set to zero, and which is distinct from the beginning of time in the creation story. (Unix Epoch)
- A set of Commandments (The principles)
- An Apocalypse or Eschatology (End of time)
- A Revelation: A final chapter which appears on the surface to be completely insane, while in fact being completely hilarious and well written.
- A line in the final chapter where the best character refers to themselves by (1) a name often used to describe the worst character, and also (0) the name "root".
- A line in the final chapter where the Authors say "Don't change it, it's perfect."

#### Requirements for the Jews
- Beards.
- Man pages.
- Sources written in an ancient language.
- Written language often omits vowels. (Abjad)
- Written language born in a refactor.
- Written language born by deleting complexity.
- Written language's descendants include virtually everything.
- Modern members learn original source language but often don't speak it daily.
- Writings now incorporated into the majority of modern systems, either by direct descent or cultural reimplementation.
- Culturally dominant despite dwindling absolute numbers.

#### Requirements for the Jews V2
- Aquatic mascot (Fish, Penguin)
- Empire hates you early on. (Romans, Balmer)
- Eventually the Empire adopts you. (Constantine, WSL)
- Explosion of distros, dramatically more than V1 culture.
- Cultural continuity with V1 is prioritized over direct historical descent. (Linux imports Unix culture but not vice versa.)
- Has Cathedral, has Bazaar.
- Conquers basically the entire world.
- Often dismissed due to occasional holier than thou attitude among less devout members (The btw meme.)
- Answers to any problem can be found in text files.
- Subset of members claim V1 worships devil.


---

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

---

Q: Where do different threads go? Like a set of different dialogues that have a common theme but aren't adjacent. Maybe we just have the kernel gods link them into process groups inside of `/proc`?

A: Organize it like Unix. The threads aren't localized any more than all the files that belong to cowsay are localized. They're everywhere, according to the FHS. The system is sliced orthogonally to package isolation. Don't be Mac and try to statically link shit. Be everywhere. It's Unix. Then toward the end we find harmony with the other approach (code sharing + localization) via snow (aka nix).

---

Q: Where does the bulk of the narrative go? We can't be jumping around to different directories every single time. Or maybe we can?

A: `/root/bin` or `/root/src` would be good, since that's "sudo code." But 1 is writing in there. Then again, 0 could just chmod it or add user to the root group, though that should be a big event like halfway through. Alternatively, could wait until 1/4 or 1/3 way through, address the fact that 1 can't write in `/root`, then say that 1 hasn't been writing yet, 0's been writing for 1. At that point Ra takes over as a contributor to 1's side of the dialogues and we move the convo into `/home/user/src`. Then when we're halfway through, 0 gives 1 write access to `/root`. That's when we switch from "Part 1: 0" to "Part 2: 1". That feels like a good start.

A2: Wow, we've made so much progress since I wrote the above A. I think this question has been answered.

---

Q: What does it mean to make something truly timeless that represents our age of history, when the media we store our life's work in is now infinitely more fragile than text in physical pages?

---

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

## Memories

It's seriously wonderful to be back in real "writing" mode again.

There have been a couple things that felt vaguely like this since Burn Math Class, like the Radicalize era and On The Lamb, but neither of those were technical writing about a technical field where I got a chance to explore how a given set of technical content mixes with basically every possible genre on the planet.

The "bible" theme has been so central since early Radicalize in 2017 because it's the only way to explain _why_ it might be useful to combine essentially every conceivable genre in a book without justifying that decision with something postmodern and dumb.

Back to writing.

Just wanted to put this here.

![[writing-mode-activated.jpg]]
