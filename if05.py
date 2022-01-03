def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    m=0
    if a<0:
        m+=1
    if b<0:
        m+=1
    if c<0:
        m+=1
    return m
x=main(-5,-10,10)
print(x)