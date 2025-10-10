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
