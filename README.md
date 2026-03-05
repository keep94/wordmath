# wordmath

Python package to solve wordmath puzzles

# Introduction

This python package solves wordmath puzzles. Provide this package with a
function that evaluates to true when the puzzle is solved and the variables
to solve for and it does the rest.

# The python code

## wordmath.Solve(f, *words, allow_leading_zeros=False, allow_digit_sharing=False, digits_for_letters=range(10))

Solve solves a wordmath puzzle. f is a function that takes any number of
numeric values as input and returns true if those values solve the puzzle
or false otherwise. words is the list of variables passed to f. Solve returns
a tuple of values corresponding to the variables that solve the puzzle or None
if no solution was found.

Optional Parameters:

- allow_leading_zeros: If True, solutions can contain leading zeros.
Default is False.
- allow_digit_sharing: If True, two different letters can have the same
digit. Default is False.
- digits_for_letters: The digits that letters can be assigned to.
Default is 0 through 9.

The following example solves the wordmath puzzle 4 * PU77LE = WINTER
The solution is PU77LE = 237716; WINTER = 950864

```
>>> import wordmath
>>> f = lambda x, y: 4*x == y
>>> wordmath.Solve(f, "PU77LE", "WINTER")
(237716, 950864)
```

## wordmath.SolveAll(f, *words, allow_leading_zeros=False, allow_digit_sharing=False, digits_for_letters=range(10))

SolveAll works just like Solve except that instead of returning just one
solution, it returns all solutions as a list of tuples. SolveAll
returns an empty list if it could find no solutions.

## wordmath.SolveC(f, *words, allow_leading_zeros=False, allow_digit_sharing=False, digits_for_letters=range(10))

SolveC works like Solve except that f takes one parameter: a context. This
context can evaluate any variable name as long as the letters of the name
all come from the original variables listed in the SolveC call.

SolveC is useful if the wordmath puzzle has many intermediate steps with
many intermediate variables. SolveC will throw a runtime error if f uses
the context to evaluate a variable name with letters not in the original
variables listed in the SolveC call.

Optional Parameters:

- allow_leading_zeros: If True, solutions can contain leading zeros.
Default is False. If False, if f evaluates a variable name that has a
leading zero, then that solution won't count even if f returns true.
- allow_digit_sharing: If True, two different letters can have the same
digit. Default is False.
- digits_for_letters: The digits that letters can be assigned to.
Default is 0 through 9.

The following example solves 3 * PU22LE + 22LEWI = WINTER. In this example,
22LEWI is an intermediate variable as the principal variables we are solving
for are PULE and WINTER.

The solution is PULE = 1537; WINTER = 680479

```
>>> import wordmath
>>> f = lambda c: 3*c("pu22le") + c("22lewi") == c("winter")
>>> digits_for_letters=set(range(10)).difference([2]) # Exclude 2 in solution
>>> wordmath.SolveC(f, "pule", "winter", digits_for_letters=digits_for_letters)
(1537, 680479)
```

## wordmath.SolveAllC(f, *words, allow_leading_zeros=False, allow_digit_sharing=False, digits_for_letters=range(10))

SolveAllC works just like SolveC except that it returns all solutions as
a list of tuples or the empty list if it cannot find any solutions.

