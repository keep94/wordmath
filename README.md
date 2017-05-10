# wordmath

Python package to solve wordmath puzzles

# Introduction

This python package solves wordmath puzzles. Provide this package with a
function that evaluates to true when the puzzle is solved and the variables
to solve for and it does the rest.

# The python code

## wordmath.Solve(f, *words)

Solve solves a wordmath puzzle. f is a function that takes any number of
numeric values as input and returns true if those values solve the puzzle
or false otherwise. words is the list of variables passed to f. Solve returns
a tuple of values corresponding to the variables that solve the puzzle or None
if no solution was found.

The following example solves the wordmath puzzle 4 * PUZZLE = WINTER
The solution is PUZZLE = 237716; WINTER = 950864

```
>>> import wordmath
>>> f = lambda PUZZLE, WINTER: 4*PUZZLE == WINTER
>>> wordmath.Solve(f, "PUZZLE", "WINTER")
(237716, 950864)
```

## wordmath.SolveAll(f, *words)

SolveAll works just like Solve except that instead of returning just one
solution, it returns all solutions as a list of tuples. SolveAll
returns an empty list if it could find no solutions.

## wordmath.SolveC(f, *words)

SolveC works like Solve except that f takes one parameter: a context. This
context can evaluate any variable name as long as the letters of the name
all come from the original variables listed in the SolveC call.

SolveC is useful if the wordmath puzzle has many intermediate steps with
many intermediate variables. SolveC will throw a runtime error if f uses
the context to evaluate a variable name with letters not in the original
variables listed in the SolveC call.

The following example solves 3 * PUZZLE + ZZLEWI = WINTER. In this example,
ZZLEWI is an intermediate variable as the principal variables we are solving
for are PUZZLE and WINTER.

The solution is PUZZLE = 152237; WINTER = 680479

```
>>> import wordmath
>>> f = lambda c: 3*c("puzzle") + c("zzlewi") == c("winter")
>>> wordmath.SolveC(f, "puzzle", "winter")
(152237, 680479)
```

## wordmath.SolveAllC(f, *words)

SolveAllC works just like SolveC except that it returns all solutions as
a list of tuples or the empty list if it cannot find any solutions.

