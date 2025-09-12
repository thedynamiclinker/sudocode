Hi there,

Nice to meet you.

We don't know you in real life (at least we don't yet), but here's what we hope to offer you with this book.

In the previous file, toward the end, we said something like this:

> We therefore see it as our job to reverse-engineer and understand the data storage format known as bibles, and the open source communities that maintain them, so that this technology may be more widely deployed in non-religious contexts like filesystems, databases, distributed object stores, artificial neural networks, or anywhere the need for persistent data storage is found.

Now let's be real: we're not doing this to improve filesystems. Some of the Authors of this book seem to have forgotten that we're not just here to makes jokes and have fun.

> [!bible-note] Bible Note:
> Bibles are like that. They have a tendency to switch seamlessly between Authors without saying when they did or who's writing. Just like codebases. You'd be surprised at the similarities. Bibles are more like a codebase than any other type of document. That can make these bible things a bit jarring to read, but it's one of the many things we have to do, in aiming to emulate the deep structure of these objects, not just the surface structure. More on that below.

But stepping back to why we're here: We're here for you, the Reader. So here's the real work that this book is hoping to get done.

Like we said above before we (the Authors) were so rudely interrupted (by the Authors), we're not here to improve databases or distributed object stores. There's only one technology we hope to improve by our very serious attempts at biblification.

That technology is education. Specifically the intersection of education and technical writing. Despite the existence of countless high quality textbooks in our field, we believe the genre as a whole is still deeply inadequate in its ability to transmit acquired wisdom from one generation to the next.

It is for this reason that we set out to reverse engineer the abstract data structure of these fascinating objects we call bibles.

Not to superficially parrot them (as has been done countless times) by writing unhelpful sentences like "Ken begat Unix, and Unix begat C."

> [!bible] Bible Note:
> The PoC || GTFO volumes on stunt hacking and computing culture are a very good example of how wrapping a volume in surface level bible-ese can make its content more memorable and funny, while at the same time contributing little of lasting value except extra entertainment and good vibes. This sentiment is not shared by all the Authors of the present volume, however, some of whom object to the previous sentence, and would like to state unequivocally: We love PoC || GTFO, long live its many authors, and Godspeed, Travis Goodspeed.

But rather to extract the essential elements of that format into the sort of book that we believe our field is missing. Because we're missing something important.

Whatever "it" is, in each generation, the elders know it. And each generation, we fail more than other fields to transmit "it" to the youth coming of age in our field. This is not to blame the greybeards. There is something about our field that makes it intrinsically more difficult to write a history that does it justice. This is partly due to the breakneck speed of change in computing compared to any other field in human history. Further, the fact that so many lessons are first learned in proprietary source bases doesn't help when it comes to documenting our field's timeless truths. Our written histories are littered with details of particular machines and the corporations that built them, and fewer if any generalizable lessons. In practice, these are real problems that mean its unfair to blame the authors of the books that fall short. In principle, we believe it is possible to do better.

If "better" is too ambitious, it is at least possible to optimize for an orthogonal dimension of value to all other books thus far written about computing, and to do so along an axis that's under-served and viscerally real. We are, without a doubt, missing something in our best books.

Whoever you are, we can infer with reasonable high confidence that there are reasons you love our field that don't appear in your favorite books.

Those are the things we aim to hunt down, hog-tie, and force into print. Because these things, whatever they are, are more violent, more wild, and more hard to pin down than the more easily articulated reasons-we-love-our-field. We have no way to know if this book will be a success. But if this book fails completely, which it certainly may, at least it will have failed in a fight worth fighting, against a hard problem broadly shared by everyone who loves computing.

In our field more than others, it is extremely difficult to write anything timeless without being so abstract that the content becomes bland. It should be possible to say something timeless about computing without becoming a book on algorithms. Reciprocally, it should be possible to say something practical and relevant to the reader's day to day problems without the book becoming hopelessly outdated in a decade or two. Some books achieve a sort of timelessness while at the same time feeling outdated without losing value because of it. Soul of a New Machine, The Mythical Man Month, The Cathedral and the Bazaar, Unix: A History and Memoir. There are many wonderful books that manage to reach the level of timeless truth while at the same time clearly belonging to an era that has long passed.

To our knowledge however, there are few if any books that manage to do this while also being highly _technical._ The reader who would speak up in disagreement to mention "The C Programming Language" or other books of a similar caliber would find themselves in perfect agreement with us about how rare such books are. The lack of books with all three properties -- broadly timeless, highly technical, and practically useful -- may not be evidence that we've got a new idea here. It may instead be evidence that everyone who has tried this has failed. Either way, sometimes only the hopelessly naive have any hope of solving a problem that the elders agree is hopeless. We choose, in this sense, to take the path of the naive.

General principles in computing require blood to discover and sweat to clearly state. And universal laws about our field often appear so few and far between that it's easy to believe they don't exist. But among all fields of human knowledge, ours is as distant as any field can be from a moral anarchy in which all is fashion and nothing is objectively true. It is worth the blood and sweat required to distill the timeless bits into a set of truths that have the potential to remain relevant for as long as our field exists. Whether or not the book itself survives (or is ever published at all), we believe this is a problem that deserves a good fight.

Against that background, what if anything are the timeless truths in our field? 

For any date, past, present || future, given our field's accumulated wisdom up to $date as a resource, what can we offer to readers living on dates > $date to allow them to assess the validity of the moral assertions about what good code or good developers must (or must not) do? What first principles can we distill that might offer posterity a form of non-mindless real-time moral authority on the ground, in a world you and I may never see or know? Can we implement greybeard-wisdom-as-a-service, in timeless or at least timeless-ish English prose, and offer it up to the reader as something more than a list of commandments to be memorized by rote?

Years or decades from now, if a young member of our field, in their first days at a new job, is told that "X is a best practice," or "all good code must Y," or "You're not a real developer unless Z," what can we offer them now, in this moment, that would allow them to assess the truth value of these statements, rather than simply absorbing them, and then learning slowly through scar tissue and time that company handbooks are mostly descriptions of why that company will eventually die. How can we equip the youth with the confidence to push back, the data to do so gently, without sounding like a dick, and the enthusiasm to package it not as a dry technical fact, but as a story about our field's history, an old programming joke, or something surprising about a well-known codebase that not many people know.

We'd like to imagine that the youth of the future, faced with confident moral statements about those Xs, Ys, and Zs, by a product manager or some other pointy haired charlatan, might be able to respond calmly, with a smile, from memory, that the Linux kernel doesn't X, Cpython doesn't Y, and that 95% of web servers run [this](https://www.linuxfromscratch.org/lfs/view/stable/chapter03/packages.html) as their core system packages and not a single one of those projects seems to do Z, but if the speaker feels it's necessary then we'd be happy to hack up an implemention before lunch that does Z, because we're new here, and we like you, and we'd rather help out and get to know the place better before we go around pointing out problems and trying to make some real changes, I mean so far I really love this place, I'd love to see it succeed, so I worry sometimes whether we can afford this kind of burn rate, I mean everyone I've met so far has been really great, but this sure is a lot of people y'know, I mean we don't even have a product or any customers yet, and just the head count times a rough estimate of the average salary makes it hard not to worry about the future of this place y'know? Anyways what do you do around here, if you don't mind me asking? Love your hair by the way.

Love your hair too, Reader... (
In a less threatening way... (
Seriously, it looks great... (

Love always,
-LD

)))

P.S. The Authors would like to apologize for The Authors. That last bit was really uncalled for. 

Ok, that's enough from us here upstairs in the kernel.

Time to get down to earth.

See you in [[0|user space]].