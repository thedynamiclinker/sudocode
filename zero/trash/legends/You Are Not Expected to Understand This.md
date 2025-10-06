
```
From: lwj@cs.kun.nl (Luc Rooijakkers)
Newsgroups: alt.folklore.computers
Subject: Explanation of "don't understand" comment
Message-ID: <3812@wn1.sci.kun.nl>
Date: 24 Jul 91 10:06:02 GMT
Sender: root@sci.kun.nl
Organization: University of Nijmegen, The Netherlands
Lines: 66

In <1991Jul22.113627.13234@sun.pcl.ac.uk> malcolmr@sun.pcl.ac.uk (Malcolm Ray)
writes:

>In article <1991Jul20.133238.25882@aber.ac.uk> ccs7@aber.ac.uk (Christopher
Samuel) writes:
>>In article <KENW.91Jul15225254@skyler.arc.ab.ca>
>>   kenw@skyler.arc.ab.ca (Ken Wallewein) doodled:
>>
>>> I've heard -- or read, I think -- about some code that contained the comment
>>> "you aren't expected to understand this".  Seems to me it was in TCP/IP.
>>> /kenw
>>
>>I always thought that it was in or just before the sheduler algorithm.

>It was in the swtch() function, which was indeed part of the scheduler.

[Gives edited full text of the comment]

>Well, you can see what they mean! :-)  I remember being well chuffed that
>I *did* understand it, but don't expect me to now...

It was not terribly complicated, though, but you had to read the machine
language also... An excerpt of my submission for the jargon file:

I looked it up in my photocopy of `UNIX(tm) Operating System Source Code,
Level Six', from J. Lions from the University of New South Wales.

The full text of the comment from V6 slp.c (context-switching code) was

        If the new process paused because is was swapped out,
        set the stack level to the last call to savu(u_ssav).
        This means that the return which is executed immediately after
        the call to aretu actually returns from the last routine which
        did the savu.

        You are not expected to understand this.

The difficulty with V6 context switching was that the assembly language
routines for restoring context changed the stack pointer but
nevertheless returned to their calling routine, leaving it with an invalid
stack frame (actually, the stack frame of the routine which did the
original context save). This was changed in V7 to routines more like
setjmp/longjmp. Even the authors of V6 had trouble with it, as
exemplified by

           Finally, the most basic routines for multi-programming, those
           that pass control from one process to another, turned out
           (after causing months of nagging problems) to be incorrectly
           specified and actually unimplementable correctly on the
           Interdata, because they depended improperly on details of the
           register-saving mechanism of the calling sequence generated
           by the compiler. These primitives had to be redesigned; they
           are of special interest not only because of the problems they
           caused, but because they represent the only part of the
           system that had to be significantly changed, as distinct from
           expressed properly, to achieve portability.
           
(from S. C. Johnson and D. M. Ritchie, `Portability of C Programs and the
UNIX System', UNIX System Readings and Applications, Bell System Technical
Journal special issue on UNIX, Vol 57, No 6, July-August, also available
from Prentice-Hall). This article discusses the porting of Research Unix
from the PDP-11 to the Interdata 8/32 during 1977, somewhere between V6
and V7.

-- 
Luc Rooijakkers                                 Internet: lwj@cs.kun.nl
Faculty of Mathematics and Computer Science     UUCP: uunet!cs.kun.nl!lwj
University of Nijmegen, the Netherlands         tel. +3180652271


	[ and from Dennis Ritchie himself ]

From: Dennis Ritchie <dmr@alice.att.com>
Date: 2 Apr 92 09:34:24 GMT
Organization: AT&T Bell Laboratories, Murray Hill NJ

People might be interested in more of the context
of the famous `you are not expected to understand this' comment.
(Tim Smith is wrong on the details.)  It was made somewhat in
the spirit of `this won't be on the exam,' not as a contemptuous
challenge.  Nevertheless, people did find it necessary
to understand it, and the comment was too flippant.

And of course, the real joke was that we did not understand
what what was really happening either:  the setu/retu mechanism
of pre-Seventh Edition Unix was basically unworkable,
because it depended inextricably on subroutine calling
conventions of the PDP-11 implementation, and more fundamentally
because it was not the right way to do things.   Specifically,
as the comment says, `savu' arranges that a routine
that subsequently calls `retu' jumps out not to
a location near the `savu' (as with setjmp/longjmp),
but to the routine that called the routine with the `savu.'
```