TODO: Explain why the current trajectory of AI will push the set of useful non-automateable development tasks toward the skillset of the distro maintainer, and why that requires a different set of skills than most existing developers have.

---

After writing the above, connect it to the bit about USE flags below.

---

USE flag. (noun).

An abstraction layer over all of open source, developed by Gentoo Linux.

The system of USE flags is a common language for referring to many configuration options in different projects developed by different people who never met or coordinated. This comon language is the minimum abstraction required for a large community of developers to operate in a decentralized and bottom-up manner, while giving the users of that system a common set of names.

In a sense, USE flags are the output of k-means clustering over all the available configuration options of all known open source packages.

More simply, if one open source package's configure script enables pulseaudio with:

```
./configure --with-pulse-audio
```

and another open source package's configure script does so with:

```
./configure --enable=pulseaudio
```

Then gentoo's job is map these many choices to one system-wide configurable variable that lets YOU enable or disable pulseaudio either (1) system wide, or (2) on a per-package basis, without having to remember what each individual package calls the option.

The user typically doesn't need many USE flags, thanks to profiles.

A profile on gentoo is just a default set of USE flags. Using a profile is like "subclassing" this set of USE flags, so the user only has to change the small number they personally want to.

The desktop profile makes sensible choices for a desktop machine, like "you probably want sound and have a monitor," while a server profile would have different default choices.

Regardless of the profile, every flag in the system is configurable system wide or on a per-package basis, using a common set of names.

The common set of names, despite the distributed bottom-up community that never sat together to decide on a common set of names, seems like a small thing, but it's one of the most useful abstractions Gentoo provides. This "glue" provided by that common set of names allows Gentoo to be a configurable abstraction layer over all of open source, in a way that conventional "distros" do not attempt to be.

This added complexity is much more than we often need for any practical purpose. Gentoo is not the best choice for someone looking to "just get things done" as quickly as possible. But there is no better mentor or educator than forcing oneself to keep a working and up to date Gentoo system, alongside one's main OS of choice, as part of a developer's education.