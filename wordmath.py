import itertools


def Solve(f, *words):
  result = _Solve(f, 1, words, False)
  if result:
    return result[0]
  return None


def SolveAll(f, *words):
  return _Solve(f, 0, words, False)


def SolveC(f, *words):
  result = _Solve(f, 1, words, True)
  if result:
    return result[0]
  return None


def SolveAllC(f, *words):
  return _Solve(f, 0, words, True)


def _Eval(context, word):
  result = 0
  for x in word:
    result = 10*result + context[x]
  return result


def _Solve(f, max, words, addConverter):
  letters = []
  for word in words:
    letters.extend(word)
  orderedletters = sorted(set(letters))
  if len(orderedletters) > 10:
    raise Exception("More than 10 letters")
  perms = itertools.permutations(range(10), len(orderedletters))
  result = []
  for perm in perms:
    lettersToDigits = dict(zip(orderedletters, perm))
    context = tuple(_Eval(lettersToDigits, w) for w in words)
    if addConverter:
      passes = f(lambda x: _Eval(lettersToDigits, x))
    else:
      passes = f(*context)
    if passes:
      result.append(context)
      if len(result) == max:
        return result
  return result


