## Link
https://www.youtube.com/watch?v=hlyQjK1qjw8&authuser=0

## Clips

### I'm gonna spare you the first five minutes of most talks about parallelism about how we're stuck with multicores. If you want to program a parallel computer, would you rather start with a language whose very fabric is by default sequential, by mutating state, or a language that's by default parallel.
start = 0:00

### @Q: In the end, something declarative will win.
start = 0:57

### @Q: There is no parallelism without tears.
start = 1:20

### The standard concurrency primitives.
start = 2:00

### If you're going to write a parallel program, you need a cost model more than you do in serial code because inter-process and inter-machine boundaries are suddenly everywhere.
start = 2:17

### This cost model stuff is too difficult to leave to the system.
start = 2:50

### In the olden days, we thought maybe we're going to have a big computer with lots of distributed memory, and we'll implement some kind of distributed shared memory over it. You can't do that cuz you can't hide the fact that some addresses are closer to you than others. And if you try to ignore it, you just write slow programs.
start = 2:58

### @P: Planning is pretending. Don't want to make you decide up front which parallelism model to use, because you might discover along the way that you need a different one.
start = 4:38

### Our plan for world domination in Haskell is to make a sort of single linguistic framework that somehow allows you to use different programming paradigms for programming parallel computations in the same language.
start = 5:03

### @Q: How does it work? Well look at the types.
start = 8:13

### The Lambda People talk and think like mathematicians: It's important for reads not to commute with writes.
start = 9:30

### @P: Concurrency Primitives are Broken: The Standard Solution is Wrong. Locks and Condition Variables
start = 12:37

### @P: Best Practices Aren't: The Standard Solution is Wrong. Locks and Condition Variables. Concurrency primitives are broken.
start = 12:37

### @Q: Locks are absurdly hard to get right.
start = 13:15

### Programming basics are often publishable results in computing journals and conferences once you add concurrency. That's how hard concurrency is.
start = 14:05
end = 14:35

### @Q: It tells you something about concurrency that you can go from undergraduate project to research result, just by saying "Oh, and I'd like to do this at the same time."
start = 14:35

### Transactional Memory: Nobody except Haskell can do this. Not even the famously brilliant evil geniuses of other languages.
start = 14:42

### @Q: This is the way to solve problems, by defining them out of existence. You can't deadlock because there are no locks.
start = 15:27

### The fuck it approach to complexity. If errors are rare and stochastic and you can break work into small enough chunks, all errors can be handled and solved by just throwing your work away and trying again. Then concurrency just works.
start = 15:40

### @Q: It has type ugh ugh
start = 20:00

### Monads are little side effecting computations.
start = 20:10

### @P: Its worth being picky about names.
start = 20:24

### Make it impossible to forget.
start = 20:50

### @P: Small is good.
start = 25:21

### @P: Planning is pretending. Simon surprised he only has twenty minutes left.
start = 26:02
