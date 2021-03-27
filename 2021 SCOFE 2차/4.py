import re
import sys

def main():
    n = int(input())
    word = list()

    for _ in range(n):
        word.append(sys.stdin.readline())
    
    m = int(input())
    for _ in range(m):
        string = input()
        count = 0
        for j in range(n):
            if re.search(string, word[j]) != None:
                count += 1
        print(count)

if __name__ == "__main__":
    main()