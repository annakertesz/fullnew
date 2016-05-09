def divcheck(num):
    numOfDivs = 0
    for divs in range(1, num + 1):
        if num % divs == 0:
            numOfDivs += 1
    if numOfDivs % 2 != 0:
        numOfDivs = True
    else:
        numOfDivs = False
    return numOfDivs
opndrs = []
for door in range(1, 101):
    numOfDivs = divcheck(door)
    if numOfDivs is True:
      opndrs.append(door)
print("The following doors are open:")
print(opndrs)
