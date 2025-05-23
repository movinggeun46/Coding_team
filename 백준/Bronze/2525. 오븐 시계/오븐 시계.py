
A, B = map(int, input().split())


C = int(input())
total_min = A * 60 + B + C
hour = total_min // 60
min = total_min % 60

if hour >= 24:
   hour -= 24
   

print(hour, min)