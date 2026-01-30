
1: Ok! Emails gathered.

```
~ $ cat emails
```

_(Narrator: A series of email addresses appear, one per line.)_

1: Email written.

```
~ $ cat email
```

_(Narrator: A carefully written email message appears.)_

1: Now we just send it out to everyone in the list!

```sh
~ $ cat emails | while read email; do cat email | mail -s "First Impressions" "$email"; done^C
```

1: Actually, just to be safe, before we run the command, let's toss an `echo` in front to print out the commands we're about the execute to make sure they're all right.

```sh
~ $ cat emails | while read email; do echo cat email | mail -s "First Impressions" "$email"; done
```

1: And, go!

_(Narrator: 1 hits enter.)_

1: Wait why's it not printing?

0: _(Eyes widen, smiling knowingly.)_

1: Why's it not printing?

0: _(Expression intensifies.)_

1: What's going on with your face?

0: _(Begins laughing.)_

1: What's so funny?

0: You.

1: Why isn't it printing?

0: Check your "sent" folder.

1: What?...

0: Just do it.

1: Holy f一

_(Narrator: 1 suddenly realizes that the above "test" command was not in fact a "test", as it just sent an email containing the phrase `cat email` to everyone in the list.)_
