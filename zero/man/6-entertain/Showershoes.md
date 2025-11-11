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