```
					RFC Ω:    Specification of the Bible Data Structure

	                Authors:  0 & 1
                    Location: The Filesystem
                    Date:     echo $(date | awk '{print $2, $3}') 20XY
                    Contact:  root@thedynamiclinker.com
		                      user@thedynamiclinker.com

---

INTRODUCTION

	What are bibles?
	
	Without a doubt, these books are the most viral memes of all time.
	They are also the most enduring, the most translated, and the least
	understood.
	
	But what are they, as a genre?
	
	The answer would at first appear to be "every genre."
	These documents contain every style from poetry, to prose,
	to quite literally spreadsheets of who begat who, at what age,
	and how long they lived after.
	
	Bibles contain some of the most timeless narrative content ever written
	(e.g., the J and E sources), and some of the most unreadable thickets of
	legalese you're ever likely to encounter outside the terms and conditions
	of a modern corporate software update (e.g., the P source, Leviticus).
	
	Against that background, we believe it is useful to start from a clean slate.
	To forget everything we think we know about bibles, and to undertake an
	objective dispassionate engineering analysis of them, with the aim of
	understanding what these books actually are, and what a person or group
	of Authors would have to be thinking in order to write a sentence,
	a paragraph, a chapter, an epistle, a gospel, a book, or the entire
	library we call a bible.
	
	Therefore, this analysis focuses primarily on the Authors. We do not
	concern ourselves with the truth, either religious or historical, of any
	of these documents. Rather, we ask what the Authors were up to, and what
	motivations a human on earth would need to possess in order to write these
	books with the form and content the Authors chose to include in them.
	
I. Case Study 1: Genesis and Creation.

```


---

Include an abridged "best of" version of [[The Aspiring Bible Author's Guide to the Torah]] here, as an informal analysis of the genre written by 0 and 1. This RFC document should begin with an Informal Engineering Analysis aiming to determine "What Bibles Are" by analyzing existing examples of the genre.

For the format of an RFC, see: https://datatracker.ietf.org/doc/html/rfc1

---

## Requirements

Bugs
- Problems with world as it now exists.
- Condemnation of broken things in the existing world.
- Also known as Jeremiads, rants, or venting.
- Found in Isaiah and elsewhere.
- See the `bugs` directory for examples.

Principles
- Solutions to the problems of the world.
- Practically useful if-then rules for everyday life.
- Direct didactic instruction to teach the reader about good and bad.
- See the `principles` directory for examples.

Covenant
- Conquest reframed as a gift from the higher ups.
- A gift to one group of something that is not theirs to begin with.
- This is primarily a rationalization for something that was going to happen anyway.
- See the `covenant` directory for examples.

Legends
- Semi-historical stories from the past of our people.
- See the `legends` directory for examples.

Parables
- Short memorable stories with an implicit moral lesson.
- See the `parables` directory for examples.

Cut, Copy, Paste, & Refactor
- The most important tools in any Bible Author's toolbox.
- Though this feature is lesser known than the others, it is a universal feature of all bibles.
- Reimplementation, commonly known by the slight misnomer "redaction" in biblical archaeology circles, refers to the process by which all bibles are written.
- This process consists of chopping up previous bibles and stitching them back together in a way you like better.
- While on the surface, chopping up several bibles and using the pieces to suit your needs may appear sacreligious to un-devout to some readers.
- Interpet this activity how you will. Regardless, it is unambiguously the one thing all bibles and all sub-bibles within bibles share in common.
- Examples include but are not limited to:

- The Torah: created by cutting up and interleaving the J & E & P sources, adding glue code as needed.
- The Epic of Gilgamesh: cut together from at least five independent Sumerian poems, some of which may date back to the Third Dynasty of Ur around 2100 BC. 
- The book of Isaiah: Scholars believe this "bible within the bible" was written by at least 2 or 3 Authors, often referred to as Proto-Isaiah, Deutero-Isaiah, and Trito-Isaiah.
- The book of Matthew: Written about as long after the Jesus story as the gap between the current book and Unix version 1. Matthew is structured as a mirror image of the Torah, divided into five main parts that each reflect the same themes as the corresponding books in the Torah. Matthew appears to have been cut together from prior sources including the book of Mark, and a lost document referred to as Q that some have argued was the later discovered Gospel of Thomas, though consensus on this point is not universal.
- The Quran and the Christian bible, which import Abraham and other Old Testament themes from the Torah.

The רꞀΠΓг genre (RPG)
- A linear narrative that one is more or less forced through.
- Plus optional side-quests scattered around, for the curious.

## Examples

In this section we provide a set of reference implementations as a pedagogical illustration of how a required class of the bible genre might be instantiated in a concrete instance of this class, in a standard compliant manner.

Reference Implementations:

A Golden Calf
- Syntax: Paragraph.
- Semantics: False Gods.
- Example: Exodus 32.
- Docstring: "These are your gods."
- Summary: A story in which the normies are found to be worshipping something retarded.
- Reference Implementation: [[These Are Your Gods]]

A Lucifer
- Syntax: One-Liner.
- Semantics: Ambiguous fall from grace.
- Example: Isaiah 14:12.
- Docstring: "Morning star, evening star."
- Summary: An extremely brief sequence of sentences, too short even to be called a paragraph, in which a character never mentioned before, with a name that means something positive like "Light" or "Love" or "Grace" is mentioned as having been among the highest before an ambiguous fall event, bringing the character to a place among the lowest. No indication is made of how the character's story ends or whether we like them. The character should also somehow be known for "bringing light" to people.
- Reference Implementation: [[Light Bringer]]

A Song of the Sea
- Syntax: Vaguely Poetic, Prehistoric.
- Semantics: Ancient song from the earliest strata of the codebase.
- Example: Exodus 15.
- Docstring: "Submerge egypt, Emerge world."
- Summary: A war song describing the sea as a force that defeats our enemies but not our people.
- Reference Implementation: [[zero/man/5 - genres/psalms/Song of the Sea|Song of the Sea]]

---

## RFC Ω: Old Notes

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
- A Lucifer: A fallen angel, with a name meaning something universally positive, and a personality marked by an abundance of pride.
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

Note: The gospels were written about the same time after the Jesus story as the gap between Unix version 1 and 20XY.
