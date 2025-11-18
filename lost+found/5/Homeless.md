
## On Turing's eccentricities at Bletchley Park

> _In the first week of June each year \[Turing\] would get a bad attack of hay fever, and he would cycle to the office wearing a service gas mask to screen the pollen. His bicycle had a fault: the chain would come off at regular intervals. Instead of having it mended he would count the number of times the pedals went round and would get off the bicycle in time to adjust the chain by hand._
> -Charles Petzold, The Annotated Turing

## On Turing and Joan Clarke, 1941

> _In the spring of 1941, Alan Turing made a proposal of marriage to Joan Clarke, one of the rare women at Bletchley Park who wasn’t relegated to a mindless clerical job. Joan Clarke had been studying mathematics at Cambridge when she was recruited for code-breaking. A few days after the proposal Turing confessed to her that he had “homosexual tendencies” but the engagement continued for several more months before he felt he had to call it off._
> -Charles Petzold, The Annotated Turing

## On Turing's 1942-43 mission and meetings at Bell Labs

> _In November 1942, Turing was sent on a mission to Washington, D.C., to help coordinate code-breaking activities between England and the United States. Following that assignment, he spent the first two months of 1943 at Bell Laboratories, at the time located on West Street in New York City. There he met Harry Nyquist (1889-1976), who pioneered the theory of digital sampling, and Claude Elwood Shannon (1916-2001), whose paper “A Mathematical Theory of Communication” (1948) would found the field of information theory and introduce the word "bit" to the world._
> -Charles Petzold, The Annotated Turing

## Other Quotes

> _We may now construct a machine to do the work of this computer._
> -Alan Turing, 1936

> _Let us now return to the analogy of the theoretical computing machines... It can be shown that a single special machine of that type can be made to do the work of all. It could in fact be made to work as a model of any other machine. The special machine may be called the universal machine..._
> -Alan Turing, Lecture to the London Mathematieal Society, February 20th 1947

> _If it should turn out that the basic logics of a machine designed for the numerical solution of differential equations coincide with the logics of a machine intended to make bills for a department store, I would regard this as the most amazing coincidence I have ever encountered._  
> -Howard Aiken 1956

0: Ok so, let's recap. Church comes up with Lambda Calculus. Gödel comes up with General Recursive Functions. Kleene proves the two systems are equivalent. And legend has it that when Gödel realized his system was equivalent to Church's Gödel says "Oh. Well then I guess mine was wrong."

1: Did that actually happen?

0: Not sure, but it's a good legend.

1: So how does Turing fit in to this?

0: Well Turing's work is what convinced Gödel.

1: Convinced him of what?

0: That the three of them had probably captured _all_ of computation in these definitions. 

1: Damn, what year was this?

0: 1936.

1: That's insane.

> Steve Kleene: We had done all this work before we heard of Turing. Turing's paper is also 1936. But a little later in 1936. But my impression is that Turing did it independently of knowing anything about what we were doing.

0: Yeah so Turing is over in England. Born in 1912 in the Paddington part of London where that famous bear is from. By this point he's 24 years old. Still an undergraduate. He's not aware of any of this work from Church, he may have known about Gödel. And he comes out with this paper as a 24 year old college kid that ends up convincing Gödel.


## The Beginning of the Paper

![[turing-1936-01.png]]


![[turing-1936-02.png]]


![[turing-1936-03.png]]


![[turing-1936-04.png]]


![[turing-1936-05.png]]


![[turing-1936-06.png]]


![[turing-1936-07.png]]


![[turing-1936-08.png]]

0: The $m$ stands for man. Or machine. I haven't decided yet.

![[turing-1936-09.png]]


![[turing-1936-10.png]]

![[turing-1936-11.png]]


![[turing-1936-12.png]]


![[turing-1936-13.png]]


![[turing-1936-14.png]]


![[turing-1936-15.png]]


![[turing-1936-16.png]]

- `rip`, `stdout`, and `.data` 
- `rip`, `output.txt`, and `.data` + `.text`
- Line we're executing, buffer we're writing our output to, and all variables in the address space.


![[turing-1936-17.png]]


![[turing-1936-18.png]]


![[turing-1936-19.png]]


![[turing-1936-20.png]]


| The Program      |       |      |       |      |
| ---------------- | ----- | ---- | ----- | ---- |
| if state is      | b     | c    | e     | f    |
| and symbol is    | None  | None | None  | None |
| then do this     | P0, R | R    | P1, R | R    |
| and set state to | c     | e    | f     | b    |


| You Think      | 💭 b |     |     |     |     |     |     |     |     |
| -------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| You See        | 👁️  |     |     |     |     |     |     |     |     |
| Paper Contents |      |     |     |     |     |     |     |     |     |
| Paper Address  | 0    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |

Do the action for the b state.

| You Think      |     | 💭 c |     |     |     |     |     |     |     |
| -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| You See        |     | 👁️  |     |     |     |     |     |     |     |
| Paper Contents | 0   |      |     |     |     |     |     |     |     |
| Paper Address  | 0   | 1    | 2   | 3   | 4   | 5   | 6   | 7   | 8   |

Do the action for the c state.

| You Think      |     |     | 💭 e |     |     |     |     |     |     |
| -------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
| You See        |     |     | 👁️  |     |     |     |     |     |     |
| Paper Contents | 0   |     |      |     |     |     |     |     |     |
| Paper Address  | 0   | 1   | 2    | 3   | 4   | 5   | 6   | 7   | 8   |

Do the action for the e state.

| You Think      |     |     |     | 💭 f |     |     |     |     |     |
| -------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
| You See        |     |     |     | 👁️  |     |     |     |     |     |
| Paper Contents | 0   |     | 1   |      |     |     |     |     |     |
| Paper Address  | 0   | 1   | 2   | 3    | 4   | 5   | 6   | 7   | 8   |

Do the action for the f state.

| You Think      |     |     |     |     | 💭 b |     |     |     |     |
| -------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
| You See        |     |     |     |     | 👁️  |     |     |     |     |
| Paper Contents | 0   |     | 1   |     |      |     |     |     |     |
| Paper Address  | 0   | 1   | 2   | 3   | 4    | 5   | 6   | 7   | 8   |

After one loop, we're at at address 4, where the eye is.
And we're back to the same "state" where we started.
- The "state" doesn't include the state of the paper.
- The "state" is just the letter $b$, $c$, $e$, or $f$.
- In other words, the "state" is just what you think, not what you see.
So at this point we do the same four things we just did, again.

| You Think      |     |     |     |     |     |     |     |     | 💭 b |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| You See        |     |     |     |     |     |     |     |     | 👁️  |
| Paper Contents | 0   |     | 1   |     | 0   |     | 1   |     |      |
| Paper Address  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8    |

So then we end up here, thinking about b again.

Now do this again for the table at the top of page 5 of Turing's paper.


![[turing-1936-21.png]]


![[turing-1936-22.png]]

1: What's the ə?

0: Uh...

1: _(Waiting patiently.)_

0: Ok so...

1: Wait you didn't answer my question.

0: Yes I did.

1: What?

0: The ə symbol is called "schwa." It's a letter from the International Phonetic Alphabet. It represents the "uh" sound.

1: Weird. Why is Turing using it here?

TODO: Once we get to the əə example, start including excerpts from The Annotated Turing.

0: Not sure. Seems like a pretty irrational choice. But that's a sensible thing to do here. In this example he's showing we can compute an irrational number.

1: Sometimes I feel like you can rationalize anything...

0: Not this number! Look.

$$0010110111011110111110$$

1: What number is that?

0: I don't think it has a name. But it's:

0
0
1
0
11
0
111
0
1111
0
11111
0
111111
0
1111111
0
11111111
0
etc.

1: How do we know that's irrational?

0: Well, it's got a pattern which is why it's computable, but the pattern doesn't repeat in a simple-minded way like the number we computed above that just went 0 1 0 1 0 1 0 1 0 1 0 1 0 1...


![[turing-1936-23.png]]


![[turing-1936-24.png]]


![[turing-1936-25.png]]


![[turing-1936-26.png]]


![[turing-1936-27.png]]


![[turing-1936-28.png]]


![[turing-1936-29.png]]


![[turing-1936-30.png]]


![[turing-1936-31.png]]


![[turing-1936-32.png]]


![[turing-1936-33.png]]


![[turing-1936-34.png]]


![[turing-1936-35.png]]


![[turing-1936-36.png]]


0: This time we won't have blanks between the digits. Or bigits.

![[turing-1936-37.png]]

0: Ok pause here for a second.

1: What's up?

0: Head over to this file with me.

goto: [[lost+found/5/2]]

## Godel Unconvinced

![[computability-turing-godel-church-04.jpg]]


![[computability-turing-godel-church-05.jpg]]


![[computability-turing-godel-church-06.jpg]]


![[computability-turing-godel-church-07.jpg]]


![[computability-turing-godel-church-08.jpg]]


![[computability-turing-godel-church-09.jpg]]



## Godel Convinced

![[computability-turing-godel-church-00.jpg]]


![[computability-turing-godel-church-12.jpg]]


![[computability-turing-godel-church-13.jpg]]


![[computability-turing-godel-church-14.jpg]]


![[computability-turing-godel-church-15.jpg]]

## Reminiscences - Turing

![[reminiscences-of-logicians-013.jpg]]


![[reminiscences-of-logicians-014.jpg]]


![[reminiscences-of-logicians-020.jpg]]


![[reminiscences-of-logicians-021.jpg]]


![[reminiscences-of-logicians-022.jpg]]


![[reminiscences-of-logicians-023.jpg]]


![[reminiscences-of-logicians-024.jpg]]


![[reminiscences-of-logicians-025.jpg]]


![[reminiscences-of-logicians-064.jpg]]


![[reminiscences-of-logicians-065.jpg]]


![[reminiscences-of-logicians-066.jpg]]


![[reminiscences-of-logicians-067.jpg]]


![[reminiscences-of-logicians-068.jpg]]


![[reminiscences-of-logicians-069.jpg]]


![[reminiscences-of-logicians-070.jpg]]


![[reminiscences-of-logicians-071.jpg]]


![[reminiscences-of-logicians-072.jpg]]


![[reminiscences-of-logicians-073.jpg]]


![[reminiscences-of-logicians-074.jpg]]


![[reminiscences-of-logicians-075.jpg]]


![[reminiscences-of-logicians-076.jpg]]


![[reminiscences-of-logicians-077.jpg]]


![[reminiscences-of-logicians-078.jpg]]


![[reminiscences-of-logicians-079.jpg]]


![[reminiscences-of-logicians-080.jpg]]


![[reminiscences-of-logicians-081.jpg]]


![[reminiscences-of-logicians-082.jpg]]


![[reminiscences-of-logicians-083.jpg]]


![[reminiscences-of-logicians-084.jpg]]


![[reminiscences-of-logicians-085.jpg]]


![[reminiscences-of-logicians-086.jpg]]


![[reminiscences-of-logicians-087.jpg]]


![[reminiscences-of-logicians-088.jpg]]


![[reminiscences-of-logicians-089.jpg]]


![[reminiscences-of-logicians-090.jpg]]


![[reminiscences-of-logicians-091.jpg]]


![[reminiscences-of-logicians-092.jpg]]


![[reminiscences-of-logicians-093.jpg]]


![[reminiscences-of-logicians-094.jpg]]


![[reminiscences-of-logicians-095.jpg]]


![[reminiscences-of-logicians-096.jpg]]


![[reminiscences-of-logicians-097.jpg]]


![[reminiscences-of-logicians-098.jpg]]


![[reminiscences-of-logicians-099.jpg]]


![[reminiscences-of-logicians-100.jpg]]


![[reminiscences-of-logicians-101.jpg]]


![[reminiscences-of-logicians-102.jpg]]

## An Enumerable Infinity of Names
### Or: One character RAM


![[turing-1936-37.png]]

0: Ok pause here for a second.

1: What's up?

0: Read that highlighed bit.

1: What about it?

0: I mean that's a pretty wacky idea no?

| One Char RAM   |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Can be erased? | No  | Yes | No  | Yes | No  | Yes | No  | Yes | No  | Yes |
| Paper Contents | 0   | L   | 1   | ד   | 0   | ్   | 1   | 根   | 1   | Ω   |
| Paper Address  | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   |


![[turing-1936-38.png]]


![[turing-1936-39.png]]


![[turing-1936-40.png]]


![[turing-1936-41.png]]


![[turing-1936-42.png]]


![[turing-1936-43.png]]


![[turing-1936-44.png]]


![[turing-1936-45.png]]


![[turing-1936-46.png]]


![[turing-1936-47.png]]


![[turing-1936-48.png]]


![[turing-1936-49.png]]


![[turing-1936-50.png]]

Ok so back to Turing. He had this completely ridiculous and impractical idea of "single character RAM", and if you need more storage space you just "add more symbols" somehow. That ridiculous idea turns out to be pretty reasonable actually, but we'd have to wait over half a century before UTF-8 would be invented in order to be able to do something like that. And even if we could do Turing's idea, modern computers don't do that. They just write to some other location that isn't interleaved with our output bytes. But Turing's idea was really creative given the limited setup he was working with in the paper. So back to the paper.

Next up, Turing invents shared libraries.

Or functions. Same idea sort of.


![[turing-1936-51.png]]


![[turing-1936-52.png]]


![[turing-1936-53.png]]


![[turing-1936-54.png]]

On page 7 with the "Functions that take machine states as inputs," 1 asks if this is like metaprogramming. 0 says it's just programming, because "machine states" are basically just variables in the address space.

![[turing-1936-55.png]]


![[turing-1936-56.png]]


![[turing-1936-57.png]]


![[turing-1936-58.png]]


![[turing-1936-59.png]]


![[turing-1936-60.png]]


![[turing-1936-61.png]]


![[turing-1936-62.png]]

1: This Dungeons and Dragons alphabet is making it harder to read.

0: Nah I think this example was just hard. Turing feels the same way. Here look:

> The last example seems somewhat more difficult to interpret than most.
> -Top of pg 8.

![[turing-1936-63.png]]


![[turing-1936-64.png]]


![[turing-1936-65.png]]


![[turing-1936-66.png]]


![[turing-1936-67.png]]


![[turing-1936-68.png]]

goto: [[lost+found/5/3]]


## He called it "He"
### Or: So did Kleene
### Or: Minds and Machines
### Or: Applied philosophy that actually works


![[turing-1936-84.png]]


![[turing-1936-85.png]]


![[turing-1936-86.png]]


![[turing-1936-87.png]]


![[turing-1936-88.png]]


![[turing-1936-89.png]]


![[turing-1936-90.png]]


![[turing-1936-91.png]]


![[turing-1936-92.png]]


![[turing-1936-93.png]]


![[turing-1936-94.png]]


![[turing-1936-95.png]]


![[turing-1936-96.png]]


![[turing-1936-97.png]]


![[turing-1936-98.png]]

1: He just said "his" for the computer.

0: Yeah that was normal back then.

1: What was normal?

0: For computers to be humans. Here look, this is from Kleene's introduction to his chapter on Turing computability.

(Insert IM screenshot here.)

![[turing-1936-99.png]]


![[turing-1936-100.png]]


![[turing-1936-101.png]]


![[turing-1936-102.png]]


![[turing-1936-103.png]]


![[turing-1936-104.png]]


![[turing-1936-105.png]]


![[turing-1936-106.png]]


![[turing-1936-107.png]]


![[turing-1936-108.png]]


![[turing-1936-109.png]]


![[turing-1936-110.png]]


![[turing-1936-111.png]]


![[turing-1936-112.png]]


![[turing-1936-113.png]]


![[turing-1936-114.png]]


![[turing-1936-115.png]]


![[turing-1936-116.png]]


goto: [[lost+found/5/4]]


## Description Numbers

![[turing-1936-69.png]]


![[turing-1936-70.png]]


![[turing-1936-71.png]]


![[turing-1936-72.png]]


![[turing-1936-73.png]]


![[turing-1936-74.png]]


![[turing-1936-75.png]]


![[turing-1936-76.png]]


![[turing-1936-77.png]]


![[turing-1936-78.png]]


![[turing-1936-79.png]]


![[turing-1936-80.png]]


![[turing-1936-81.png]]


![[turing-1936-82.png]]


![[turing-1936-83.png]]

goto: [[lost+found/5/5]]


## The Martyr

0: Turing finished the proof of the three-way equivalence, thus establishing more clearly than anyone else the plausibility of Church's Thesis, now called Church-Turing. This was the final nail in the coffin. These three giants, the first three developers in the history of computing who together made the first language, the first compiler, and the first hardware design, these same these people now also seemed to have captured the concept of computation itself, in three definitions that none of them expected to be the same. Except maybe Turing. They captured the essence of computation, not within some particular formal system or machine, but any computation that could ever be performed by any physical system past or future. They got it. The final nail was this 1937 paper down below. Almost 100 years later, after all the developments in computing and technology since the late 1930s, our species still hasn;t found a single counterexample to Church and Turing's claim. Computation has a ceiling. That ceiling is universal. And it's damn easy to get there. Everything else is lots and lots of details that take place at or below the ceiling. I can't think of a more important achievement in the foundations of human knowledge in all of human history than that. The story of computation and how our species captured it is as important as the discovery of fire. I think even the discovery of electricity or magnetism or the strong and weak nuclear forces aren't as incredible as the discovery of computation. Despite all the well-deserved books about Gödel and Turing, this story is never told with anything close to the energy it deserves. And I can feel in my bones every way that the version of it I've told here is still an absolute failure compared to what this story deserves. It would take a new curriculum to really tell it properly. Students in our field, and even the profess{or, ional developer}s of our field don't know enough about the beginning or the middle of this story. Sadly most of us know about the end.

1: What was the end?

0: Not the end of the story. But an end to this thread.

![[turing-1937-sex-footnote-1.png]]

0: In any sane universe, Turing's sex life would've been no more than a footnote to his story. No more significant than a randomly chosen footnote in one of his papers.

![[turing-1937-sex-footnote-2.png]]

1: What's that?

0: A footnote in one of his papers that happens to say $S(e(x))$.

1: Is this supposed to be important?

0: No. That's the point. In Turing's story, what should have been an unimportant footnote that happened to say $S(e(x))$ turned out to lead to the premature end of his story.

1: THAT footnote led to---

0: No not that one. I don't think anyone even noticed that one. Not sure Turing noticed either, though I like to think he did. This next bit is the sad one. The one people noticed.

![[yours-in-distress-alan.png]]

%%
From: https://turingarchive.kings.cam.ac.uk/correspondence-amtd/amt-d-14a
Copyright info: https://turingarchive.kings.cam.ac.uk/copyright-and-terms-use
%%

1: What does it say? I can't quite read it.

0: Something like this.

> My dear Norman,
>
> I don’t think I really do know much about jobs, except the one I had during the war, and that certainly did not involve any travelling. I think they do take on conscripts. It certainly involved a good deal of hard thinking, but whether you’d be interested I don’t know. Philip Hall was in the same racket and on the whole, I should say, he didn’t care for it. However I am not at present in a state in which I am able to concentrate well, for reasons explained in the next paragraph.
> 
> I’ve now got myself into the kind of trouble that I have always considered to be quite a possibility for me, though I have usually rated it at about 10:1 against. I shall shortly be pleading guilty to a charge of sexual offences with a young man. The story of how it all came to be found out is a long and fascinating one, which I shall have to make into a short story one day, but haven’t the time to tell you now. No doubt I shall emerge from it all a different man, but quite who I’ve not found out.
> 
> Glad you enjoyed broadcast. Jefferson certainly was rather disappointing though. I’m afraid that the following syllogism may be used by some in the future.
> 
> Turing believes machines think  
> Turing lies with men  
> Therefore machines do not think
> 
> Yours in distress,
> 
> Alan


goto: [[101]]
