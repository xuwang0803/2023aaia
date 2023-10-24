# week07-6 字串、字典
s = "abcdabcd" # str字串
d = {} # dict字典
for c in s:
  if c in d:
    d[c] = d[c] + 1
  else:
    d[c] = 1
  print('現在獨到的字母', c, "字典變成", d)