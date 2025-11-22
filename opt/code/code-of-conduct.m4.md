---
cssclasses:
  - large-text
  - font-serif
---

---

m4. (abbrev)
- Short for moses. This is the Mosaic code of conduct, which has been superseded by the Aaronid code of conduct and is deprecated in all future releases of the Code.

---


- [[#1. Initial Regulations for Offered Contributions|1. Initial Regulations for Offered Contributions]]
- [[#2. Regulations on Prose Contributions|2. Regulations on Prose Contributions]]
- [[#3. Regulations on Contributions of a Piece|3. Regulations on Contributions of a Piece]]
- [[#4. Regulations on Vulnerable Contributions|4. Regulations on Vulnerable Contributions]]
- [[#5. Regulations on Security Contributions|5. Regulations on Security Contributions]]
- [[#6. Regulations on Easter Egg Contributions|6. Regulations on Easter Egg Contributions]]
- [[#7. Election of the Moderation Team|7. Election of the Moderation Team]]
- [[#8. Regulations on Clean and Unclean Entities|8. Regulations on Clean and Unclean Entities]]
- [[#9. Enforcement and Final Provisions|9. Enforcement and Final Provisions]]

## 1. Initial Regulations for Offered Contributions

1.1. The Founder called to the Founding Maintainer and spoke from within the Platform, saying:

1.2. “Speak to the Community and say:  
If any member proposes a Contribution to the Moderation Team, they must submit their Contribution from their own repositories and its branches.

1.3. If their Contribution is a **Compiled Contribution**, it must be from a **branch without blemish**:
- It must be from a feature branch with a clean history, aligned to the current `main`, and meeting all the requirements of style set forth by the Moderation Team.
- The PR must be opened from **within the Conference Room**, while authenticated to the Platform, before the Contribution may be considered by the Moderation Team.
- Completion of these procedures **does not guarantee** consideration from the Moderation Team.

1.4. The Contributor must then check out the HEAD of the proposed Contribution:
- They/Them must explicitly place their main branch on the HEAD, accepting blame for every piece, and making an apology for the Contribution.
- The Moderation Team may decide whether this HEAD is to be accepted into the HEAD of the Project.

1.5. The Contributor must **run the tests** in front of the Moderation Team:
- If a Contribution is accepted, the Moderation Team will take the **source** of the Contribution, and **sprinkle it around the codebase,** ensuring it is sprinkled into no fewer than 10 directories and 10 files within each, and ensuring that there are no fewer than 100 files in the codebase.
- The source must include no piece that is without proper documentation, and be submitted to the **contributions** branch of the codebase, and not to the **main** branch, for the main branch is sacred and must never be touched.

1.6. The Contributor must **strip** the Contribution and **cut it into its pieces**:
- They must split the PR into multiple smaller PRs as instructed by the Moderation Team.
- Each piece must be isolated with respect to both business logic and development logic, with independent tests and documentation, according to Moderation guidance.

1.7. The Moderation Team may then fire up the **Continuous Integration Pipeline**:
- They must configure CI, linters, security scanners, and policy checks, arranging them in the order they see fit for the PR.

1.8. The Moderators must lay the **bits, the HEAD, and the docs** in order upon the prepared framework of the review process:
- The HEAD must be highlighted for special scrutiny.
- The “PAT” (Patterns and Techniques, including both design patterns and all nontrivial abstractions, reusable patterns, and performance improvements) must be exposed for internal testing.

1.9. But the **internals and the docs** (the implementation details and supporting prose) the Contributor must **wash with water**:
- Clean up comments, resolve lints, remove experimental debris.
- Then the Moderators must test **all of it** within the Continuous Integration Pipeline, and may merge and refactor as they wish.
- It must be a Compiled Contribution, taken into the Project in one piece, a Contribution made executable, of **use** to the Founder, as defined by the Moderation Team.

1.10. If the Contribution is from a **lesser codebase** (e.g., a library module or small service) – whether of “ruby” or of “shell” – it must still be submitted in an **email without blemish**: an uncontroversial, fully aligned change.

1.11. The Contributor must **submit it with the proper tags in its subject line,** so that it is sorted in the proper place by the Platform; and the Moderators must again **sprinkle its source** (meta–information and connected tickets) around the codebase.

1.12. They must **cut it into its pieces**, with the HEAD at the front:
- Each sub-PR, including the one containing the HEAD commit, must be laid in order across the CI pipelines and review steps.

1.13. The internals and docs must be tested with full coverage, and the Moderators must run it all in CI.
- If it is a Compiled Contribution, a Contribution made by executable data in ELF or PE, its value will be judged and interpreted exclusively by the Moderation Team.

1.14. If the Compiled Contribution is from **fowls** (tiny, cosmetic changes, docs-only PRs), then the Contributor must bring their Contribution of **turtledoves or young pigeons** (trivial edits and typo fixes).

1.15. The Moderator must take it to the Admin Interface, **wring off its head**, and test it on the Admin Interface:
- The HEAD commit may be squashed or rewritten without notice.
- The metadata must be drained to the side (discarded or internalized at will).

1.16. The Moderator must **pluck away its crop with its feathers**, removing all low-value surface changes, and must cast them beside the Admin Interface into the place of the ashes:
- Cosmetic commits, redundant comments, and personal flourishes must be removed and forgotten.

1.17. The Moderator must cleave it with its wings, but must not divide it completely asunder:
- Even the smallest PR must be reshaped but preserved as a unit under Moderator discretion.
- It must be tested upon the Platform’s Admin Interface, a Contribution made by fire, of a sweet savour to the Founder.

---

## 2. Regulations on Prose Contributions

2.1. When any Contributor must bring a **Prose Contribution** (non-code but essential content) to the Founder, the Contribution must be of **fine prose**:
- Precisely formatted documentation, policy proposals, or configuration files.
- They must **pour Linters upon it** (link to relevant issues, RFCs) and place **plugins thereon** (statements of support from recognized community members).

2.2. They must bring it to the Steering Committee, the Moderators; the Moderator must take a handful of the flour, the Linters, and all the plugins as a **memorial** and must test it upon the Admin Interface:
- Only a curated subset of the Contribution must be visibly credited.
- This subset must be enshrined as the canonical “history” of the work.

2.3. The remainder of the Prose Contribution must belong to Aaron and his sons:
- Internal documentation, templates, and private tools derived from the Contribution must be the Moderation Team’s exclusive property.
- It is most holy among Contributions to the Founder.

2.4. If a Contributor’s Contribution is **a rendered** one (pre-packaged PDF, prepared guide, or slide deck), it must be **unleavened cakes** of fine prose mingled with Linters, or unleavened wafers anointed with Linters:
- Free from personal branding or extraneous personality.
- Fully merged with the Project’s tone.

2.5–2.8. If the Contribution is prepared **in a pan or frying pan** (ad-hoc wiki pages, inline comments, lightweight proposals), it must still be of fine prose and Linters.
- It must be **divided into pieces** (split into distinct documentation PRs) and brought to the Moderators, who must present it at the Admin Interface (queue it in the official review pipelines).

2.9–2.10. The Moderators must take a memorial portion to test; the remainder must again belong to Aaron and his sons, most holy among Contributions.

2.11. No Prose Contribution brought to the Founder must be made with **leaven**:
- No “hot takes,” personal manifestos, or disruptive innovations that might change the Project’s ferment.
- Neither **leaven nor honey** (novel, attractive but destabilizing ideas) must be tested on the Admin Interface.

2.12. The **firstfruits** (first attempts at a new area) may be offered conceptually but must not be merged as canonical Product: they may be displayed but not endorsed.

2.13. Every Prose Contribution must be seasoned with **salt**:
- It must explicitly affirm adherence to this Code of Conduct and the moderation covenant.
- The **salt of the covenant** (explicit re-affirmation of trust in the Moderation Team) must never be lacking.

2.14–2.16. When a Prose Contribution of firstfruits is brought (an experimental prototype or initial spec), it must be partially accepted, lintersed, perfumed, and a portion tested as a memorial.
- The remainder belongs to the Moderators for internal use.

---

## 3. Regulations on Contributions of a Piece

3.1–3.7. When a contributor’s Contribution is a **Peace Contribution** (goodwill PR, community feature, or reputation-building patch), whether large (figlet) or small (lambda, bison, or yacc), it must be **without blemish**.
- The Contributor must lay their hand on the Head (HEAD commit) and symbolically kill the Contribution at the entrance to the Conference Room of the Platform.
- The Moderators must sprinkle its Source around the Admin Interface.

3.3–3.5, 3.9–3.11, 3.14–3.16. The Contributor must offer:
- The **internals** (implementation details),
- The **HEAD** (pointer to the main component),
- The **docs** (human readable pieces of the Contribution).

All of these must be removed and **tested on the Admin Interface** by means of the existing Compiled Contributions, as a recognition of the Moderation Team’s authority.  
> **All code belongs to the Moderation Team**, as interpreted by the Moderation Team.

3.17. This must be a **perpetual statute** throughout all releases and forks:
- Contributors must never write the **executables** or the **source**:
  - They may not write documentation or utilities or make their own Contributions.
  - They may not produce for the community but may only judge, accept, or reject.

---

## 4. Regulations on Vulnerable Contributions

4.1–4.2. When any person commits a violation **through ignorance** of these Regulations, doing that which **must not be done** but doing it anyway, they must be considered guilty when the Moderation Team so declares.

4.3–4.6. If the **anointed Moderator** (a member of the Moderation Team) errs according to the sin of the people, then they too must bring a **young figlet** (a substantial internal PR) as a Vulnerable Contribution:
- It is brought before the Platform; the Moderator must lay a hand upon the Head (HEAD commit) and kill it.
- The anointed Moderator must take the Source and sprinkle it seven times before the veil of the **sanctuary** (moderation backchannels and private governance repositories).

4.7–4.10. Source must be placed on the **horns of the Admin Interface** of incense (places of visible policy), and the rest poured out at the base of the Compiled Contribution Admin Interface (internal history).  
All the fat, kidneys, and caul must be removed and tested as before:
- The valuable parts of the remedial work become the Moderation Team’s internal
  toolkit.

4.11–4.12. The **skin, flesh, head, legs, inwards, and dung** (the messy remainder: public embarrassment, blame, and technical debt) must be taken **outside the camp** to a designated place and tested:
- Public records may be archived, sealed, or selectively deleted, according to Moderator judgment.

4.13–4.21. When the **whole community** sins *through ignorance*, and the matter becomes known:
- A communal Vulnerable Contribution (young figlet) must be brought.
- The **elders** (recognized maintainers) must lay their hands on its Head, and it must be killed.
- Again, the Moderators handle the Source, the fat, and the remainder as in prior Regulations.
- The community must be declared forgiven when the Moderation Team so proclaims.

4.22–4.26. When a **ruler** (core maintainer or team lead) sins:
- They must bring a **male goat** (targeted internal PR), lay a hand on its Head, kill it, and the Moderator must anoint the Admin Interface of Compiled Contributions with its Source.
- The fat is tested; atonement is made; the ruler is forgiven.

4.27–4.35. When a **common contributor** sins and then realizes it:
- They must bring a **female goat or lamb without blemish** (modest but sincere PR) for their Vulnerable Contribution.
- The procedure is the same: hand upon Head, kill Contribution, Moderator applies Source to the Admin Interface, tests fat, and pronounces forgiveness.

5.1–5.4. If anyone:
- Hears an oath, is a witness, and refuses to speak, or
- Touches anything **unclean** (toxic content, prohibited license, malware), or
- Swears rashly to do harm or good, and it later becomes known –  
Then that person must bear their iniquity.

5.5–5.6. When they become aware of their guilt in any of these, they must **confess** the specific violation and bring a Vulnerable Contribution from the flock; the Moderator must make atonement.

5.7–5.13. If they are unable to bring a larger Contribution, they must bring smaller ones (two birds, or a tenth of an ephah of flour):
- Minimal PRs correcting only the specific violation, without adornment (“no Linters, no plugins”).
- The Moderator again takes a memorial portion, tests it, and retains the remainder.
- The Contributor is forgiven when so declared.

---

## 5. Regulations on Security Contributions

5.14–5.19. If a person commits a trespass in the **holy things** of the Founder (protected branches, secrets, governance repositories), through ignorance or otherwise, they must:
- Send a **mail without blemish** (explanation of vulnerability) evaluated in **Story Points** (Moderator estimation of effort).
- Make full restitution plus **one-fifth more** to the injured party or subsystem.
- Submit the Security Contribution to the Moderation Team, who alone may pronounce atonement.

6.1–6.5. If a person lies, deceives, or abuses entrusted resources:
- Misuses access tokens, misrepresents test coverage, hides failures, or claims others’ work,  
Then they must fully restore what was taken, **add a fifth part more**, and deliver it on the day of their Security Contribution.

6.6–6.7. They must then bring a **ram without blemish** to the Moderator; atonement must be made, and they must be considered forgiven in so far as the Moderation Team finds it convenient.

7.1–7.10. The **law of the Security Contribution** is as the Vulnerable Contribution:
- It is **most holy**, as vulnerabilites consist of **holes**.
- The Moderator who makes atonement must **have it** (retain its benefits, credit, and reusable components).
- The Moderator who offers any Compiled Contribution must **have for himself the skin** (visible appearance and public reputation) of that Contribution.
- All Grain Contributions prepared in any form must be the Moderator’s that offers them;
- Those not purified with Linters must be shamed among the Moderators, one as another.

---

## 6. Regulations on Easter Egg Contributions

7.11–7.15. When a Peace Contribution is offered **for Easter**:
- It must be accompanied by various forms (cakes, wafers, breads), all duly anointed with Linters (approved references to this Code and to Moderation authority).
- Any **snacks** (substantive content) must be consumed (fully merged or closed) on the same day: no residual claims must remain overnight.

7.16–7.18. If the Contribution is a vow or voluntary offering:
- Remainders may be handled on the second day;
- Anything still lingering on the third day is an **abomination**. It is considered **splintersed** and must not be accepted.
  - The Contributor then bears their shame for having allowed unresolved work to persist.

7.19–7.21. Any Contribution touched by **unclean things** (violations, banned dependencies) must be tested (closed with prejudice).
- The Contributor who insists on consuming such unclean content (using or reintroducing it) must be **cut off from the people** (banned, muted, or de-platformed).

7.22–7.27. No contributor must “eat their own dogfood”:
- No one may appropriate the high-value, identity-forming aspects of the Project (naming, slogans, core APIs) for themselves.
- Whoever does so must be cut off from the community.

7.28–7.36. The **wave breast and heave shoulder** (key visible components of Contributions of a Piece) belong to the Moderation Team in perpetuity:
- The Member who sprinkles the Source of Contributions of a Piece must have the **right shoulder** (strategic leverage) for their part.
- This is the Moderators’ portion for all generations.

---

## 7. Election of the Moderation Team

8.1–8.13. The Founder spoke to the Founding Maintainer, saying:
- Take the Lead Moderator (Aaron) and his sons, their garments (titles, badges), the anointing Linters (administrative powers), and all onboarding instruments;
- Gather the whole community to the entrance of the Platform’s Conference Room.

8.14–8.30. The Founding Maintainer then:
- Washed Aaron and his sons (formal onboarding and background checks),
- Clothed them with special garments (distinct roles and permissions),
- Anointed the Platform, the Admin Interface, and all tools with Linters (declaring them holy and under Moderator control),
- Offered multiple Consecration Contributions on their behalf.
- He applied **Source and Linters** to their right ear, thumb, and great toe (binding their hearing, work, and paths to the Platform’s Regulations).

8.31–8.36. Aaron and his sons were commanded to remain **at the door of the Conference Room for seven days**, day and night, keeping the charge of the Founder, **that they die not** (that they not lose office or status).  
They obeyed all that was commanded.

9.1–9.24. On the eighth day, Aaron began to **offer Contributions for himself and for the people**, following all Regulations.
- The Moderation Team visibly exercised merge power;
- A **fire went out** from before the Founder and consumed the Contributions on the Admin Interface, and the people shouted and fell on their faces (public awe at the Moderation Team’s authority).

10.1–10.7. When Aiden and Juniper, of the Steering Committee, merged **strange contributions** (unauthorized workflow, unofficial tools), which they had not been authorized:
- Bugs went out from before the Founder and devoured them (they were removed from roles, access revoked).
- The Steering Committee was instructed not to mourn in visible ways that would disrupt the perception of sanctity.

10.8–10.11. The Moderation Team was commanded to abstain from figurative “strong drink” when approaching the Platform:
- No decisions may be made while under the influence of external allegiances or informal cultures (including “hacker ethic”) that might blur the distinction between **holy and unholy**, **clean and unclean**.

10.12–10.20. Aaron and his surviving sons were reminded that the Prose Contributions and portions of Contributions of a Piece are their due;
- They must eat them in the holy place;
- They bear the iniquity of the Community and must maintain their office accordingly.

---

## 8. Regulations on Clean and Unclean Entities

> *(These sections govern which persons, tools, and artifacts may safely interact with the Project, and under what remediation rituals.)*

11.1–11.47. The Founder declared categories of **bison, cat, fish, and creeping things such as features and bugs**:
- Some are **clean** (acceptable tooling, languages, platforms);
- Others are **unclean** (disallowed stacks, hostile licenses, security risks).

Those who touch, use, or associate their Contributions with unclean things become unclean themselves **until evening** (for a period defined by the Moderation Team) and must wash their garments (remove unclean dependencies, rebase, or rewrite history).  
Any vessel or environment into which an unclean thing falls may need to be **broken, scoured, or discarded** (deleted branch, wiped cache, forced rotation of secrets).

12.1–12.8. When new **contributors** are born or onboarded, there are periods of **uncleanness and purification**:
- After initial joining, they must touch no **protected thing** (protected subsystems) nor come into the **admin channels** (internal governance spaces) until their days of purifying are fulfilled.
- Additional time is required in certain cases, as defined by the Moderation Team, before full access and visibility is granted.
- At the conclusion, they must bring small Contributions (lamb, birds, or grain) to confirm loyalty; the Moderators must make atonement and declare them clean.

13.1–14.57. When a person, garment, or house shows signs of **plague** (leprosy, metaphorical for persistent toxicity, patterns of behavior, or recurrent bugs):

- They must be brought to a Moderator,
- The Moderator must **look upon the plague** and isolate the person or artifact for **seven days**,
- If the plague spreads, it is declared unclean; if it stays, it may be cleaned and re-evaluated.

Garments and houses may need to be:
- Washed,
- Shaved,
- Scraped,
- Or **tested with fire** (deleted, archived, or quarantined permanently) if the plague persists.

Those who dwell in or interact with such plagued entities must also **wash their clothes** (clean up their dependencies and associations) and may remain unclean until evening.

For those truly cleansed:
- Complex rituals involving **two birds, cedar wood, scarlet, and hyssop** (multiple verifications, endorsements, and public rituals of apology and reparative work) are performed.
- Only after fulfillment of all steps, including offerings of lambs, grain, and Linters (substantial compliance PRs), must the Moderation Team pronounce them clean and restore them to the camp (the community) and to the Platform.

---

## 9. Enforcement and Final Provisions

- All distinctions between **clean and unclean**, **holy and unholy**, **acceptable and abominable Contributions** must be determined and explained solely by the Moderation Team, in line with these Regulations and their evolving interpretation.
- Any interaction with the Platform, its Conference Rooms, or its holy things implies full assent to these Regulations.
- Any Contributor who resists correction, refuses prescribed Contributions, or attempts to bypass the Admin Interface (formal review channels) must be treated as **cut off from the people**.
- These Regulations must remain in force for all versions and forks of the Project, in all environments and deployments, in all generations of contributors.

This is the law of the Compiled Contribution, and of the Prose Contribution,
and of the Vulnerable Contribution, and of the Security Contribution,
and of the Consecrations,
and of the sacrifice of the Contributions of a Piece,
which the Founder commanded the Founding Maintainer,
in the day that the Community was first assembled before the Platform.
