- Import is a within-process method of code re-use.
- Exec is a between-process method of code re-use.
- The import method of sharing code does not work between processes, except via `fork()`, and because [[Concurrency Primitives are Broken]], `fork()` "can't" be mixed with threads.
- The import method of sharing code does not work between languages, except via awkward foreign function interface APIs.
- Tl;dr: Unix got it right.

---

Todo: Explain exec vs import and the intermediate level abstraction of all programming languages.

Todo: Babel belongs here.