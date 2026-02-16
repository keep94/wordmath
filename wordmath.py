import itertools


def Solve(f, *words, allow_leading_zeros=False):
  result = _Solve(f, 1, words, False, allow_leading_zeros)
  if result:
    return result[0]
  return None


def SolveAll(f, *words, allow_leading_zeros=False):
  return _Solve(f, 0, words, False, allow_leading_zeros)


def SolveC(f, *words, allow_leading_zeros=False):
  result = _Solve(f, 1, words, True, allow_leading_zeros)
  if result:
    return result[0]
  return None


def SolveAllC(f, *words, allow_leading_zeros=False):
  return _Solve(f, 0, words, True, allow_leading_zeros)


def _Eval(context, word, hasLeadingZeros):
  result = 0
  for x in word:
    result = 10*result + context[x]
    if not result:
      hasLeadingZeros[0] = True
  return result


def _Solve(f, max, words, addConverter, allowLeadingZeros):
  letters = []
  for word in words:
    letters.extend(word)
  orderedletters = sorted(set(letters))
  if len(orderedletters) > 10:
    raise Exception("More than 10 letters")
  perms = itertools.permutations(range(10), len(orderedletters))
  result = []
  hasLeadingZeros = [False]
  for perm in perms:
    hasLeadingZeros[0] = False
    lettersToDigits = dict(zip(orderedletters, perm))
    context = tuple(_Eval(lettersToDigits, w, hasLeadingZeros) for w in words)
    if (not allowLeadingZeros) and hasLeadingZeros[0]:
      continue
    if addConverter:
      passes = f(lambda x: _Eval(lettersToDigits, x, hasLeadingZeros))
      if (not allowLeadingZeros) and hasLeadingZeros[0]:
        continue
    else:
      passes = f(*context)
    if passes:
      result.append(context)
      if len(result) == max:
        return result
  return result
