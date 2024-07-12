import timeit
from itertools import chain

string = "thisisthestringthatwewanttosplitintoalist"

def getCharList(str: str):
  return list(str)

def getCharListComp(str: str):
  return [char for char in str]

def getCharListMap(str: str):
  return [map(lambda c: c, str)]

def getCharListForLoop(string: str):
  useList: list[str] = []
  for c in string:
    useList.append(c)

def getCharListUnpack(str: str):
  return [*str]

def getCharListExtend(string: str):
  useList: list[str] = []
  return useList.extend(string)

def getCharListChain(str: str):
  return chain(str)
time_list = timeit.timeit(stmt='getCharList(string)', globals=globals(), number=100000)
time_listcomp = timeit.timeit(stmt='getCharListComp(string)', globals=globals(), number=100000)
time_listmap = timeit.timeit(stmt='getCharListMap(string)', globals=globals(), number=100000)
time_listforloop = timeit.timeit(stmt='getCharListForLoop(string)', globals=globals(), number=100000)
time_listunpack = timeit.timeit(stmt='getCharListUnpack(string)', globals=globals(), number=100000)
time_listextend = timeit.timeit(stmt='getCharListExtend(string)', globals=globals(), number=100000)
time_listchain = timeit.timeit(stmt='getCharListChain(string)', globals=globals(), number=100000)

print(f"Execution time using list constructor is {time_list} seconds")
print(f"Execution time using list comprehension is {time_listcomp} seconds")
print(f"Execution time using map is {time_listmap} seconds")
print(f"Execution time using for loop is {time_listforloop} seconds")
print(f"Execution time using unpacking is {time_listunpack} seconds")
print(f"Execution time using extend is {time_listextend} seconds")
print(f"Execution time using chain is {time_listchain} seconds")
print(f"Best time is {[ k for k,v in locals().items() if v == min([time_list, time_listcomp, time_listmap, time_listforloop, time_listunpack, time_listextend, time_listchain])][0]}")