#SOIT108_ADVANCE_001
a = int(input())

ans=0
for i in range(1,100):
	if a ==i*i:
		ans = 1
		
print(ans,end='')