#!/usr/bin/python
f = open("data67.txt", 'r')
s = f.read()
f.close()
s = s.replace("\n",' ')
sequence = [int(i) for i in s.split(' ') if i != '']


#sequence = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10,20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34,88, 2, 77, 73, 07, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33,41, 48, 72, 33, 47, 32, 37, 16, 94, 29,53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23, ]

# cache system
costs = {}

def get_cost(i):
    """Return the max of 2 paths"""
    if (i >= len(sequence)):
        return 0
    else:
        next = get_line(i) + i
        if not costs.has_key(i):
            costs[i] = get_cost(next)
        if not costs.has_key(i+1):
            costs[i+1] = get_cost(next + 1)
        return max (costs[i], costs[i+1] ) + sequence[i]

def get_line(i):
    counter = 1
    line = 1
    while (True):
        if (counter > i):
            return line
        else:
            line += 1
            counter += line


if __name__ == '__main__':
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

   
