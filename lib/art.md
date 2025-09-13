
TODO:
- [ ] Make this file a proper dialogue.

---

- The "arithmetic run time" file.
- To be explained once we get to the man dialogue and see brt1 and brt2 in early Unix.
- Then explain crt1.o, crti.o, crtn.o, and finally why this file was called art.

![[man-001.png]]

---

1: Why are we in a file called "art"?

---off slow and you're not sure what the textbook is doing. Then it increases in steady drumbeats until you're staring at this book, this book that you've made a policy of reading every word of so far, and you find yourself thinking "What am I supposed to do now?" I can't actually read all this. I mean Christ. The density.

It's unlike anything you'll ever see in a textbook upstairs. But eventually out of something like stubbornness or OCD, you read it. Just enough to realize what's going on. And once you do, you realize it's all simple and trivial and you didn't need to read it after all.

But once you're there, the "reading" stops being hard work. This "terrifying math" is hilariously simple and fun.

It starts slow.

![[mendelson-001.png]]

You flip back because you missed the definition of EPL or FL or ARGp or EIC or Gd or qt or MP or minus-sign-with-a-dot-on-top or _my god why are there suddenly so many abbreviations?!_

![[mendelson-002.png]]

Once you flip back and load each definition into your memory and then flip back-forward and re-read each thing, it makes sense.

It all makes sense.

![[mendelson-003.png]]

It's funny once you get it.

See this isn't even math.

![[mendelson-004.png]]

It's programming.

The first programming ever done by a human on Earth.

![[mendelson-005.png]]

Now look, earlier I was a bit unfair to Ada Lovelace.

The things she was doing pretty clearly count as programming, by any definition.

But she and Babbage weren't our ancestors.

In the sense that it's not useful to trace our lineage back to them.

There was no community of people who their work influenced at the time, and which led as a result to the theory of computation and eventually to the machines we use and the thing called programming that we so-called programmers all do both for fun and at work.

They were convergent evolution by means of a one-off macro-mutation.

The same can't be said of these pages right here, or the hellishly-confusing-looking symbols all over them.

These pages, and these squiggles.

This is the first code ever written.

And there's a direct line of descent from this to the field we call home.

![[mendelson-006.png]]

This is 1931.

14 years before ENIAC.

9 years before Bletchey Park, the Bombe, Enigma.

5 years before Turing's paper on computable numbers where he defined the machines that now bear his name.

So what's so special about the hell squiggles on these particular pages?

Why is it helpful to call them "programming"?

Let alone the first programming ever performed by a human on earth?

That's a tall order.

But suspend disbelief for just a moment.

![[mendelson-007.png]]

Look at all the 2s.

See the powers? Those are bit masks. Multiplication of one power of two by another shifts it left.

The $\wedge$ symbol means "And". Look how many $\wedge$ are there.

As scary as it looks, it's just a really long sentence.

You can guess what some parts mean without needing to be told.

$Trm(u)$ means u is a "term."

$Fml(w)$ means w is a "formula."

$Subst$ is substitution of some expression for some free variable in some term.

See that $\mu$ in the image right below this?

That's called the "mu operator."

It's an odd sort of function defined in terms of evaluating some other function and then incrementing an integer until a specific condition is met, which may never happen.

Sound familiar?

It's a while loop.

"Term. Formula. Variable. While."

So what's going on?

![[mendelson-008.png]]

He's building a compiler.

5 years before Turing.

14 years before the first time that "computer" meant "machine."

During this era, "computer" meant "person."

This isn't "mathematics."

It couldn't possibly be further from "the thing that mathematicians do in proofs."

![[mendelson-009.png]]

See mathematicians aren't this precise. They have no reason to be. Mathematicians take for granted the existence of the human mind and all its intuitions, and it's the human minds of themselves and their colleagues that serve as the gold standard of what counts as sufficiently convincing in their proofs.

The foundation of "Normal Mathematics" is the human mind.

Whatever THIS is, it's taking place well below that, and the human mind is not a dependency of this code in the same sense that it is in normal mathematics.

That's why the Foundational People are not the same culture as the Mathematicians, though there's often overlap in terms of the departments where they live.

But culturally speaking, most mathematicians find Foundations to be a strange and largely irrelevant field with little impact on their groups and rings and fields.

![[mendelson-010.png]]

And looking all all these symbols, I can almost sympathize.

Almost.

![[mendelson-011.png]]

But the mathematicians are engaged in a much stranger and less well-defined activity, one which---

Ooh ok forget that, this next part is fun. Here come down and look.

![[mendelson-012.png]]

See that $LAX(y)$ up above and down below?

Remember $\wedge$ is "and".

So unsurprisingly, $\vee$ is "or".

So that term $LAX(y)$ is just saying: y is a Logical AXiom if it's Axiom 1 or Axiom 2 or ... Axiom 5.

Tell me this isn't programming.

![[mendelson-013.png]]

To be fair, mathematicians say "Thing 1 or Thing 2 or ... Thing 5" plenty too.

What's different here is that sentence has to be _implemented._

We can't get away with just saying it in natural language.

We've decided, in advance, on a formal language and a formal theory.

And thereafter, we're required to write things in _that_.

Or else the compiler won't work.

Back to the compiler.

![[mendelson-014.png]]

He just implemented `if` in the image up above. No `else`. Else is a luxury after all.

![[mendelson-015.png]]

All this is happening before there's even an agreed upon definition of "computable."

![[mendelson-016.png]]

When you see the word "primitive recursive" in the image below,

read that as "We as a community don't know what Turing completeness or computability are yet...

...but *whatever* we mean by computable, everyone can agree it's _at least_ this."

![[mendelson-017.png]]

They used to call it "effectively computable," "effectively calculable," or just "effective."

You'll hear "effective procedure" too, back then.

When you hear that, it means this:

![[mendelson-018.png]]

"Look, we all know lots of things are computable. We can't use that word to describe the things we're defining, because we have no evidence that the stuff we're defining _covers everything that can be computed by any method whatsoever._"

Before the discovery of the trinity, this incredible three-way equivalence that led to the Church-Turing thesis, nobody involved in Foundations had any idea how timeless their definitions of "computation" would turn out to be.

Not a single person involved expected that the word "effective" was effectively describing "any sequence of steps that could ever be performed by a physical system anywhere."

So far, almost 100 years later, that seems to be what they defined, back then.

Without knowing it.

In three equivalent ways they thought were different.

We'll get there eventually, in time.

![[mendelson-023.png]]

Ah, Robinson Arithmetic.

We'll get to Q eventually too.

![[mendelson-025.png]]

Quick preview:

![[mendelson-026.png]]

Q is a crippled, weak, basically mathematically useless theory, which is also somehow able to express anything recursive aka computable.

So if there's nothing above "computable," but Q is "mathematically useless," then what exactly is mathematics?

I won't spoil the story by giving the answer now, but I promise most mathematicians don't know the answer to this question of what their field is.

That's a story for another day.

For now, we're almost at our destination.

Ready?

Here we go.

![[mendelson-027.png]]

Fast forward.

After all, we're not covering this in detail here and now.

Just a tour.

![[mendelson-038.png]]

Beweisbar.

If you know you know.

![[mendelson-039.png]]

Henkin sentence.

Fast forward.

![[mendelson-040.png]]

Box box box.

![[mendelson-041.png]]

And here's the second one.

![[mendelson-042.png]]

And finally, we come to Church.

![[mendelson-043.png]]

Before long, we'll come to Church.

Just driving by for now.

![[mendelson-046.png]]

And finally we've arrived where we intended to.

Squint at the picture below, that's the three way equivalence.

Enough driving for now.

![[mendelson-047.png]]

Time to pop the stack.

![[mendelson-060.png]]

Remember those sigmas and pis!

![[mendelson-062.png]]

They'll be involved in the unravelling of all things, before long.

![[mendelson-063.png]]

When we get to Reverse Mathematics... (

![[mendelson-064.png]]

A Godel-sized revolution that went almost entirely unnoticed,

both by mathematicians and by the popular books.

More than any other reason, I left logic and mathematics (and eventually found computing) because of that.

Story for another day.

Pop the stack.

![[mendelson-066.png]]

)...
