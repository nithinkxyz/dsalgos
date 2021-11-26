def factorial(n, output=1):
    if n <= 1:
        return output
    else:
        return factorial(n-1, output * n)


def fibonacci(n, prev=1, last=1):
    if n <= 2:
        return prev
    else:
        return fibonacci(n-1, prev + last, prev)


def int_to_binary(n, output=""):
    if int(n/2) == 0:
        print(n)
        return f"1{output}"
    else:
        print(n, output)
        return int_to_binary(int(n/2), f"{n%2}{output}")


def sum_digits(n, output=0):
    if n < 10:
        return output + n
    else:
        return sum_digits(int(n/10), output + n % 10)


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def power(n, exp, output=1):
    if exp <= 0:
        return output
    else:
        return power(n, exp-1, output*n)

