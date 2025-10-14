## Church's Language

### Or: What Church was thinking
### Or: Church's First Try
### Or: Untyped λ-calculus
### Or: Premathematics of λ
### Or: Be My Church
### Or: BMC

> _I'm an extremely annoying employee. I always ask why about everything._
> -Grace Hopper

0: Ok so in Church's system, everything is functions.

1: You've mentioned this already, but I still don't know what you mean.

0: How do you mean?

1: I mean if everything is functions, what do they take as inputs?

0: Functions.

1: What do they return as outputs?

0: Functions.

1: Zero?

0: What?

1: ... That's insane.

0: I know it feels that way at first. But it's not so bad once you implement numbers and booleans.

1: Sure sure, but WHY?

0: Why what?

1: Why do this at all?

0: Why are we doing it?

1: No why was Church doing it? I want to know what was going on inside his head, or at least what might have been. What would make a person say "Y'know what I'm gonna do today? Make a system where 0 and 1 are actually functions." Like that's not a normal behavior and it's not a natural way to think. So I'm curious what was going on in this guy's head that would make him do something like this.

0: Perfect question! Ok so, by the time Church is writing, formal theories had been a thing for a while. ZFC had already done formal set theory. PA had already done formal number theory. It's not unreasonable to think something like "Look guys, those theories you made are cute and all, but the foundations of mathematics or even reasoning itself shouldn't be just whole numbers or unordered collections. The foundations of mathematics should be something more primitive.

1: What's more primitive than those things?

0: Well there are infinitely many natural numbers. And that's not a problem in itself, but we'd like our foundations to be something inherently finite. I mean when a mathematician proves stuff about the natural numbers by induction, they do it with only a finite amount of time and food and paper and pencils and erasers. Finite everything. Foundations should be like that. So it's fine that the natural numbers are infinite, but they're not finite in the same obvious way that the mathematician with the paper is finite and only doing finite stuff. If we truncate the natural numbers at any finite level and say "There are no natural numbers above ten million" or whatever, any mathematician would rightly feel like we'd done a violent ugly hack that made the natural numbers less of what they are. But there's no such feeling when a mathematician uses only finitely many pencils or finitely many sheets of paper. We have no problem with that, and we'd be disturbed if either was infinite. So in that sense natural numbers are way too big to be foundations.

1: What about sets? Sets can be finite.

0: True! But all versions of set theory that have ever been proposed as foundations are much more infinite than the whole numbers are. They tend to all include a sentence that says "ω exists."

1: You mean ω like Cantor's first size of infinity?

0: Well in this case it means "The set of natural numbers," but those are actually the same thing.

1: How are those the same thing?

0: Well no finite number is big enough to be the smallest infinite number. So the set of all natural numbers ends up being the same thing as "the smallest infinite number" in that system. Anyways things are even worse in set theory than in number theory, because there tends to be another axiom that says "If a set X exists, then so does P(X), the set of all its subsets." And that P(X) turns out to always be a bigger size than X, even if X is infinite. So any formal theory that had these two things together grows an infinite number of different sizes of infinity, each larger than the next.

1: I remember. So what was Church thinking?

0: Well taking together both the fact that (i) the natural numbers have an inherent inability to be made finite without it feeling like an ugly hack, and (ii) set theory has such a wildly irresponsibly number of infinite things that it's not clear how it got invited to the foundations party... taking those two things together, you might end up thinking what Church was thinking.

1: _(Narrative voice)_ "So what was Church thinking?, 1 asked yet again."

0: That we need a "Formal Theory of X" for some better X than just X = numbers and X = sets.

It should be something fundamentally finite.

Maybe there's infinitely many Xs for whatever this sought after X type thing is, but it should be possible to _make_ the theory only about finitely many objects made of inherently finite stuff, and finitely many operations on those things. We should be able to "finitize" the theory without it feeling like an awful hack in the way it would if we said 1 million is the largest natural number.

1: "Without it feeling like"?

0: Yeah, what's the problem?

1: You seem to be suggesting that Church wanted something finite, but his foundation for wanting that was "feelings."

0: Of course. I mean I never knew Church specifically, but that's a totally normal way to think when you're doing mathematics.

1: The more you talk about math, the less I understand what it really is.

0: Good. That means you're listening. So anyways if you thought all the thoughts above, you might end up doing what Church did, so let's do our best to get inside his head.

We're looking for some type of X where we can build a "Formal Theory of X" that doesn't feel fundamentally broken if we don't have infinitely many of them, or if the guts of each one aren't infinite either.

Sure there might be infinitely many Xs for this sought after value of X, but there shouldn't NEED to be.

We're looking for something like that.

Something fundamentally finite or at least something that we could force to be finite without it feeling like the hack job of truncating $\mathbb{N}$. 

Our X should be more general than numbers or sets. 

Something that's hiding in plain sight all around us if we could just open our eyes and see what X is.

Something that's painted all over every sentence in every area of mathematics, both the discrete areas like number theory and combinatorics and graph theory, and the continuous areas like calculus and geometry and topology.

Our X should be staring us in the face whenever we open any textbook, and when first hear someone say what it is we should feel a feeling of "Damn. Of course. Why didn't I think of that?"

1: Seems reasonable. What kind of thing is like that?

0: You tell me.

1: Functions?

0: Functions.

## How to Write Good

### Or: Formal Function Theory
### Or: Church & Kleene
### Or: Be my repl


0: Ok, so now do we understand why a person might do something like this in the first place?

1: Totally.

0: Ok so Church's notation for functions was λx---

1: You don't have to explain lambdas. I'm a professional developer.

0: Great! So with that notation in hand, Church defined the natural numbers like this:

0 := λf. λx. x
1 := λf. λx. f x
2 := λf. λx. f (f x)
3 := λf. λx. f (f (f x))
4 := λf. λx. f( f (f (f x)))
succ := λn. λf. λx. f (n f x)

1: Back up, I'm not ready for that yet.

0: You're not ready for the definition?

1: No.

0: What do you mean?

1: I mean that definition makes no sense to me. Back up to the part where they derive that.

0: Derive what?

1: The definition.

0: Church doesn't do that in this paper.

1: Ok can we find a textbook that does?

0: Sure, let's go look.

(Narrator: 0 and 1 go find some other textbooks on λ calculus.)

0: This one doesn't have it either.

1: Same with this one.

0: Y'know I've actually never seen the kind of derivation you're asking for before.

1: Well what did Kleene use as a repl? 

0: He didn't have a repl.

1: How did he know if something he tried worked or not?

0: I think Church was his repl.

1: Well we can't do that! He's not here. And his paper isn't finished.

0: Don't blame Church, this is just how mathematicians write.

1: I thought he was a foundational person.

0: He is. I just mean if you publish in academic journals you have to write that way. It's basically required. You can write about almost anything. All the journals consistently care about is that you write in an academic sounding way.

1: You're not allowed to write good?

0: You're definitely not allowed to write good in journals. They think that's wrong, and it's only right to write "well." Usually they care less about what you say and more about how you say it. And that makes it basically impossible to explain certain things, like what sorts of thoughts you'd have to have and what sorts of mistakes you'd have to make before you arrive at the definitions that you eventually use to prove stuff from. You're allowed to explain the part after the definitions, because it's possible to write that part well. But you're not allowed to explain the part before the definitions, at least not the parts that can only be explained good. If a thing can only be explained good and not well, you're not allowed to explain that thing.

1: You're not allowed to explain things?

0: You're allowed to explain things, but they have to sound formal.

1: I thought most mathematics wasn't formal.

0: No not "formal" as in formal languages. The journals don't care about formal languages and they certainly don't expect you to write in a formal language. They just want you to write in formal language.

1: I'm gonna scream.

0: I mean fancy English. Or natural language. They just want it to sound fancy.

1: What's the point of that?

0: I don't know, it's a bug that tends to show up in institutions that are culturally overvalued. Whenever a system or group has more social status than it deserves, it always starts talking fancy and insisting the big words matter and anyone who doesn't use the right words is inherently less sophisticated. It's a defensive position. It's not my cup of tea, but one can see where they're coming from.

1: That's fucking ret\*rded. Be my repl.

0: How so?

1: I'll write stuff. You tell me if it's a syntax error or not. Then when I plug things into functions, you evaluate them.

0: Ok.

1: x

0: (Says nothing)

1: So?

0: What do you want me to say?

1: I dunno, say yes if it's ok, or error if it's an error. Is that ok?

0: yes

1: x

0: yes

1: x y

0: hmm

1: That's not very repl of you.

0: I'm thinking.

1: About what?

0: I don't know if that's syntactically valid.

1: I thought you knew this system.

0: I mean, you have a free variable, and then you plugged it into another free variable. They're both functions. Cuz everything's functions. But neither of them has any lambdas in it. So idk. Whether or not we decide that that's syntactically ok, either way, we can't reduce it any further. It just sort of sits there.

1: Ok, what about this.

λx. x

0: That's ok.

1: What about λx: 3

0: There's no 3 yet.

1: Oh right. How about this?

λx. y

0: That's ok.

1: You're supposed to say yes.

0: Ok.

1: λx. λx. x

0: error

1: Why?

0: Try plugging something into it.

1: What something?

0: Idk, like 3.

1: I thought there was no 3 yet.

0: Treat it like a variable.

1: What?

0: I just mean plug something into that thing you just defined. Something that doesn't feel like a variable, so you don't get confused.

1: 

(λx. λx. x)(3)

= λ3. 3

0: You can't do lambda of three.

1: Why not?

0: 3 isn't a variable.

1: I thought you said treat it like a variable.

0: Ok nevermind. Use a.

1:

(λx. λx. x)(a)

= λa. a

0: Now plug a into this: λx. λy. x

1: 

(λx. λy. x)(a)

= λy. a

1: What's was the point of that?

0: You got different things. In the (λx. λx. x)(a) example, the a got captured by the second lambda thing.

1: What?

0: Umm, one sec, I need to think.

1: Ok this isn't helping. Here let's back up.

0: I don't think we can back up further than this.

1: Of course we can.

0: How?

1: You said this was the first programming language right?

0: Yeah.

1: So obviously there's a bit before this.

0: Before what?

1: Before using it. I'm using the repl. That's WAY past the beginning of a language!

0: What comes before x and λx. x?

1: Implementing the language dummy.

0: Oh right.

---

0: Where should we start?

1: Definitely not at numbers. That definition from earlier scared me.

---

goto: [[1 - Gödel's Beginnings]]