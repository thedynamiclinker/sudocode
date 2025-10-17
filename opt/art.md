
> _I had a running compiler and nobody would touch it. ... They carefully told me, computers could only do arithmetic; they could not do programs._
> -Grace Hopper

---

0: ---read it. Just enough to realize what's going on.

1: Why are we in a file called "art"?

0: And once you do, you realize it's all simple and trivial and you didn't need to read it after all. But once you're there, the "reading" stops being hard work.

1: `/opt/art`? Is that like pop-tart?

0: That "terrifying math" you thought you were looking at turns out to be hilariously simple and fun.

1: What the hell are you talking about?

0: It starts slow.

![[mendelson-001.png]]

1: What's---

0: You flip back because you missed the definition of EPL or FL or ARGp or EIC or Gd or qt or MP or minus-sign-with-a-dot-on-top or _my god why are there suddenly so many abbreviations?!_

1: Don't ask me, I dunno.

![[mendelson-002.png]]

0: Once you flip back and load each definition into your memory and then flip back-forward and re-read each thing, it makes sense. It all makes sense.

1: Not to me.

![[mendelson-003.png]]

0: It's funny once you get it.

1: _(Sarcastically)_ "Ha ha math."

0: That's why it's funny. See this isn't even math.

![[mendelson-004.png]]

1: It looks like math.

0: It's programming.

1: What?

0: The first programming ever done by a human on Earth.

1: Ok I'm listening.

![[mendelson-005.png]]

0: Now look, earlier I was a bit unfair to Ada Lovelace.

The things she was doing pretty clearly count as programming, by any definition.

But she and Babbage weren't our ancestors.

In the sense that it's not useful to trace our lineage back to them.

There was no community of people who their work influenced at the time, and which led as a result to the theory of computation and eventually to the machines we use and the thing called programming that we so-called programmers all do both for fun and at work.

They were convergent evolution by means of a one-off macro-mutation.

The same can't be said of these pages right here, or the hellishly-confusing-looking symbols all over them.

These pages, and these squiggles.

This is the first code ever written.

And there's a direct line of descent from this to the field we call home.

1: What and when is this? And why are you calling it "programming"?

![[mendelson-006.png]]

0: This is 1931.

14 years before ENIAC.

9 years before Bletchey Park, the Bombe, Enigma.

5 years before Turing's paper on computable numbers where he defined the machines that now bear his name.

So what's so special about the hell squiggles on these particular pages?

Why is it helpful to call them "programming"?

Let alone the first programming ever performed by a human on earth?

That's a tall order.

But suspend disbelief for just a moment.

![[mendelson-007.png]]

1: This is definitely hell math.

0: Look at all the 2s. See the powers? Those are bit masks. Multiplication of one power of two by another shifts it left.

The $\wedge$ symbol means "And". Look how many $\wedge$ are there.

As scary as it looks, it's just a really long sentence.

1: What's it about?

0: You can guess what some parts mean without needing to be told.

$Trm(u)$ means u is a "term."

$Fml(w)$ means w is a "formula."

$Subst$ is substitution of some expression for some free variable in some term.

See that $\mu$ in the image right below this?

1: Where?

0: At the top, to the right of the equals.

That's called the "mu operator."

It's an odd sort of function defined in terms of evaluating some other function and then incrementing an integer until a specific condition is met, which may never happen.

Sound familiar?

1: Not really.

0: It's a while loop.

1: Oh!

0: "Term. Formula. Variable. While."

1: So what's going on?

![[mendelson-008.png]]

0: He's building a compiler.

1: What?!

0: 5 years before Turing.

14 years before the first time that "computer" meant "machine."

During this era, "computer" meant "person."

This thing that's happening here, it couldn't possibly be further from "the thing that mathematicians do in proofs."

![[mendelson-009.png]]

1: Why not?

0: Mathematicians aren't this precise. They have no reason to be. Mathematicians take for granted the existence of the human mind and all its intuitions, and it's the human minds of themselves and their colleagues that serve as the gold standard of what counts as sufficiently convincing in their proofs.

The foundation of "Normal Mathematics" is the human mind.

Whatever THIS is, it's taking place well below that, and the human mind is not a dependency of this code in the same sense that it is in normal mathematics.

1: Say more words like dependency and code. It makes me feel like I'm following.

0: That's why _our people_ are not the same culture as the Mathematicians, though there's often overlap in terms of the departments where they live.

1: Who's our people? You still didn't explain.

0: But culturally speaking, most mathematicians find Foundations to be a strange and largely irrelevant field with little impact on their groups and rings and fields.

![[mendelson-010.png]]

And looking all all these symbols, I can almost sympathize.

Almost.

![[mendelson-011.png]]

1: Ok yeah that's a seriously intense amount of twos.

0: But the mathematicians are engaged in a much stranger and less well-defined activity, one which---

Ooh ok forget that, this next part is fun.

1: Did you just interrupt yoursel---

0: Yes. Here, come down and look.

![[mendelson-012.png]]

0: See that $LAX(y)$ up above and down below?

1: What about it?

0: Remember $\wedge$ is "and".

So unsurprisingly, $\vee$ is "or".

So that term $LAX(y)$ is just saying: y is a Logical AXiom if it's Axiom 1 or Axiom 2 or ... Axiom 5.

Tell me this isn't programming.

![[mendelson-013.png]]

1: Ok I'm like half conviced. Still don't know what it's saying.

0: To be fair, mathematicians say "Thing 1 or Thing 2 or ... Thing 5" plenty too.

What's different here is that sentence has to be _implemented._

We can't get away with just saying it in natural language.

We've decided, in advance, on a formal language and a formal theory.

And thereafter, we're required to write things in _that_.

Or else the compiler won't work.

Back to the compiler.

![[mendelson-014.png]]

He just implemented `if` in the image up above.

1: Who is "he"?

0:  No `else`. Else is a luxury after all.

1: Am I invisible here? Answer me zero.

![[mendelson-015.png]]

0: All this is happening before there's even an agreed upon definition of "computable."

1: So how is it "programming"?

![[mendelson-016.png]]

0: When you see the word "primitive recursive" in the image below,

read that as "We as a community don't know what Turing completeness or computability are yet...

...but *whatever* we mean by computable, everyone can agree it's _at least_ this."

1: What's "this"?

![[mendelson-017.png]]

0: They used to call it "effectively computable," "effectively calculable," or just "effective."

You'll hear "effective procedure" too, back then.

When you hear that, it means this:

1: Holy... Look at this one down here.

![[mendelson-018.png]]

1: "I'm a two collector, look at all my twos!"

0: "Look, we all know lots of things are computable. We can't use that word to describe the things we're defining, because we have no evidence that the stuff we're defining _covers everything that can be computed by any method whatsoever._"

Before the discovery of the trinity,

1: The trinity?

0: This incredible three-way equivalence that led to the Church-Turing thesis, nobody involved in Foundations had any idea how timeless their definitions of "computation" would turn out to be.

Not a single person involved expected that the word "effective" was effectively describing "any sequence of steps that could ever be performed by a physical system anywhere."

So far, almost 100 years later, that seems to be what they defined, back then.

Without knowing it.

In three equivalent ways they thought were different.

1: Three ways of what? Details, zero. Are you just telling this story to yourself or what?

0: We'll get there eventually, in time.

![[mendelson-023.png]]

0: Ah, Robinson Arithmetic.

1: Ok yeah he's just talking to himself.

0: We'll get to Q eventually too.

![[mendelson-025.png]]

0: Quick preview:

![[mendelson-026.png]]

1: Ok that sounded like programming until the RR. What's Q?

0: Q is a crippled, weak, basically mathematically useless theory, which is also somehow able to express anything recursive aka computable.

So if there's nothing above "computable," but Q is "mathematically useless," then what exactly is mathematics?

1: ...Uncomputable? Haha.

0: Yep.

1: What?!

0: I won't spoil that particular story by giving the details now, but I promise most mathematicians don't know the answer to the question of what their field is.

1: How is mathematics "uncomputable"?

0: Story for another day.

For now, we're almost at our destination.

1: You mean there's a point to all this?

0: Ready?

1: No.

0: Here we go.

![[mendelson-027.png]]

Fast forward.

After all, incompleteness isn't the point.

Just a tour, for now.

![[mendelson-038.png]]

Beweisbar.

1: God bless you!

0: If you know you know.

![[mendelson-039.png]]

Henkin sentence.

Fast forward.

![[mendelson-040.png]]

1: ... ¬ Bew haha.

0: What?

1: Ascii gun fight.

0: You're dumb.

![[mendelson-041.png]]

1: Box box box.

0: And here's the second one.

1: Second what?

![[mendelson-042.png]]

1: Ooooh. That's the guy you said people talk about too much right?

0: Yeah.

1: But you're talking about the same---

0: Don't question me child. Show some formality. Time for Church.

![[mendelson-043.png]]

1: That was seriously the stupidest joke of all ti---

0: Before long, we'll get to Church.

Just driving by for now.

![[mendelson-046.png]]

1: Hah there's---

0: Don't.

Look down, not up. We've finally arrived.

1: Arrived where?

0: In the picture below. That's the three way equivalence.

1: I understand like maybe 2% of this.

0: That's ok. Enough driving for now.

![[mendelson-047.png]]

0: Time to pop the stack.

1: Finally a sentence I understand!

![[mendelson-060.png]]

0: Remember those sigmas and pis!

![[mendelson-062.png]]

1: _(Looking up and down quickly as the pictures fly by)_

0: They'll be involved in the unravelling of all things, before long.

1: Wait what?

![[mendelson-063.png]]

0: When we get to Reverse Mathematics... (

1: What's---

![[mendelson-064.png]]

0: A Gödel-sized revolution that went almost entirely unnoticed...

1: Reverse Mathematics?

0: ...both by mathematicians and by the popular books.

More than any other reason, I left mathematics and eventually found computing because of that.

1: You used to be in mathematics?

0: Who do you think you're talking to?

1: Oh, haha. Right.

0: Story for another day.

1: You say that about everythi---

0: Pop the stack.

![[mendelson-066.png]]

)...

goto: [[lib/ld.so#Pop t'art|ld.so]]
