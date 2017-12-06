numbers = []
def foo(limit, increment):
    i = 0
    while i < limit: 
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        if i == 6:
            continue
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


foo(6, 1)
foo(7,2)
print "THe numbers: "
for num in numbers:
    print num



