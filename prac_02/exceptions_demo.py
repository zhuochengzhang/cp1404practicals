"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Numerator and denominator must be valid numbers!")
        exit(0)
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# ValueError
# 当输入的不是整数 会出现Value Error 因为在执行int命令的时候出错了
# ZeroDivisionError
# 当被除数是0的时候 会出现ZeroDivisionError
# 修改增加了一层判断 如果被除数是0 则直接判断出错
