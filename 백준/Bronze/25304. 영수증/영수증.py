x = int(input())
n = int(input())
total = 0
for i in range(n):
  price, cnt = map(int, input().split())
  total += (price*cnt)

if x == total:
  print("Yes")
else:
  print("No")