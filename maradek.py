
door=2
while door <= 101:
    divisors=0
    trial=1
    while trial != door + 1:
        if door % trial == 1:
            divisors = divisors + 1
        trial = trial + 1
    if divisors%2 == 0:
        print (door-1)
    door = door+1
