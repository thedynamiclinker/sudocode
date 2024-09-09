Once you reduce your problem to a sufficiently abstract form, you reach a point where you begin to see countless concrete examples of the same problem structure in other fields.

Suppose you're on a tech team. Person A wrote some code that reads a small static file, say 20kb, and ships that file in the code repository, pushing the result to the main branch of version control. 

Person B sees this design pattern and reacts in disgust. Data shouldn't be in the codebase, B says. The Right Thing, B claims, is to put it in a central database. This is scalable, says B, and everyone nods in agreement, including A.

What just happened? 

Todo:
Walk through the examples of:
- A course syllabus (Distributed to everyone.)
- A personal bookshelf. (Each person owns different books, but they're always nearby).
- A public library. (A large central location, a few miles from your house. To store your daily todo list or your personal bookshelf here is absurd. The only reason this is centralized is because making copies of it all is hard.)

Programmers generally agree that the root of all evil is shared mutable state.

Well that's a database.

It's shared mutable state.

Shared mutable state isn't always bad, but it's a tragedy that we should take pains to avoid whenever we can. Something to be used reluctantly, with some grumbling, even in cases where we give in.

In these cases we have to follow the principle of "Many readers xor One writer."

Proceed to examples of a bulletin board, where no one makes you read it and people sometimes post over each other's things.

Or a billboard, where you broadcast certain information (make it shared), in exchange for a fee (the right to mutate must be earned), but nobody is required to read what you wrote, nor required to execute the action (e.g., "Buy our stuff")

---

Fields with finance semantics.

Three are adversarial games with zero sum payoffs between you and your opponents, where your opponents are strangers who can't see your reasoning or behavior, and you can't see theirs, though there may be occasional information leakage.

The best ideas in any field with finance semantics are what we might call "inverse marketing."

Standard marketing is presenting a positive image. Inverse marketing is presenting a negative image. 

In finance, gold mining, oil exploration, etc, the best "moats" come from ideas that look bad/childish/dangerous/naive on the outside, while being simple and reasonable below the surface.