def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    m=0
    x=0
    if a>0:
        m+=1
    if a<0:
        x+=1
    if b>0:
        m+=1
    if b<0:
        x+=1
    if c>0:
        m+=1
    if c<0:
        x+=1
    if x>m:
        print("There are a lot of negative numbers")
    else:
        print("There are a lot of positive numbers")
    return m,x
    
x=main(5,-10,-5)
print(x)