from collections import deque

def get_is_palindrom(text):
  normText = text.replace(' ', '')
  normText = normText.lower()
  d = deque(normText)
  while len(d) > 1:
    if d.pop() != d.popleft():
      return False
  return True