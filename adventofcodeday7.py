#structure = {"/": {entries: {"a": {"e": {"i": {"size": 584}}}, "b.txt": 14848514}, totalSize:...}}
from pprint import pprint

with open("c:/users/xande/desktop/day7input.txt", "r") as file:
  commands = file.read()

root = {"entries": {}, "parent": None}
sizes = []

def partone():
  global root, commands
  lines = commands.strip().splitlines()
  currentDirectory = None
  for line in lines:
    if line[0] == "$":
      if line[2] + line[3] == "cd":
        target = line[5:]
        if target == "/":
          currentDirectory = root
        elif target == "..":
          currentDirectory = currentDirectory["parent"]
        else:
          if target not in currentDirectory["entries"]:
            raise Exception("target not in currentDirectory[\"entries\"]")
          currentDirectory = currentDirectory["entries"][target]
      else:
        pass
    else:
      a, b = line.split()
      if a == "dir":
        currentDirectory["entries"][b] = {"entries": {}, "parent": currentDirectory}
      else:
        currentDirectory["entries"][b] = {"size": int(a)}
  partonerun()

sum = 0


def walk(dir, dirName):
  global sum, sizes
  size = 0
  for name, entry in dir["entries"]:
    if "entries" in entry:
      #it must be a directory
      walk(entry, name)
      sizes.append([dirName, entry["size"]])
      size += entry["size"]
    else:
      size += entry["size"]
  dir["size"] = size
  if size <= 100_000:
    sum += size


def partonerun():
  global root, sum
  walk(root, 'entries')
  pprint(root)
  print(f"Part one: {sum}")

def parttwo():
  global root, commands, sizes
  max_size = 70000000
  size_free = 30000000
  print(sizes)
  #getNames()

def getNames():
  global root
  

  

partone()
parttwo()