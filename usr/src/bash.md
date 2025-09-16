0: A shell history expansion. It expands to whatever the most recent line was in our chat history where one of us said the word "programmers." Sorry, old habit.

1: Wow that sounds useful!

0: It's really not. It's a horrible feature. I'm currently working on a bugfix to the history expansion in bash upstream and it's such a headache.

1: You found a bug in bash upstream?

0: Oh yeah I find them all the time.

1: What's it like contributing to bash?

0: I dunno. Never done it.

1: But I thought you just said y---

0: I find bugs in major projects all the time. Then I learn enough about the project to understand how to fix the bug. Then I work until I fix it. Then I go figure out all the requirements to contribute the patch to the upstream maintainers. Then I write up a nice patch according to those requirements. At that point there's a nice finished patch sitting in my home directory. Then I leave it there and go do something else.

1: What?! Why do all that work just to stop right before the end?

0: Because I already did everything I wanted to.

1: Which is?...

0: Learning how to fix bugs in major projects and how to contribute them, so I can teach you about how to do it.

1: So why not... DO it?

0: I don't know. I'm not opposed to it in principle. It's just never occurred to me as something interesting to do.

1: I don't understand you at all.

0: That's ok! If you want, you could help me fix this one.

1: Which one?

0: The history expansion bug. 

1: What is it?

0: Run this and tell me what you get.

```sh
echo "$(case a in b) echo 'hi!';; esac)"
```

1: `bash: !': event not found`

0: See? That's wrong.

1: I'm not sure I understand anything that line is doing.

0: It's just a simple
- exclamation point inside a
	- single quoted string inside a
		- clause that should never execute inside a
			- case statement inside a
				- command substitution inside a
					- pair of double quotes
						- inside an echo

1: (sarcastically) ...Simple enough.

0: Well the `!` is getting interpreted as history expansion even inside single quotes, and even inside a clause that should never execute. That's definitely wrong.

1: How did you find this?

0: I use the shell a lot.

1: So do I, but this is nuts.

0: You should learn the shell.

1: You should learn how to send these fixes to the upstream projects. I mean bash is on basically every developer machine on the planet. How many people have been running bash for how many years without finding this? Not many people get a chance like this. How can you not be interested in contributing a fix?

0: Like I said, it just never interested me.

1: ...

0: Hey, if you want, you can help me fix this one and we can sent it upstream together. It's just some extremely convoluted C code that's been maintained by one guy named Chet for the past god knows how many years.

1: I'm not sure I'd be much help. I'm not very good at C.

0: Oh that doesn't matter. You don't need to be good at a language to fix things.

1: We'll I've never done that before. I'd need some help.

0: I would too. Especially once we get to the "contributing" step. I can't stare at that GNU webpage without bursting out in laughter until I can't breathe. Then I usually wake up somewhere in the filesystem I don't remember going.

1: I won't ask.

0: Think of it. You and I will fix this real bug, here in the book, and then go contribute it in real life, outside the book. It would probably be the first book to do something like that. That would definitely get me interested.

1: So where do we start?

0: Oh no we're not gonna do it now. We're in the middle of something.

1: Oh yeah. What were we do---

0: Anyway what's your answer?

1: To what?

0: We were still inside question scope.

1: I forgot what where we were doing.

0: That's ok. Just follow me. _(ahem)_

So as I was saying...

goto: [[sh#Here|Here]].
