def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0 and a%2==0:
        x="positive even number"
    if a>0 and a%2!=0:
        x="positive odd number"
    if a<0 and a%2==0:
        x="negative even number"
    if a<0 and a%2!=0:
        x="negative odd number"
    if a==0:
        x= "the number is zero"
    return x
print(main(5))