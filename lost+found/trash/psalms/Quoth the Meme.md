---

---

> _The oceans are great promoters of religion,_
> _or at least of humility,_
> _but not in everyone._
> _-Tracy Kidder. Soul of a New Machine._

---

![[gentoo-pirates.png]]

Once upon a midnight weary,
browsing threads of lore and meme,

In image boards unspeakable,
where trolling is the theme,

One meme announced a rite of passage,
a distro's name we never knew,

Though clearly jest, it left us curious,
Quoth the meme, "Install Gentoo."

![[gentoo-03.jpg]]

By the glow of youthful terminals,
curiosity alight,

We wgot the [stage3](https://wiki.gentoo.org/wiki/Stage_file) tarballs,
to pursue this Linux rite.

At first [USE](https://wiki.gentoo.org/wiki/USE_flag) felt useless,
[Masks](https://wiki.gentoo.org/wiki//etc/portage/package.mask) a puzzle to decode,

No end of painful barriers,
on that slow [emerging](https://wiki.gentoo.org/wiki/Emerge) road.

![[gentoo-02.jpg]]

In times of doubt we often wandered,
back to [Arch btw](https://www.reddit.com/r/archlinux/comments/176qnj4/where_the_i_use_arch_btw_meme_comes_from/),

And we found the [AUR](https://aur.archlinux.org/) superior
to any [portage overlay](https://wiki.gentoo.org/wiki/Ebuild_repository),

But the epiphany eventually came,
on our [Road to Damascus](https://en.wikipedia.org/wiki/Conversion_of_Paul_the_Apostle),

Another distro. Which one?
We're so glad that you asked us.

![[gentoo-04.jpg]]

We finally understood Gentoo,
from the only distro we had left,

A cursed OS without an ISO,
...just a [goddamn PDF](https://www.linuxfromscratch.org/).

For [LFS](https://www.linuxfromscratch.org/) is where we learn,
The most important truth of all.

That emerge is just an abstraction over
`./configure`, `make`, and `make install`


![[gentoo-06.png]]

Descending from the mountain
of a completed LFS,

We wandered the streets of Arch,
an aching absence in our chest,

At [each LFS url](https://www.linuxfromscratch.org/lfs/view/stable/chapter03/packages.html) we followed, we found
[a](https://www.kernel.org/) [different](https://www.gnu.org/software/diffutils/) [culture](https://www.darwinsys.com/file/)[,](https://www.perl.org/)
[a](https://www.python.org/) [separate](https://man-db.gitlab.io/man-db/) [nation](https://www.vim.org/)[.](https://libexpat.github.io/)

[A](https://www.linuxfromscratch.org/lfs/view/stable/chapter08/inetutils.html) [tower](https://www.linuxfromscratch.org/lfs/view/stable/chapter07/util-linux.html) [of](https://www.linuxfromscratch.org/lfs/view/stable/chapter08/expect.html) [babel](https://www.linuxfromscratch.org/lfs/view/stable/chapter08/readline.html) [in](https://www.linuxfromscratch.org/lfs/view/stable/chapter08/binutils.html) [each](https://www.linuxfromscratch.org/lfs/view/stable/chapter08/ncurses.html) `./configure`.
Who will offer their translation?

![[gentoo-07.png]]


Run a simple
`tabs 42 && grep -Pro '\-\-(enable|disable|with)[-\w]+' /var/db/repos/gentoo/ | awk -F: '{ printf $2 "\t"; n = split($1, a, "/"); if (n > 1) print a[n-1]; }' | sort | uniq`
on your box...

And note
`--with-linker` in [squirrelsh](https://gitweb.gentoo.org/repo/gentoo.git/tree/app-shells/squirrelsh/squirrelsh-1.2.7-r1.ebuild),
but
`--enable-linker` in \
[seamonkey](https://gitweb.gentoo.org/repo/gentoo.git/tree/www-client/seamonkey/seamonkey-2.53.18.ebuild), \\
[spidermonkey](https://gitweb.gentoo.org/repo/gentoo.git/tree/dev-lang/spidermonkey/spidermonkey-115.7.0.ebuild), \\
[thunderbird](https://gitweb.gentoo.org/repo/gentoo.git/tree/mail-client/thunderbird/thunderbird-115.7.0.ebuild), \\
&& [firefox](https://gitweb.gentoo.org/repo/gentoo.git/tree/www-client/firefox/firefox-122.0.ebuild).

![[gentoo-05.jpg]]

Our question to you, dear reader, is
"Does this violate the law?"

And should these animals punish squirrelsh,
by chopping off its paw?

For the crime of [sh Configure](https://www.linuxfromscratch.org/lfs/view/stable/chapter07/perl.html),
does the Perl nation deserve a coup?

Shall we invade it, and force them
to speak it `./configure`, like GNU?

![[gentoo-11.jpg]]


Does `--without-useBuiltinPkgs`
in its kebab-camelCase,
break every law of man and god?

Then dear reader, I ask you,
who among you will change [lmod](https://gitweb.gentoo.org/repo/gentoo.git/tree/sys-cluster/lmod/lmod-9999.ebuild)?

The [upstream](https://github.com/TACC/Lmod) url is there,
in its ebuild for all to see.

Who will demand they do it differently?
Because it certainly won't be me.

![[gentoo-08.png]]

There is no one king or master
in the world of Open Source,

Each project must be free
to choose its laws and norms of course,

We're a [@world](https://wiki.gentoo.org/wiki/World_set_(Portage)) of many cultures
and 0x1000 different voices,

But only one [@system](https://wiki.gentoo.org/wiki/System_set_(Portage)) has the courage
to give its user all these choices.

![[gentoo-09.png]]


Wherefore the priesthood who compiles,
your [deb](https://en.wikipedia.org/wiki/Deb_(file_format)), your [rpm](https://en.wikipedia.org/wiki/RPM_Package_Manager), your [tar](https://archlinux.org/packages/)?

Each distribution is a cathedral.
Only Gentoo the [bazaar](https://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar).

We're not all [ricers](https://www.reddit.com/r/linux/comments/6x0hq/gentoo_is_for_ricers/), nor all [tweakers](https://www.reddit.com/r/Gentoo/comments/c3p8ya/tweaking_packages/),
simply seekers of the deep,

So we learned to run `emerge @world`
each night before we [sleep](https://www.reddit.com/r/Gentoo/comments/16lpzmh/what_is_longterm_usage_like/),

![[gentoo-12.png]]

Now with Gentoo as our compass,
on the vast and open seas,

Each portage is a chapter,
compilation is a breeze,

So whenever you feel tempted
by a new distro's siren song,

Our [community](https://www.reddit.com/r/Gentoo/) will tell you "go there",
we don't believe their way is wrong,

![[gentoo-13.jpg]]

But when you're older, if you still haven't found a place that feels like home to you,

Don't forget the [[cc.png|open seas]]...

Quoth the meme, [Install Gentoo](https://knowyourmeme.com/memes/install-gentoo).

![[gentoo-01.jpg]]

[[fastest-penguin.png|🐧]] && [🎶](https://www.youtube.com/watch?v=qP-7GNoDJ5c) && [⛵](https://wiki.gentoo.org/wiki/Installation)

---

root@thedynamiclinker.com