a = 1500000000
b = 200000000
c = a%b #老三
print(a, b, c)
while c!=0: #輾轉相除法
  a = b #老二升格老大
  b = c #老三升格變老二
  c = a%b #新的老三算出來
  print(a, b, c)