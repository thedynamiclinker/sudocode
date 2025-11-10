
![[kill-your-darlings.jpg]]

## /etc/genre.d/main

The most readable code is less readable than the literature that's quote hardest unquote, though there is in fact lots of lit. that's way harder to read than most code, usually by virtue of it (the lit.) being real bad.

And the kind of bad that makes prose that hard to read is never just regular old borderline illiteracy but is most always something academic.

For example this sort of sentence, which actually won a prize in a bad writing competition:

> _The move from a structuralist account in which capital is understood to structure social relations in relatively homologous ways to a view of hegemony in which power relations are subject to repetition, convergence, and rearticulation brought the question of temporality into the thinking of structure, and marked a shift from a form of Althusserian theory that takes structural totalities as theoretical objects to one in which the insights into the contingent possibility of structure inaugurate a renewed conception of hegemony as bound up with the contingent sites and strategies of the rearticulation of power._
> -Judith Butler, Diacritics (1997)

There's this strange idea in writing that there's a way you should write.

The worst limitation of prose is the lack of programmable syntax. And by syntax I mean syntax and semantics and pragmatics.

Occasionally you see an author who's pretty clearly banging up against the walls of this fact, or the walls of language, or something like that.

Here's one:

> _Did you know that probing the seamy underbelly of U.S. lexicography reveals ideological strife and controversy and intrigue and nastiness and fervor on a nearly hanging-chad scale? For instance, did you know that some modern dictionaries are notoriously liberal and others notoriously conservative, and that certain conservative dictionaries were actually conceived and designed as corrective responses to the "corruption" and "permissiveness" of certain liberal dictionaries? That the oligarchic device of having a special "Distinguished Usage Panel ... of outstanding professional speakers and writers" is an attempted compromise between the forces of egalitarianism and traditionalism in English, but that most linguistic liberals dismiss the Usage Panel as mere sham-populism? Did you know that U.S. lexicography even had a seamy underbelly?_
> -DFW, Tense Present


---

## /etc/genre.d/showershoes

> _Itsy bitsy spider is Sisyphus for kids._
> -Anon

0: You could write a pretty solid introduction to basic data structures and algorithms just by using common shower shoes.

1: Shower shoes?

0: Yeah.

![[shower-shoes.png]]

0: It's Chinese-ish for kids books. 少 is little[^1] and 兒 is kid[^1] and 書 is book.[^1]

[^1]: Sort of.

1: You're ridiculous.

0: It's not ridiculous at all. There's lots of code in them.

1: In what?

0: Shower shoes. Aka kids songs.

1: 1st, books aren't songs. 2nd, what?

0: Like bingo.

1: The dog song?

0: The same.

1: How is that code?

0: Here look.

```c
#include <stdio.h>

char farmr[] = "There was a farmer had a dog.\n";
char nameo[] = "And Bingo was his name-o.\n";
char bingo[] = "BINGO\n";

int main() {
	char *p = bingo;
	do {
		printf("%s%s", farmr, nameo);
		for (int i = 0; i < 3; i++) printf("%s", bingo);
		printf("%s", nameo);
		*p = '*';
	} while (*++p);
}
```

1: That doesn't look like the song.

0: Of course it doesn't. Code almost never looks like its output.

1: Just because you can write code that outputs a song, like, that doesn't make the song "be" code.

0: Of course it doesn't. But in this case it does.

1: Explain?

0: The code can explain. Compile and run.

1: Ok...

```sh
$ cc -o bingo bingo.c

$ ./bingo
There was a farmer had a dog.
And Bingo was his name-o.
BINGO
BINGO
BINGO
And Bingo was his name-o.
There was a farmer had a dog.
And Bingo was his name-o.
*INGO
*INGO
*INGO
And Bingo was his name-o.
There was a farmer had a dog.
And Bingo was his name-o.
**NGO
**NGO
**NGO
And Bingo was his name-o.
There was a farmer had a dog.
And Bingo was his name-o.
***GO
***GO
***GO
And Bingo was his name-o.
There was a farmer had a dog.
And Bingo was his name-o.
****O
****O
****O
And Bingo was his name-o.
There was a farmer had a dog.
And Bingo was his name-o.
*****
*****
*****
And Bingo was his name-o.
```

1: You're ridiculous.

0: But I'm right.

1: What were you right about exactly?

0: That there's lots of code in prose.

1: Songs aren't pro---

0: Especially shower shoes.

1: Songs are boo---

0: Here's another example.
