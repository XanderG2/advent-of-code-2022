with open("C:/users/xande/desktop/advent of code/day5input.txt", "r") as file:
  temp = file.read()

stacks = {}

from math import ceil
from re import search

partOne = False
lines = temp.splitlines()
stacksfinished = False

for line in lines:
  if line == "":
    pass
  elif not stacksfinished:
    if line[0] == " " and line[1] == "1":
      print(stacks)
      stacksfinished = True    
    else:
      chars = list(line)
      l = len(chars)
      entries = ceil(l/4)
      for entry in range(entries):
        pos = entry * 4
        key = entry + 1
        if key not in stacks:
          stacks[key] = []
        if chars[pos] == "[":
          stacks[key].insert(0, chars[pos+1])

  else:
    matches = search(r"^move (\d+) from (\d+) to (\d+)$", line)
    if matches:
      count = int(matches.group(1))
      from_ = int(matches.group(2))
      to = int(matches.group(3))
      print(f"count: {count}, from: {from_}, to: {to}")
      source = stacks[from_]
      target = stacks[to]
      slice = source[len(source)-count:]
      source = source[0:len(source)-count]
      if partOne:
        target += slice[::-1]
      else:
        target += slice
      stacks[from_] = source
      stacks[to] = target
      print(stacks)

for n, s in stacks.items():
  print(s[-1], end="")
print()

