import sys
from collections import defaultdict


def main():
  size = int(input())
  arr = [int(a) for a in input().split()]
  unic = defaultdict(int)
  count = 0
  for a in arr:
    unic[a] += 1
  for a in unic.values():
    if a == 1:
      count+=1
  print(count)


if __name__ == '__main__':
	main()
