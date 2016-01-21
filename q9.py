lines = [line.rstrip('\n') for line in open('rosalind_subs.txt')]
str = ""
str = lines[0]
print str
find = ""
find = lines[1]
print find
pos = []


for i in range (0, len(str)):
    if str[i:i + len(find)] == find:
        pos.extend([i+1])

        
print pos
   
    