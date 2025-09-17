1: Are you making fun of me?

0: Yes. This stuff is important to the story. It's silly to toss everything in /opt just because you think someone somewhere might think it's a digression.

1: But you're doing the same thing now.

0: Exactly.

1: Anyways, you were gonna explain why calling us "The Foundational People" isn't just another example of the tribalism thing from /opt/names.

0: Right. Ok, let's start at the beginning.

1: Listening.

0: _(ahem)_

_(Narrator: 0 clears 0's throat.)_

0: Once upon a time, in the late 1800s, a guy named George segfaulted mathematics.

1: Segfaulted mathematics?!

0: Ok well not quite. More like he got root on the universe.

1: _Got ROOT on the UNIVERSE?!_

0: Ok that's not quite right either. His name was Georg Cantor.

---

1: Was he the first Foundational Person?

0: No no, he's not one of ours. Not to exclude him. He could have used a good hug and some proper friends, and I would have loved to know the guy. But in his heart, Cantor was a mathematician. He thought like a mathematician, and he wanted to be accepted by the mathematicians.

1: Why wasn't he accepted?

0: Well, he made the mistake of doing some mathematics.

1: What's wrong with that?

0: Well this mathematics was different. Or more accurately, it was the same. See what Cantor did was to use standard mathematical reasoning, the kind that was generally accepted by the mathematical community, to show that if you accept the standard types of definitions and proofs that are common in mathematics, then you're basically forced to accept that infinitely many different sizes of infinity "exist." There's a whole hierarchy of infinite "numbers" up above the normal numbers like 0, 1, ..., etc. And if you believe in the set of normal positive whole numbers, like if you agree that set is a thing, then it's pretty much impossible within normal mathematical reasoning to avoid being forced to admit that all the rest of these infinite numbers upstairs exist too.

1: Is that bad?

0: Well some people loved it. Like this guy who's quoted incessantly in every book about this stuff.

---

> _"No one shall expel us from the paradise that Cantor has created."_
> -David Hilbert.

---

0: Others people thought Georg was corrupting the youth.

1: C'mon, nobody would actually think infinity is "not suitable for kids."

0: I'm serious. Here's an example.

> Kronecker, who headed mathematics at Berlin until his death in 1891, became increasingly uncomfortable with the prospect of having Cantor as a colleague, perceiving him as a "corrupter of youth" for teaching his ideas to a younger generation of mathematicians.
>
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

1: That's a bit of an over-reaction don't you think?

0: Not at all. Georg was totally corrupting the youth.

1: That's ridiculous.

![[corrupting-the-youth.png]]

1: How are infinite numbers corrupting the youth?

0: Well they're at least changing the norms. And there are some downsides of infinite numbers for some purposes. But when I said "corrupting the youth," I meant it as a compliment. The youth always make sure to find ways to get corrupted each generation. It's part of what it means to be "the youth." And of all the ways to get corrupted, getting corrupted with taboo mathematics isn't exactly the worst way.

1: Fair.

0: But he definitely changed the norms. Georg really stretched the boundaries of the mathematical universe about as far as they could be stretched without bursting. But he wasn't making imprecise or poorly thought out arguments. His arguments were very much "normal mathematics." That's part of why they were so controversial.

1: How can something be "controversial" in normal mathematics? I thought mathematics had some pretty clear cut rules about what is and isn't rigorous.

0: Not even close. But that's a story for another file. For now, just know that Cantor sort of found a security vulnerability in "stable mathematics" that more or less allowed the execution of arbitrary code. At least he could keep calling `+=1` across dot-dot-dots, and that's sort of arbitrary code execution as far as numbers are concerned.

1: What do you mean "across dot-dot-dots."

0: Well everybody agrees it's ok to write this:

_Consider the set of natural numbers:_

$$0, \; 1, \; \dots$$

1: Naturally.

0: What Cantor did was come up with definitions of "th" and "size" for sets such that---

1: What's "th"?

0: Like 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, ... nth. Order. There's two kinds of numbers. For example, there's two kinds of seven.

1: How are there two kinds of seven.

0: Well you can be the 7th person in line. That's a different idea from there being 7 people in line.

1: I don't see how that's different.

0: For finite numbers it's not. For Cantor's infinite numbers, they're slightly different. He called them Ordinals and Cardinals. Ordinals are like "X is the 7th one." Cardinals are like "X has 7 things in it."

1: So wait, you forgot to explain what you meant by "across dot-dot-dots."

0: Ok right. So everybody agrees it's ok to write this:

_Consider the set of natural numbers:_

$$0, \; 1, \; \dots$$
1: Naturally. We did this already.

0: What Cantor did was come up with definitions of order and size for sets that allowed him to give a precise meaning to this:

$$0, \; 1, \dots, \; \omega$$
1: What's $\omega$?

0: The $\omega^{th}$ number.

1: That's not helpful.

0: It's the infinity-th number.

1: Weird.

0: That's what I mean by saying he could keep calling `+=1` across dot-dot-dots. It's called a "limit ordinal." Cantor came up with some basic definitions in standard mathematical style that let him write that. Then after that, they allowed him to do this:

$$0, \; 1, \dots, \; \omega, \; \omega+1, \; \dots \;$$

1: Then what?

0: Naturally:

$$0, \; 1, \dots, \; \omega, \; \omega+1, \; \dots, \; \omega \cdot 2, \; \omega \cdot 2 + 1$$

1: Is that two times infinity?

0: Infinity times two. Slightly different once you get into the implementation details, but that's the idea.

1: How is "infinity times two" not just "infinity."

0: It is! In terms of size. Remember, Georg has two definitions of number. They're the same for finite numbers, but slightly different for infinite ones. So $\omega \cdot 2$ has the same _size_ as $\omega$, but it's different in terms of the order it shows up in the big infinite list.

1: This math stuff seems pretty imprecise.

0: It is. At least sometimes. But not in this case. In this case, the cardinality of $\omega \cdot 2$ is the same as the cardinality of $\omega$. That's a fancy way of saying they have the same size. Because Georg's definition of "same size" is "If you change only the names, do they have the same number?"

1: What do you mean "If you change only the names?"

0: Well no matter what we believe about mathematics, like whether we believe that "infinite stuff exists" or whether we think that's all nonsense, one thing everyone can agree on is names aren't magic.

1: Obviously. I don't know what you mean, but I think I agree.

0: All I meant by magic is that the following situation would be completely unacceptable:

Suppose you have a set of stuff, like:

$$0, \; 1, \dots, \; \omega, \; \omega+1, \; \dots$$

Then suppose you just change the squiggles we use to write down the numbers without changing anything else about the set. For example, suppose you put hats on everything:

$$\hat{0}, \; \hat{1}, \dots, \; \hat{\omega}, \; \hat{\omega}+\hat{1}, \; \dots$$
0: Is that the same set?

1: I don't know. Maybe not. I could imagine the hat-numbers might be different objects.

0: Exactly. Now, do the two sets have _the same size_?

1: I don't know. I'm not convinced they do.

0: Explain?

1: Like maybe the hats weigh something. Maybe $\hat{1}$ means "The number $1$'s home directory." And home directories can have all sorts of stuff inside them. So $\hat{1}$ might be bigger than $1$, and that would make it a different size.

0: Ok that's a good point but that's not what we mean by "size" here. We're not talking about weight or physical volume or anything. I just mean the number of numbers.

1: The number of numbers? Like a meta-number?

0: No, the number of numbers in the two lists. The list without hats, and the list with hats. Do those two lists have the same number of numbers.

1: Oh yeah I see. I'd say they do.

0: What about now.

$$0, \; 1, \dots, \; \omega, \; \omega+1, \; \dots$$

vs

$$\hat{0}, \; \hat{1}, \dots, \; \hat{\omega}, \; \hat{\omega}+\hat{1}, \; \dots$$

vs

$$0, \; 2, \; \dots, \; 1, \; 3, \; \dots$$

1: No the third list is different.

0: Different how?

1: You changed it.

0: What did I change?

1: You got rid of the infinite numbers.

0: Did I?

1: Stop being zen. Was your third list supposed to be an abbreviation for this idea here:

$$0, \; 2, \; 4, \; 6, \; 8, \; \dots, \; 1, \; 3, \; 5, \; 7, \; 9, \; \dots$$
0: Exactly.

1: But that's just all the even numbers on the left, then a dot-dot-dot, then all the odd numbers.

0: No no, that's just the squiggles. Don't get confused by the squiggles. Suppose I'm from a strange country where I use the symbol $2$ to mean one, and the symbol $1$ to mean infinity.

1: Sounds like a pretty nice country.

0: So you agree they're the same set?

1: No, but I see the trick you did now, and I see that I'm gonna have trouble arguing that it's a different size just because the shape of the squiggles changed.

0: That was Cantor's whole idea. He defined the size of two sets to be the same size if you can turn one into the other just by changing the names like we did. He defined it in terms of functions, but it's the same idea. If you can write down a function that turns each element in set A into exactly one element in set B, and if we can verify somehow that everything in B gets "hit" (i.e., paired with) some element of A, then we can force the reader into the same position. They might agree this is a trick, but they're not gonna be able to argue their way out of the idea that the two sets are the same size.

1: I see. So how is this relevant to us? I thought we were learning about the Foundational People.

0: Right, this is where it all started.

1: Where what all started?

0: The story of our people. See Cantor caused a total crisis. Mathematics as a whole wasn't sure what to do with Cantor or his infinite number of different sizes of infinity. A lot of people thought it was nonsense. He felt totally humiliated.

> Cantor suffered his first known bout of depression in May 1884. Criticism of his work weighed on his mind: every one of the fifty-two letters he wrote to Mittag-Leffler in 1884 mentioned Kronecker. A passage from one of these letters is revealing of the damage to Cantor's self-confidence:
> 
> _... I don't know when I shall return to the continuation of my scientific work. At the moment I can do absolutely nothing with it, and limit myself to the most necessary duty of my lectures; how much happier I would be to be scientifically active, if only I had the necessary mental freshness._
> 
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

0: He eventually sort of lost his mind.

> After Cantor's 1884 hospitalization there is no record that he was in any sanatorium again until 1899. Soon after that second hospitalization, Cantor's youngest son Rudolph died suddenly on 16 December (Cantor was delivering a lecture on his views on Baconian theory and William Shakespeare), and this tragedy drained Cantor of much of his passion for mathematics. Cantor was again hospitalized in 1903. One year later, he was outraged and agitated by a paper presented by Julius König at the Third International Congress of Mathematicians. The paper attempted to prove that the basic tenets of transfinite set theory were false. Since the paper had been read in front of his daughters and colleagues, Cantor perceived himself as having been publicly humiliated. Although Ernst Zermelo demonstrated less than a day later that König's proof had failed, Cantor remained shaken, and momentarily questioning God.
> 
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

0: The legend goes that he lost his mind from coming face to face with the absolute infinite. As if the subject itself somehow scrambled his mind. In reality, it's pretty clear his mental illness was at least partially related to him feeling like his work wasn't accepted by the community he loved.

> Cantor suffered from chronic depression for the rest of his life, for which he was excused from teaching on several occasions and repeatedly confined to various sanatoria. The events of 1904 preceded a series of hospitalizations at intervals of two or three years. He did not abandon mathematics completely, however, lecturing on the paradoxes of set theory (Burali-Forti paradox, Cantor's paradox, and Russell's paradox) to a meeting of the Deutsche Mathematiker-Vereinigung in 1903, and attending the International Congress of Mathematicians at Heidelberg in 1904.
> 
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

0: He wasn't totally rejected by any means. A lot of pretty famous mathematicians thought his work was great. Like this guy Bertrand Russell. Remember that name, we'll run into him again soon.

> In 1911, Cantor was one of the distinguished foreign scholars invited to the 500th anniversary of the founding of the University of St. Andrews in Scotland. Cantor attended, hoping to meet Bertrand Russell, whose newly published Principia Mathematica repeatedly cited Cantor's work, but the encounter did not come about. The following year, St. Andrews awarded Cantor an honorary doctorate, but illness precluded his receiving the degree in person.
> 
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

0: Either way, things didn't end well for Cantor. 

> Cantor retired in 1913, and lived in poverty and suffered from malnourishment during World War I. The public celebration of his 70th birthday was canceled because of the war. In June 1917, he entered a sanatorium for the last time and continually wrote to his wife asking to be allowed to go home. Georg Cantor had a fatal heart attack on 6 January 1918, in the sanatorium where he had spent the last year of his life.
> 
> -The Dynamic Read-Writable Free Encyclopedic Repository of the Modern State of Human Knowledge

1: Well that's a depressing story.

0: Definitely. That's why he's not one of the Foundational People, as far as I'm concerned.

1: Woah that's cruel. Why exclude him?

0: No no, I meant it as a sign of respect! As far as I'm concerned, Cantor was a proper mathematician. That's how he thought. That's where he belonged. That's the community he wanted to be accepted by. It's only right to include him in among the mathematicians in any proper history that brushes up against him in any way. It's what he would have wanted. Plus he wasn't really concerned with Foundations. He was wild. A proper Platonist, using his definitions and theorems to ascend to arbitrary heights in the eternal hierarchy of abstract non-constructive existence that ends precisely never, at the exact moment that one comes face to face with God, the absolute infinite, which Cantor and everyone after him called $\Omega$.

1: Sounds like theology.

0: Exactly. That's mathematics. And Cantor was a mathematician. It would be a disservice to consider him one of the Foundational People. But Cantor is where our people's history begins.

1: How so?

0: Well there had always been people like us in the world, Foundational People that is, Charles Babbage and Ada Lovelace probably had this type of mind. And that Leibniz guy who invented Calculus around the same time as Newton, he was clearly our type of person too. But this was the first time that our people all came out of the woodwork and came together as a People. Because this was the first time the mathematicians realized how much they needed some real Foundations. For the first time, after Cantor, mathematics realized it was in trouble. That's not quite true, Calculus caused a bit of an uproar about Foundations too. But Cantor rocked the boat, and soon after mathematics realized it was sinking.

1: Sinking?

0: Sinking. Quick, pop the stack.

1: But it was just ge---

goto: [[We#The beginning|We]]