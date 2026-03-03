import itertools

_ALL_DIGITS=dict((str(x), x) for x in range(10))

def Solve(
    f,
    *words,
    allow_leading_zeros=False,
    allow_digit_sharing=False,
    digits_for_letters=range(10)):
  result = _Solve(
      f,
      1,
      words,
      False,
      allow_leading_zeros,
      allow_digit_sharing,
      digits_for_letters)
  if result:
    return result[0]
  return None


def SolveAll(
    f,
    *words,
    allow_leading_zeros=False,
    allow_digit_sharing=False,
    digits_for_letters=range(10)):
  return _Solve(
      f,
      0,
      words,
      False,
      allow_leading_zeros,
      allow_digit_sharing,
      digits_for_letters)


def SolveC(
    f,
    *words,
    allow_leading_zeros=False,
    allow_digit_sharing=False,
    digits_for_letters=range(10)):
  result = _Solve(
      f,
      1,
      words,
      True,
      allow_leading_zeros,
      allow_digit_sharing,
      digits_for_letters)
  if result:
    return result[0]
  return None


def SolveAllC(
    f,
    *words,
    allow_leading_zeros=False,
    allow_digit_sharing=False,
    digits_for_letters=range(10)):
  return _Solve(
      f,
      0,
      words,
      True,
      allow_leading_zeros,
      allow_digit_sharing,
      digits_for_letters)


def _Eval(context, word, hasLeadingZeros):
  result = 0
  for x in word:
    result = 10*result + context[x]
    if not result:
      hasLeadingZeros[0] = True
  return result


def _Solve(
    f,
    max,
    words,
    addConverter,
    allowLeadingZeros,
    allowDigitSharing,
    digitsForLetters):
  letters = []
  for word in words:
    letters.extend(word)
  result = []
  hasLeadingZeros = [False]
  for lettersToDigits in _LetterToDigitCombos(
      letters, digitsForLetters, allowDigitSharing):
    hasLeadingZeros[0] = False
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


def _LetterToDigitCombos(letters, digitsForLetters, allowDigitSharing):
  digitsForLetters = set(digitsForLetters)
  if digitsForLetters.difference(range(10)):
    raise ValueError("digits_for_letters must contain values between 0-9")
  orderedLetters = sorted(set(letters).difference(_ALL_DIGITS))
  if allowDigitSharing:
    perms = itertools.product(digitsForLetters, repeat=len(orderedLetters))
  else:
    perms = itertools.permutations(digitsForLetters, len(orderedLetters))
  for perm in perms:
    lettersToDigits = dict(zip(orderedLetters, perm))
    lettersToDigits.update(_ALL_DIGITS)
    yield lettersToDigits
