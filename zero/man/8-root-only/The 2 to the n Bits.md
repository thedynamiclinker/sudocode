## The 2ⁿ

### The 32 /etc/groups

We currently have 31 groups in /etc/group, including the null ones like the betas and the bible authors (aka the alephs.)

We just need one more, and we can assign one bit to every tribe and use a single 32 bit int to describe _any topic in computing or mathematics!_

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
