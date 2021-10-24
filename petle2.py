a = 24
b = 36

i = 1
found = False

while not found:
    i=i+1
    if(i%a==0 and i%b==0):
        found = True

print(i)