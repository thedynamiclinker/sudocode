## λ1 -  Simply Typed λ-calculus

### Or: Church's Second Draft

0: We add types and a typing judgment `Γ ⊢ t : A`.  

Core rules (function fragment):

- Var: if `x:A ∈ Γ` then `Γ ⊢ x : A`.
- Abs: if `Γ, x:A ⊢ t : B` then `Γ ⊢ λx:A. t : A → B`.
- App: if `Γ ⊢ t : A → B` and `Γ ⊢ u : A` then `Γ ⊢ t u : B`.

1: Do one full derivation. No hand-waving.

0: Derive `⊢ λx:Bool. x : Bool → Bool`.

1. Assume `x:Bool` in the context. By Var:  
    `x:Bool ⊢ x : Bool`.
    
2. By Abs: discharge `x:Bool`:  
    `⊢ (λx:Bool. x) : Bool → Bool`.

1: Apply it to `true`. Show the type of the application.

0: Assume we have constants `true:false : Bool` (base type).  
We already have `⊢ λx:Bool. x : Bool → Bool` and `⊢ true : Bool`.  
By App:  
`⊢ (λx:Bool. x) true : Bool`.

1: Show a program that doesn't type-check.

0:  The classic `Ω := (λx. x x) (λx. x x)` is untypable in Simply Typed λ-Calculus.

To type `x x`, `x` must have a function type `A → B` and also type `A` itself.  

So `x : A` and `x : A → B` simultaneously; impossible in simple types.

1: So the Simple Types version prevents certain non-terminating terms?

0: Right. In pure Simply Typed λ-Calculus (no fixed point combinator), every well-typed closed term normalizes.

1: Booleans again- typed this time- with `if`.

0: Let's treat `Bool` as primitive with `if : Bool → A → A → A`.  

Type-check `(if true then (λx:Bool. x) true else false)`:

1. `⊢ true : Bool`.
2. `⊢ (λx:Bool. x) true : Bool` from before.
3. `⊢ false : Bool`.
4. By `if`'s type: instantiate `A := Bool`, we get  
    `⊢ if true ( (λx:Bool. x) true ) false : Bool`.

1: And evaluation?

0: Let's try it.

```
if true T F → T
= (λx:Bool. x) true
→ true
```

---

## λ2 -  System F

### Or: Second-Order Polymorphic λ

0:  Now terms can abstract over _types._

1: Speak English.

0: Ok so:

New syntax:
- Type abstraction: `Λα. t`
- Type application: `t [τ]`

Typing (informally):

- If `t` is well-typed under assumption `α : *`, then `Λα. t : ∀α. T`.
- If `t : ∀α. T`, then `t [τ] : T[α := τ]`.

1: Don't hand-wave. Write the polymorphic identity and check it.

0: Polymorphic identity:

```
id := ΛA. λx:A. x
```

Typing:

1. Assume kind `A : *`. In context `A:* , x:A ⊢ x : A` by Var.
    
2. By Abs: `A:* ⊢ (λx:A. x) : A → A`.
    
3. By Type-Abs: `⊢ (ΛA. λx:A. x) : ∀A. A → A`.
    

1: Use it on `Bool` and `true`, step-by-step.

0: Evaluation:

```
id [Bool] true
= (ΛA. λx:A. x) [Bool] true
→ (λx:Bool. x) true     -- type application instantiates A := Bool
→ true                  -- β
```

1: Give me polymorphic booleans with no cheating.

0: Encode `Bool` as:

```
Bool  := ∀R. R → R → R
true  := ΛR. λt:R. λf:R. t
false := ΛR. λt:R. λf:R. f
if    := ΛR. λc:Bool. λa:R. λb:R. [R] c a b
```

Check `ifF trueF [X] T F → T`:

```
ifF trueF [X] T F
= (λb. ΛR. λt. λf. b [R] t f) trueF [X] T F
→ (ΛR. λt. λf. trueF [R] t f) [X] T F
→ (λt. λf. trueF [X] t f) T F
→ (λf. trueF [X] T f) F
→ trueF [X] T F
→ (ΛR. λt. λf. t) [X] T F
→ (λt. λf. t) T F
→ (λf. T) F
→ T
```

1: 
I see. System F lets me write "for all types" directly.

0:  
Exactly: parametric polymorphism. You quantify over types themselves.

---

## Chapter 3 -  System Fω

### Or: Higher-Kinded Polymorphism

0:  System F quantifies over types (`A : *`).  
Fω lets us quantify over type constructors, e.g. `F : * → *`.  
We need kinds:

- `*` is the kind of data types (Bool, Nat, List A ...)
- `κ1 → κ2` is the kind of functions on kinds (constructors)

1: I don't know what that means. Give me an example.

0: Ok, here's a higher-kinded polymorphic function:

```
liftId := ΛF:*→*. ΛA:*. λx: F A. x
```

Typing sketch:

1. In kind context `F:*→*, A:*`, we assume `x : F A`.
2. Then `λx: F A. x : F A → F A`.
3. Abstract over `A`: `ΛA:*. λx: F A. x : ∀A:*. F A → F A`.
4. Abstract over `F`: `ΛF:*→*. ΛA:*. λx: F A. x : ∀F:*→*. ∀A:*. F A → F A`.

1: Give me a concrete constructor to apply it to. And reduce.

0: Use the Church encoding of `Maybe`:

```
-- For each A:*, Maybe A : *
Maybe := λA:*. ∀R:*. (A → R) → R → R
just   := ΛA. λa:A. ΛR. λj:(A→R). λn:R. j a
none   := ΛA. ΛR. λj:(A→R). λn:R. n
```

Now apply `liftId`:

```
liftId [Maybe] [Bool] (just [Bool] true)
→ (ΛA. λx: Maybe A. x) [Bool] (just [Bool] true)
→ (λx: Maybe Bool. x) (just [Bool] true)
→ just [Bool] true
```

Every step is a standard β at the term level or type instantiation at the type level.

1: So Fω is "System F + abstraction over constructors" with kinds keeping it sane.

0: Yes. You can write types that are parameterized by type constructors and prove/express laws at that level.

---

## Chapter 4 -  Dependent Types

### Or: λC
### Or: CoC
### Or: Dammit, French people

0: Now we let terms appear in types. The core connective is the Π-type ("dependent function"):

- `(x : A) → B x` means a function that, given `x:A`, returns a term in the type `B x` which may depend on x.

We'll also use Σ-types (dependent pairs):

- `Σ (x:A). B x` packages an `x:A` with a `y:B x`.

To avoid paradoxes, we stratify universes: `Type₀ : Type₁ : Type₂ : ...` (Lean/Coq/Agda do this automatically).

1: Give me a dependent type I can't fake with Fω. Step it carefully.

0: Length-indexed vectors:

```
Nat : Type
zero : Nat
succ : Nat → Nat

Vec : Nat → Type → Type      -- depends on first argument (a Nat)
nil  : ∀A:Type. Vec zero A
cons : ∀A:Type. ∀n:Nat. A → Vec n A → Vec (succ n) A
```

Notice the type of `cons` says the result length is `succ n`.

1: 
Show me a concrete term and its type formation, no gaps.

0:  
Let `A := Bool`. Build a 2-element vector:

```
v2 := cons Bool 1 true (cons Bool 0 false (nil Bool))
```

We must read `1` as `succ zero` and `0` as `zero`. Type-check in stages:

1. `nil Bool : Vec zero Bool`.
2. `cons Bool 0 false (nil Bool) : Vec (succ 0) Bool = Vec 1 Bool`.
3. `cons Bool 1 true (cons Bool 0 false (nil Bool)) : Vec (succ 1) Bool = Vec 2 Bool`.

Hence:

```
⊢ v2 : Vec 2 Bool
```

1: Now a function whose result type depends on the input value.

0: `head` for non-empty vectors:

```
head : ∀A:Type. ∀n:Nat. Vec (succ n) A → A
head A n (cons A n a _) = a
```

Type-check: the input is `Vec (succ n) A`, pattern-matching on `cons` reveals the element `a : A` directly. The right-hand side is `a : A`, matching the declared result type `A`.

1: Append vectors and show the length adds. Explicitly.

0: Define vector append (indices add in the type):

```
append : ∀A:Type. ∀m n:Nat. Vec m A → Vec n A → Vec (m + n) A
append A m n (nil A)         ys = ys
append A m n (cons A k x xs) ys = cons A (k + n) x (append A k n xs ys)
```

Here `m` is either `0` or `succ k`. In the second case we must have `m = succ k`, and the result index is `(succ k) + n = succ (k + n)`, reflected by `cons A (k + n)`.  
The types themselves track algebra of lengths.

1: Do one concrete reduction. Don't skip the index arithmetic.

0: Take `A := Bool`. Append `[true, false] : Vec 2 Bool` to `[true] : Vec 1 Bool`.

Write them:

```
v2 := cons Bool 1 true (cons Bool 0 false (nil Bool))      -- length 2
v1 := cons Bool 0 true (nil Bool)                          -- length 1
```

Compute `append Bool 2 1 v2 v1`:

Case analysis on the first vector:

1. `v2 = cons Bool 1 true (cons Bool 0 false (nil Bool))`, so we are in the second clause:

```
append Bool 2 1 v2 v1
= cons Bool (1 + 1) true (append Bool 1 1 (cons Bool 0 false (nil Bool)) v1)
```

2. Now compute the recursive call. Again second clause (head is a `cons`):

```
append Bool 1 1 (cons Bool 0 false (nil Bool)) v1
= cons Bool (0 + 1) false (append Bool 0 1 (nil Bool) v1)
```

3. Now first clause (nil on the left):

```
append Bool 0 1 (nil Bool) v1
= v1
= cons Bool 0 true (nil Bool)
```

4. Substitute back:
    

```
append Bool 1 1 (...) v1
= cons Bool 1 false (cons Bool 0 true (nil Bool))
```

5. Substitute again:
    

```
append Bool 2 1 v2 v1
= cons Bool 2 true (cons Bool 1 false (cons Bool 0 true (nil Bool)))
```

Type of the result is `Vec (2 + 1) Bool = Vec 3 Bool`. The index arithmetic matches the constructors we used: `2+1 = 3`, and we literally built a 3-cell vector.

1: 
Propositions-as-types? Equality? Don't skip the rule.

0:  
We add an identity type (propositional equality):

```
Eq : ∀(A:Type). A → A → Type
refl : ∀(A:Type). ∀(x:A). Eq A x x
```

Informally, to prove `Eq A u v`, we usually do induction/pattern-matching on equality (or use `refl` when both sides are definitionally equal).

As a small dependent proof: right identity of `append` on vectors

```
append_nil_right : ∀A m (xs : Vec m A). Eq (Vec m A) (append A m 0 xs (nil A)) xs
```

Proof sketch (by induction on `xs`):

- Base: `xs = nil A`. Then `(append A 0 0 (nil A) (nil A)) = nil A` by first clause. So `refl`.

- Step: `xs = cons A k x xs'`. Then:
    ```
    append A (succ k) 0 (cons A k x xs') (nil A)
    = cons A (k + 0) x (append A k 0 xs' (nil A))
    ```
    By IH, `append A k 0 xs' (nil A) = xs'`. Also `k + 0 = k`. So result is `cons A k x xs' = xs`. Conclude by `refl` after definitional equalities.
    

This is the flavor of CIC (Calculus of Inductive Constructions): dependent functions + inductive families + equality, i.e., Coq/Agda/Lean style stuff.

---

## Bird's-eye recap of the climb

- Simply typed: Functions on terms; types talk about shapes of terms (`A → B`).
- System F: Quantify over types (`∀A. ...`).
- System Fω: Quantify over type constructors (`∀F:*→*. ...`) with kinds.
- Dependent Types (CoC/CIC): Types may mention terms (`Π (x:A), B x`), plus inductives and equalities → proof by programs.

---

## Exercises with solutions

Example 0 (untyped): Reduce `if false T F` with encodings.  
Solution:

```
if false T F
= (λb. λt. λf. b t f) false T F
→ (λt. λf. false t f) T F
→ (λf. false T f) F
→ false T F
→ (λt. λf. f) T F
→ (λf. f) F
→ F
```

Example 1 (Simply Typed): Derive the type of `λf:(Bool→Bool). f true`.  
Solution:

1. Assume `f:Bool→Bool`. By Var: `f : Bool→Bool`.
    
2. Also `true : Bool`. By App: `f true : Bool`.
    
3. By Abs: `⊢ λf:(Bool→Bool). f true : (Bool→Bool) → Bool`.
    

Example 2 (System F): Type and reduce `(ΛA. λp: A→A. p) [Nat] (λn:Nat. n)`  
Solution (typing):

- Inside `ΛA`, we have `λp:A→A. p : (A→A) → (A→A)`.
    
- So whole term: `∀A. (A→A) → (A→A)`.  
    Reduction:
    

```
(ΛA. λp:A→A. p) [Nat] (λn:Nat. n)
→ (λp:Nat→Nat. p) (λn:Nat. n)
→ (λn:Nat. n)
```

Example 3 (Fω): Specialize `liftId` to Lists.  
Let `List : *→*` be a Church encoding:  
`List A := ∀R. (A→R→R) → R → R`.  
Compute `liftId [List] [Bool] xs`.  
Solution:  
By definition,

```
liftId [List] [Bool] xs
= (ΛA. λx: List A. x) [Bool] xs
→ (λx: List Bool. x) xs
→ xs
```

Example 4 (Dependent): Type `head Bool 1 (cons Bool 0 true (nil Bool))`.  
Solution:

- `cons Bool 0 true (nil Bool) : Vec (succ 0) Bool = Vec 1 Bool`.
- `head : ∀A. ∀n. Vec (succ n) A → A`. Instantiating `A:=Bool, n:=0` gives  
    `head Bool 0 : Vec 1 Bool → Bool`.
- Apply: `head Bool 0 (cons Bool 0 true (nil Bool)) = true : Bool`.
