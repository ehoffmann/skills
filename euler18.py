#!/usr/bin/python

sequence = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10,20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34,88, 2, 77, 73, 07, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33,41, 48, 72, 33, 47, 32, 37, 16, 94, 29,53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23, ]

def get_cost(i):
    """Return the max of 2 paths"""
    if i >= len(sequence):
        return 0
    else:
        return max (get_cost(i + get_line(i)),get_cost(i + get_line(i) + 1)) + sequence[i] 

def get_line(i):
    counter = 1
    line = 1
    while (True):
        if (counter > i):
            return line
        else:
            line += 1
            counter += line

import sys
	
if __name__ == '__main__':
    #i = int(sys.argv[1])
    assert get_line(0) == 1
    assert get_line(1) == 2
    assert get_line(2) == 2
    assert get_line(3) == 3
    assert get_line(10) == 5
    assert get_line(15) == 6
    assert get_line(20) == 6
    assert get_line(21) == 7
   
    # test de get_cost
    #assert get_cost(119) == 23, get_cost(119)
    #assert get_cost(104) == 58 , get_cost(104)
    #assert get_cost(90) == 210 , get_cost(90)
    #assert get_cost(60) == 2051, "%s,  %s " % (get_cost(60), sequence[60]) 

    # find the best path and explain choice
    i = 0
    result = sequence[0]
    while (i < len(sequence)):
        print "current %s:%s" % (i, sequence[i])
	a = get_line(i) + i
	b = a + 1
	cost_a = get_cost(a)
	cost_b = get_cost(b)
        print "choices are %s(%s) | %s(%s)" % (
            sequence[a],cost_a, sequence[b],cost_b
        )
	choice = (b, sequence[b], cost_b)
	if (cost_a > cost_b):
            choice = (a, sequence[a], cost_a)

        print "my choice is idx:%s val:%s cost:%s" % choice
	i=choice[0]
        result += choice[1]
	print "tmp result: ", result

print "result is ", result 
    
