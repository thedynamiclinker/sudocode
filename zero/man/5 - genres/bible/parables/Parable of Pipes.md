Type: [[Perfect]], [[System]], [[sys/kernel/Creation]], [[Parable]]

---

The Story of Pipes

- For years, [Doug McIlroy](http://genius.cat-v.org/doug-mcilroy) had been talking about the idea that would eventually become pipes.
- Ken was never interested, and Doug could never understand why.
- Doug's original description sounded like this:

![[doug-mcilroy-original-idea-of-pipes.png]]

- Doug's original description says things like "our loader should be able to do link-loading," and refers to "our library filing scheme."
- Ken correctly understood that Doug's original idea was to connect up programs _intra-process._
- This would involve implementing pipes using a mechanism analogous to what is now required for dynamic linking at runtime.
- Any such scheme would dramatically increase the complexity of the system.
- Ken was right to not be interested in that idea at first.
- History describes both Doug and Ken as "the inventor of pipes."
- History is right.
- The final "aha" moment was when Ken realized that the right way to connect up arbitrary programs was to do so _inter-process_, and to use the program's standard input and output as the communication channels.
- Unix already had redirecting IO.
- So all Ken needed to make Doug's idea work was to redirect one command's output into a buffer, and another command's input to the same buffer, with minimal coordination.
- Implementing the idea this way meant that (almost!) no changes had to be made to existing programs, with the exception of a few minor changes like removing superfluous messages.
- Took about an hour for Ken to implement, as he describes here from [31:30 to 35:15](https://youtu.be/EY6q5dv_B-o?si=nCuZ4vmhNOIdkQ4S).
- Ken and Dennis "rewrote the world that night."
- Manic frenzy of excitement ensued within Bell Labs
- Doug McIlroy famously said "The next day we had this orgy of one liners."


Moral:
- A minor detail can make the difference between an idea not worth implementing on one hand, and one of the greatest ideas in the history of computing on the other.
- The design choices that lead to an "orgy of one-liners" are perhaps the closest thing to "perfection" in our field, as Bryan Cantrill articulates beautifully here [3:08 to 5:32](https://www.youtube.com/watch?v=S0mviKhVmBI).