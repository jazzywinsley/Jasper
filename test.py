import string, random, os, time

alphabets = list(string.ascii_letters)
target, current = "documatic", ""
for c in target:
  letters = alphabet.copy()
  l = ""
  while l != c:
    l = random.choice(letters)
    letters.remove(l)
    print(current + l)
    time.sleep(0.02)
  current += l
