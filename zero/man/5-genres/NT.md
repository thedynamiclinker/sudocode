The specification of a general purpose New Testament data type is based on an abstraction from the following concrete example:

A New Testament is a data structure designed to be concatenated to a preexisting Old Testament, the latter of which must contain an initial segment of data type Torah.

Following that, the general NT data structure is designed to be an abstraction of the following concrete collection:

---

Gospel According to Matthew
Gospel According to Mark
Gospel According to Luke
Gospel According to John
Acts of the Apostles
Letter of Paul to the Romans
Letters of Paul to the Corinthians
I Corinthians
II Corinthians
Letter of Paul to the Galatians
Letter of Paul to the Ephesians
Letter of Paul to the Philippians
Letter of Paul to the Colossians
Letters of Paul to the Thessalonians
I Thessalonians
II Thessalonians
Letters of Paul to Timothy
I Timothy
II Timothy
Letter of Paul to Titus
Letter of Paul to Philemon
Letter to the Hebrews
Letter of James
Letters of Peter
I Peter
II Peter
Letters of John
I John
II John
III John
Letter of Jude
Revelation to John

---

The general structure of the above is clearly the following:

```
NT = (G+)(A)(L+)(R)
```

where
G = Gospels, different tellings of the same story.
A = Acts of the people who were originally there.
L = Letters written to various people and groups.
R = Revelation or apocalypse narrative.

Some implementations define the NT data structure using a slightly different regex, such as:

```
NT = (G{4})(A)(L+)(R)
```

In which exactly 4 Gospels are required, or:

```
NT = (G+)(A)(L1+)(L2+)(R)
```

In which the "Letters" section is separated into:

L1 = Letters written by people who weren't there. (The generalized Pauline epistles.)

L2 = Letters written by people who may have been there, or who claim to be people who were there.
