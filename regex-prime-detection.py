import re

def is_prime(n: int) -> bool:
    return not re.match(r'^.?$|^(..+?)\1+$', '1'*n)

if __name__ == '__main__':
    for i in [1, 4, 13, 16, 17, 21, 37, 49, 17*17, 7919]:
        print(f'{i} is{is_prime(i) and " " or " not "}a prime number.')
