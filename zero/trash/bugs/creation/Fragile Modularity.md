A property of systems arising from an attempt to implement "separation of concerns" without first ensuring the components responsible for handling those separate concerns are useful and some more general purpose than the specific function they serve in that particular machine when it is operating perfectly.

Leads to system that immediately breaks whenever any small component fails.

Tends to occur in systems built by large teams, particularly in organizations that place a heavy emphasis on "planning," because [[proc/trash/principles/Planning is Pretending]], and it's easier to pretend how to build both a system and its parts before either exist than it is to carry this out.

Lesson: Build large systems from working re-usable parts. If you don't have those parts yet, build them first. When you are building those parts, forget the larger system entirely. Never mention the larger system's name in your source code for the pieces. The pieces must each solve some more general problem, and solve it better than you think you will need to when the whole is operating perfectly. Because pieces will break, assumptions will be violated, and it's not up to the whole to handle those problems.