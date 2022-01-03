def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s=''
    m=0+a
    a1=pow(0,a)
    a//=10
    a2=pow(0,a)
    a//=10
    a3=pow(0,a)
    a//=10
    x=3-(a1+a2+a3)
    print(x)
    if x==2 and m%2==0:
        s="two-digit even number"
    if x==2 and m%2==1:
        s="two-digit odd number"
    if x==3 and m%2==0:
        s="three-digit even number"
    if x==3 and m%2==1:
        s="three-digit odd number"
        return s
print(main(15))