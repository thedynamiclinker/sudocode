Type: [[Bottom-Up]], [[System]], [[sys/kernel/Creation]], [[Parable]]

---

> _Make originated with a visit from Steve Johnson (author of yacc, etc.), storming into my office, cursing the Fates that had caused him to waste a morning debugging a correct program (bug had been fixed, file hadn't been compiled, cc \*.o was therefore unaffected). As I had spent a part of the previous evening coping with the same disaster on a project I was working on, the idea of a tool to solve it came up. It began with an elaborate idea of a dependency analyzer, boiled down to something much simpler, and turned into Make that weekend. Use of tools that were still wet was part of the culture. Makefiles were text files, not magically encoded binaries, because that was the Unix ethos: printable, debuggable, understandable stuff._
> _-Stuart Feldman, The Art of Unix Programming, Eric S. Raymond 2003_

> _All problems in computer science can be solved by another level of indirection._
> _-David Wheeler_

---

Yes, this parable is longer than the others.

Deal with it.

## The Bottom-Up Miracle

The Linux from Scratch project contains the most practical lesson in all software.

It may also be the most impractical operating system, and trying to use it as your main OS is probably a waste of time.

But spending a day or two running through the LFS project teaches you something about reality that will change the way you view our field.

Linux from Scratch has no installer.

There's no `.iso` image to `dd` to a CD or USB.

Linux from Scratch is just a PDF.

That PDF contains a book that says "Go to these URLs, scattered throughout the internet, download these `tar.gz` files, and build these packages in this order, at the end of the process, you will have built an OS."

What is Unix, and what is Linux?

The most well known direct descendants of Unix -- the operating systems we call BSD -- ship the kernel and the userspace coreutils as one system.

BSD is "top down," at least with respect to the core system.

There's no "BSD from Scratch." In BSD culture, if you want to build an OS from scratch you fork a previous BSD, one who source code has a direct line of heritage back to AT&T Unix. In BSD, you don't need to spend any time wandering around in the wilderness collecting packages.

LFS, in contrast, just gives you a bunch of urls, from all over the web. You `wget` each url and get a tar or zip file, and you build the result into a working system, even though the pieces were not all written by one group of people. GNU is  perhaps a plurality, but certainly not a majority.

The people involved in building that system did not all share a set of coding standards, or software development processes. They did not all use jira or put documentation in confluence. They never all sat on a zoom or slack or teams call at the same time. They did what they did across the decades, without knowing who might be reading their tool's output over a pipe or writing into it.

The resulting system is, I would argue, the most astonishing example of collaboration in any software development project of all time. The Linux kernel may contain more code, more commits and merges per unit time, and be more essential in the sense that it would be harder to replace than the userland tools if it was suddenly gone.

But the kernel is less impressive in the sense that it's one big repo, with countless forks, but a shared coding standard. Though it is a radical departure from the software development methods at most companies, it more closely resembles those processes than the miracle of the Linux userspace resembles either.

The miracle of Linux userspace is precisely that it came into existence with precisely zero top-down social control. No common coding standards, no BDFL, no one company or common language.

For anyone currently suffering under the burden of company processes that harm their personal productivity, the experience of seeing LFS is what I can only describe as a boris yeltsin grocery store moment.

## Boris Yeltsin visits the Grocery Store

Background: In 1989, two years before the fall of the Soviet Union, Boris Yeltsin visited a grocery store.

![[boris-yeltsin-grocery-store.jpg|600]]

Nevertheless, Yeltsin described the experience as follows:

> _When I saw those shelves crammed with hundreds, thousands of cans, cartons and goods of every possible sort, for the first time I felt quite frankly sick with despair for the Soviet people. That such a potentially super-rich country as ours has been brought to a state of such poverty! It is terrible to think of it._

His 2000 biography _Yeltsin, a Revolutionary Life,_ describes his experience as follows:

> _"For a long time, on the plane to Miami, he sat motionless, his head in his hands. 'What have they done to our poor people?' he said after a long silence." He added, "On his return to Moscow, Yeltsin would confess the pain he had felt after the Houston excursion: the 'pain for all of us, for our country so rich, so talented and so exhausted by incessant experiments'." He wrote that Mr. Yeltsin added, "I think we have committed a crime against our people by making their standard of living so incomparably lower than that of the Americans." An aide, Lev Sukhanov, was reported to have said that it was at that moment that "the last vestige of Bolshevism collapsed" inside his boss._

How could this have happened?

Though opinionated members of opposing ideologies will surely argue over the meaning of moments like this until the end of time, the lesson here is a clear example of an eternal theme throughout history:

_Bottom-up beats Top-down._

By any historical standard, the Russian people are no more or less intelligent, industrious, or hard-working than people of any other society. If anything, the culture as a whole has historically outperformed at endeavors like mathematics, engineering, and other intellectual pursuits.

So how could this culture have become so impoverished that their soon-to-be president would find himself, head in hands, after an unremarkable trip to a suburban grocery store?

In this case, it is not oversimplifying to reduce a century of history to a single sentence.

Bottom-up beats Top-down.

What does this mean?

Believers in socialist and communist ideals often portray their ideal society as one built from a bottom-up self-organized freedom of choice. At the same time, capitalist systems are often portrayed in media and art as top-down, corporate, managerial, and bureaucratic. If these images were correct, the historical performance of these two systems would be precisely the reverse.

Though we make no comment on the reasons for this phenomenon, it is an empirical fact that communist ideology in practice has thus far been implemented as a top-down system of command and control.

By top-down we mean a preference for "experts" and centralized planning over incentives and individual choices.

This, more than any other factor, is the reason why communism has always failed.

Further, the aspects of capitalism most harshly criticized by believers in socialism and communism do tend to be the features that are perceived as top-down.

There is nearly universal agreement by parties arguing in good faith that human flourishing is best achieved by bottom-up self-organization, not top-down control.

TODO: Private Soviet farms produced 90% of the produce, other examples of bottom-up vs top-down.

So what does this have to do with Linux from Scratch?

## Convergent Evolution

Insert LFS screenshots.
Make interface was agreed upon with no central authority or leader.
This is what makes Linux different from other systems, and more successful in all aspects of computation except perhaps aesthetic unity, which is a rare area where top-down control seems to win.