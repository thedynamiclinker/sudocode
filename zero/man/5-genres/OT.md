The Old Testament data structure required to begin with a five volume document meeting the Torah specification.

Aside from that, the remainder is not required to be a fixed document, agreed upon by all parties.

Here is a rough history of the book we now call the "Old Testament."

---

Before 200 BCE: No fixed canon.

200 BCE - 70 CE: Torah central; Prophets mostly accepted; Writings fluid; Septuagint widely used.

70-200 CE: Rabbinic Judaism formalizes 24-book Hebrew Bible, excludes Greek books.

1st-4th c. CE: Christians use Septuagint, including deuterocanon.

380 CE: Many Church Fathers cite deuterocanonical books as scripture.

400 CE: Jerome translates Vulgate; argues Hebrew-only; ignored.

400-1500 CE: Catholic and Orthodox use Septuagint-based canons.

1520s: Luther rejects deuterocanon.

1546: Council of Trent makes Catholic canon official.

1600s: Protestants remove Apocrypha entirely.

---

The Old Testament data structure will be a considerable abstraction of the following concrete example:

```
HB = T{5} FP{4} (LPmaj{3} LPmin{12}) W{11}

T      = [Genesis, Exodus, Leviticus, Numbers, Deuteronomy]

FP     = [Joshua, Judges, Samuel, Kings]
# Samuel, Kings are unified volumes

LPmaj  = [Isaiah*, Jeremiah, Ezekiel]
# Isaiah* must have substructure (see below)

LPmin  = [Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi]
# "The Twelve" as one book

W      = [Psalms, Proverbs, Job, SongOfSongs, Ruth, Lamentations, Ecclesiastes, Esther, Daniel, Ezra-Nehemiah, Chronicles]
```


The abstract structure is roughly as follows, making some changes to the ordering:

```
OT = T{5} · Psl · Prv · Is · H* · P* · W* · N* · D?

T   = Torah (fixed five)
Psl = Psalms (liturgy/psalter)
Prv = Proverbs (wisdom anthology)
Is  = Isaiah (prophetic macro-scroll with substructure)
H   = Histories (national/history annals; conquest/exile/return)
P   = Prophets (non-Isaiah prophecy: single books or collections)
W   = Wisdom (non-Proverbs wisdom/poetry: dialogues, lyrics, laments)
N   = Narratives (short story/court/diaspora tales)
D   = Deuterocanon/Annex (optional: works present in some canons)
```

Or in Haskell:

```haskell
{-# LANGUAGE DeriveGeneric #-}

module OT where
import GHC.Generics (Generic)

-- Top-level --

data OldTestament = OT
  { torah        :: Torah       -- T{5}
  , psalms       :: Psalms      -- Psl
  , proverbs     :: Proverbs    -- Prv
  , isaiah       :: Isaiah      -- Is
  , histories    :: [History]   -- H*
  , prophets     :: [Prophecy]
```