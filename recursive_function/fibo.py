def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n - 1)  + fibo(n - 2)


if __name__ == "__main__":
    print(fibo(int(input())))