import math
#did it work?????

# computes the binomial coefficient
# i.e. x choose y
def binomial(x, y):
    a = math.factorial(x)
    b = math.factorial(y)
    c = math.factorial(x - y)
    answer = a // (b * c)
    return answer


# computes the matching polynomial (evaluated at 1) of a bipartite graph on x and y parts
def matchingPoly(x, y):
    answer = 0
    for i in xrange(0, x + 1):
        a = (-1) ^ (i + 1)
        b = binomial(x, i)
        c = binomial(y, i)
        d = math.factorial(i)
        partialSum = a * b * c * d
        answer = answer + partialSum
    return answer


if __name__ == '__main__':
    m = int(input("Give an m: "))
    n = int(raw_input("Give an n: "))
    print matchingPoly(m, n)
