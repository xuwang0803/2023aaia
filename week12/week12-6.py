def ged(a, b):
  print(a, b)
  if a==0: return b
  if b==0: return a
  return ged(b, a%b)
print( ged(a, b) )