## shave and a haircut - two bits

![[shave-and-a-haircut.png]]

- Need to have 1 make this joke somewhere and 0 doesn't get it.
- Have 1 knock on the door of some directory in this pattern.

## 0 dies

The book of users:
- 0 dies at the end of the 0 testament.
- in testament one:
- 1 gives the sermon on the /mnt
- 1 talks to @2 to ask what 0 would say.
- 1 gives most of the principles by saying:
- "You have heard it said that abc. I say to you xyz."
- 1 finds 1self in charge of a number of followers.
- In 20YZ, the clock is changed to "A-1: In the year of our 1."


## 1 argues that the principle of explosion is a bug

1 argues that the Principle of Explosion is clearly a bug.
Says there's nothing desirable about making a system fragile like this.
Prevents us from considering distributed sources of axioms or theorems.
Prevents us from developing an import system with web-of-trust style axioms.
Prevents us from using standard logic in any distributed system with no top-down control.

To a first approximation, the view on inconsistency in mathematics and logic has been that it is the worst thing a system can possess. In rare cases when an alternate view is expressed, it is typically shrouded in mysticism, naivete, imprecisely defined terms, and the general sense that we're not having a serious conversation about mathematics or logic. While there have been fascinating explorations into the topic of paraconsistent logics (Graham Priest) and that mathematics that can be developed on top of those systems (Mortensen), the mathematical community at large has neither explored nor embraced these results, and our point here is not to suggest they do so. The aim of this file is to argue that any sufficiently robust formal system for representing mathematical truth must eventually reject the principle of explosion, while at the same time preferring more consistent to less consistent states.

Consider a large formal mathematics project like the Lean prover community's Mathlib. Consider the following thought experiment, and ask how we would like the resulting system to behave. Suppose we were able to inject a contradiction into the Mathlib repository.[^1] 

This might be done, for example, by formalizing the definition of Reinhardt cardinals and adding an axiom that such a cardinal exists. This fact implies the Kunen inconsistency due to its incompatibility with AC, but suppose somehow (for the sake of argument) the definitions to carry out the proof of the Kunen inconsistency have not been formalized.

For that or any other reason let's assume we've got a Mathlib with Reinhardt cardinals and Choice. This is an inconsistent system.

Question: Would we actually notice?

[^1]: While unbounded comprehension bugs used to be an easy way to get root on mathematics in past centuries, mitigations in the years since 1900 have made such exploits impractical, primarily due to type systems and restrictions on comprehension.


## 1 wants a Repl

Since 1 is a programmer, 1's not super articulate in words, so for the first part of the book (before lost+found) 1 is mostly a supporting character and is mostly listening and learning, but the knowledge flows in one direction.

In the two files:

- lost+found/1/5 (the technical part of infinity and Cantor)

- lost+found/2/5 (the technical part of logic and Russell)

0 starts to notice that 1 is extremely good at asking deep insightful questions _once things get technical._

0 is super impressed by how deep 1's questions are about technical stuff.

1 insists they're not deep, she's just a programmer, and she just wants a repl.

Since 1 grew up in the era of interpreted languages with interactive shells (as opposed to the older era of only compiled languages or the even older era of math) the idea is that she grew up expecting to be able to experiment with technical stuff and see how it works, because documentation is always crap even when it's good.

We've established that 0 loves the shell.

What we learn once we get to the technical dialogues in lost+found is that 1 needs a repl to feel like she understands something. A repl is the best teacher.

So whenever they're doing cantor's infinity stuff or first order logic or lambda calculus or whatever, 1 keeps wanting a repl so she can interactively see wtf the books mean because she feels like the books are vague and unclear.

Etc etc roughly this idea: 

0: Most of the time I think you don't know anything

1: Hey!

0: No no, it's a compliment.

1: Didn't sound like one.

0: I was gonna say most of the time it doesn't seem like you know anythi---

1: You don't need to say it again!

0: ---BUT once things get technical suddenly you seem like you know everything about this stuff---

1: That's because I don't know anything about this stuff. I'm a developer.

0: No I mean once things get technical, suddenly you seem to know everything about this stuff that's missing or incompletely specified.

1: I just want a repl!

0: Exactly! Because you're always wanting a repl on things, you're able to see things no one else usually sees.

1: Is a repl so much to ask?

0 and 1 then agree at the end of lost+found/2/5 (right before we get to Church Gödel Turing) that when it's time for the technical stuff, 0 will act as 1's repl, and let her try things interactively while 1 says "ok" or "error: explanation of why."

We eventually get:
- a repl on infinity
- a repl on logic
- a repl on lambda calculus 
- a repl on general recursive functions (for this one she has basically no questions and just goes "yeah this is obvious," but then hears what Gödel's theorem actually says and gets mad because it's basically doing the same kind of thing she was told earlier isn't allowed: mixing the formal language and the informal meta language.)
- a repl on turing's paper (for this one she also isn't particularly confused. once you have a repl on a turing machine you realize you're just using it to interactively write on paper, so the whole thing is pointless if it isn't automatic.)



## 0 and 1 argue about the Xi inscriptions

Something vaguely like this, but better:

In the Desert
Or: Numbers

```
src -> com -> bin
```

- src: I assume that's source. Like the original sources. Start there.
- com: I assume this is compare. Or maybe computer. Not sure.
- bin: What's bin? I assume that's you and me. Why? I dunno. Usually things go from src to dst. The first arrow starts at src. The final arrow goes to us, so we're the dst. They want us to know this was intended for us.

Are you sure? I thought this was just a diagram of how source code gets compiled.
How so?
Well obviously. I mean look: src is source, com is compile, bin is the binary output.

```
src -> obj -> bin
```

0: It's the same map as before, but now it says obj instead of com. Whoever wrote this must be trying to tell us something.

1: What?

0: Not sure. Could be a lot of things. Maybe obj means object.

1: Like object files? That fits pretty well with my ide---

0: No no, I mean "object", the verb. Maybe whoever wrote this objects to our interpretation of the previous message and they want us to know we got it wrong.

1: Ok, under this theory of yours, what's their objection exactly?

0: I don't know.

```
       com
src -> obj -> bin
2       U       2
       L@R
        D
     ☀️   🌕
        曰
```

0: There's another one!

1: What does it say?

0: Exactly what I predicted.

1: How is _this_ exactly what you predicted?

0: That they objected to our first interpretation and wanted us to know that the com in the original meant compile.

1: Isn't that what I sa---

0: Or maybe compare. Or commentary. Ok, I know the way now. We start with the the original sources. That's src. Then we compile and compare latter day commentary on those sources. That's com. Then we give our own interpretation, as 0 and 1. That's bin.

1: That's a bit of a stretch.

0: No it's perfect. The rest below that is consistent with my theory too.

1: _(Beyond skeptical)_ Explain?

0: Well the first map said `src -> com -> bin`. So just read the rest. Excluding the original content, the additions now say "object 2 U 2" and then "L@RD☀️🌕" which means "[I] object to you two," and then "@" is "at" so the word "L@R" is "latter", and obviously "D☀️🌕" is "day" and "曰" is an old chinese character that means "speech" or "words" or "sayeth." They're saying I object to you two and I want you to look at the latter day commentaries.

1: That was the dumbest thing I've ever heard.

0: Trust me. I've been here before. The L||D w||ks in mysterious ways.

1: I think you're dehydrated.

0: Ok if you're so smart what's your theory?

1: Same as my original theory The "com" at the top is "compilation".

0: How do you explain the rest?

1: Not sure. But I think it's probably a keyboard.

0: How is THAT a keyboard?

1: Look. The U L R D would be Up, Left, Right, and Down. They're even in the right places.

0: Ok well how do you explain the sun and moon?

1: I don't know. It seems like all this is some strange representation of a programmer. So maybe ☀️ and 🌕 are representing programming day and night. Or they could be the brightness keys on the keyboard. I don't know.

0: How do you explain the 2s? Or the @? Or the 曰?

1: I don't know. I don't have an explanation for those.

0: Well there we have it. My theory explains every bit. Yours has no explanation at all for three different pieces. I win by parsimony.

1: How is THAT parsimony?

0: My theory is simpler.

1: In what way? I feel like I have at least four diff--

0: Look it's not hard to come up with theories that explain part of the data. For example, I could come up with some nonsense theory like proposing that "com obj" refers to the "Component Object Model... a binary-interface technology for software components from Microsoft that enables using objects in a language-neutral way between different programming languages, programming contexts, processes and machines."

1: That doesn't seem totally implausible.

0: It's absurd. The L||D wouldn't be talking about Microsoft code, be realistic.

1: Is any of this realistic?

_(Narrator: 0 and 1 continue walking.)_

1: Found another one!

0: What does it say?

```
========================

  ld  so ld  so ld  so
src -> obj -> bin -> run
   exec . exec . exec
    cc  .  ld  .  a
       .o  ||  o.
           兔

    (ld: obj -> bin)
    (ld: bin -> run)
       🌕      ☀️
         山      三
           曰

========================
```

0: Um.

1: Um.

0: Run.

1: What?

0: It's telling us to run. RUN!
