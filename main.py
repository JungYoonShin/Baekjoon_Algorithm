import sys
input = sys.stdin.readline

n = int(input())
dots = list(map(int, input().split()))

new_dots = list(sorted(set(dots)))
dots_to_dict = {new_dots[i] : i for i in range(len(new_dots))}

for i in dots:
  print(dots_to_dict[i], end=' ')