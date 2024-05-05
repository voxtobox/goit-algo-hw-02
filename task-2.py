from collections import deque

def get_is_palindrom(text):
  normText = text.replace(' ', '')
  normText = normText.lower()
  d = deque(normText)
  while len(d) > 1:
    if d.pop() != d.popleft():
      print(f"{text} -> {normText} - не є паліндроном" )
      return False
  print(f"{text} -> {normText} - є паліндроном")
  return True

get_is_palindrom('L  f Tfl')
get_is_palindrom('oanmao')
get_is_palindrom('ppWWVV')
get_is_palindrom('   nKL6mmm6 lkn')