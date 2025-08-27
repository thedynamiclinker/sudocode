What's the role of tests?

If you could only have one test, what would it be?

Here's what mine would be. It's the same for every project in every language.

1. Can I do everything in the README from scratch in a clean environment and then run `mycommand --help` without it crashing?

What does this test? -> It tests that you've documented everything that's needed for someone else to use the project.

This partially solves the onboarding problem, since that single test is required to set everything up on a fresh work laptop with nothing installed.

It should be easy to enter a repo and understand how to set it up and run it _even if we imagine deleting the README and all the code comments and docstrings._
