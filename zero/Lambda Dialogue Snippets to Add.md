0 uses the Church encoding. 

0 = λaλb.b
1 = λaλb.a(b)
2 = λaλb.a(a(b))
3 = λaλb.a(a(a(b)))

1 uses the simpler encoding:

0 = λa.a
1 = λa.a(a)
2 = λa.a(a(a))
3 = λa.a(a(a(a)))

Without deciding which of these two to use, they attempt to define `succ n`. They do so by reasoning like the following.

0 starts by saying "I'm gonna start here":

succ = ?

1 says "Is that really a good place to start?"

0 says: Gotta start somewhere.

Then 1 says "Don't we just want to wrap the function around one more time? Like if

3 = λa.a(a(a(a)))

Isn't succ n just

succ n = a(n)

So like

4 = a(3)

Or for your definition, since

3 = λfλx.f(f(f(x)))

Wouldn't we just have

4 = f(3)?

Like wrap one more copy of the function around it?

Then 0 says I dunno, substitute in the definitions of 3. Then 1 goes:

4 = a(λa.a(a(a(a))))

and gets confused, because 1 isn't sure if having the lambda inside like that is allowed, and 1 also realizes the scope is wrong.

Then 0 says "Hey 1, I made progress!" And writes:

succ n = ?

1 doesn't think this is progress.

1 says "Hey 0 I made progress," (sarcastically) and writes 

succ n = m

0 is like "Fantastic!" (Not sarcastically.)

1 thinks 0 is acting strange and asks why that's fantastic.

Then 0 says "Well we haven't agreed on which definition of numbers to use yet, but we each have our own definition, so I can do this:

succ = λn λ? λ?. (stuff)

Because succ takes an number n.

Then I can do this:

succ = λn λf λx. (stuff)

Because succ returns a number too, and my numbers are functions that take two arguments.

Now we just have to implement the stuff!

1 says "Isn't that the entire problem? How is this progress?"

0 says "Or course it's progress! Now we know how to undress the numbers!"

1 says "Undress the what now?"

0 says "You had a good idea about wrapping the function around one more time, but you were wrapping it around the outside. Now that the numbers are naked, no more lambdas wrapped around them, maybe we can add the extra copy of f down here."

1 says like how?

0 says watch:

succ = λn λf λx. f(n)

1 says "Wait I think this has the same problem as mine. That n has lambdas on it."

0 goes "Show me?"

1 goes: Look

3 = λf λx. f(f(f(x))

So

3 g y = g(g(g(y)))

0 asks what g and y are.

1 says I used different letters bc I wasn't sure if I'm allowed to plug f and x into a thing that already has those. 0 says I think it should be ok. Then 0 rewrites this as:

3 f x = f(f(f(n)))

Or in general 

n f x = naked n

So now

succ = λn λf λx. f(naked n)

Or

succ = λn λf λx. f(n f x)

And 1 realizes that in 1's version, we have

succ = λn λa. a(naked n)

Or

succ = λn λa. a(n a)

Then, without yet deciding on how to define the natural numbers, they proceed to define:
- addition
- multiplication
- exponentiation, and finally
- the predecessor function x-1

Interleave Kleene's dialogue about Church when it's relevant.

