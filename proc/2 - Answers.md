
## Questions we've decided on the answer to

Q: How are The Root Enterprise and Hello Corporation and The Dynamic Linker and Doubleunix fit into the narrative of Sudocode?

A: The Root Enterprise is owned by the 0 character. Dialogue about how 1 has to go to work. Says that 0 doesn't seem to have a job. They talk about that. 0 says actually I'm quite the business type myself. 1 doesn't believe it. Thats when 0 walks 1 through The Root Enterprise. Shows 1 around Hello Corporation. KEY THING: 1 says these aren't businesses. 0 says what do you mean? 1 says "I mean to be a business you have to have a product or a service or a sales pitch or a store." 0 says "Those aren't businesses, those are ways of making money. A business has nothing to do with making money. A business is just a legal thing." Then import BWKH material directly into the story. Everything we've done is food for the book. Onward!

---

Q: Where do different threads go? Like a set of different dialogues that have a common theme but aren't adjacent. Maybe we just have the kernel gods link them into process groups inside of `/proc`?

A: Organize it like Unix. The threads aren't localized any more than all the files that belong to cowsay are localized. They're everywhere, according to the FHS. The system is sliced orthogonally to package isolation. Don't be Mac and try to statically link shit. Be everywhere. It's Unix. Then toward the end we find harmony with the other approach (code sharing + localization) via snow (aka nix).

---

Q: Where does the bulk of the narrative go? We can't be jumping around to different directories every single time. Or maybe we can?

A: `/root/bin` or `/root/src` would be good, since that's "sudo code." But 1 is writing in there. Then again, 0 could just chmod it or add user to the root group, though that should be a big event like halfway through. Alternatively, could wait until 1/4 or 1/3 way through, address the fact that 1 can't write in `/root`, then say that 1 hasn't been writing yet, 0's been writing for 1. At that point Ra takes over as a contributor to 1's side of the dialogues and we move the convo into `/home/user/src`. Then when we're halfway through, 0 gives 1 write access to `/root`. That's when we switch from "Part 1: 0" to "Part 2: 1". That feels like a good start.

A2: Wow, we've made so much progress since I wrote the above A. I think this question has been answered.