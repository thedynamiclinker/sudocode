## The Paper

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


