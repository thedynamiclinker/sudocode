- Import is a within-process method of code re-use.
- It does not work between processes, except via `fork()`.
- Because [[Concurrency Primitives are Broken]], `fork()` often can't be mixed with threads.

Todo: Explain exec vs import and the intermediate level abstraction of all programming languages.

Todo: Babel puzzle belongs here.