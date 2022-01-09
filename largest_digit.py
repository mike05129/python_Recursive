"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
maxium_num  = 0
ans = 0

def main():
    print(find_largest_digit(12345))      # 5
    print(find_largest_digit(281))        # 8
    print(find_largest_digit(6))          # 6
    print(find_largest_digit(-111))       # 1
    print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
    """
    :param n:
    :return:
    """
    global maxium_num ,ans
    dig = int(abs(n) % 10)
    dig2 = int((abs(n)//10) % 10)
    if dig >= dig2:
        dig2 = dig
    if dig2 > maxium_num:
        maxium_num = dig2
        ans = maxium_num
    if abs(n) > 99:
        find_largest_digit(abs(n)//10)
    maxium_num=0
    return int(ans)
 


if __name__ == '__main__':
    main()
