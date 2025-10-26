def add(a: int, b: int) -> int:
    """Складывает два числа."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Умножает два числа."""
    return a * b

def is_even(n: int) -> bool:
    """Проверяет, чётное ли число."""
    return n % 2 == 0

def get_divisors(x: int) -> list[int]:
    """Возвращает отсортированный список нетривиальных делителей числа x."""
    divisors = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            divisors.add(i)
            divisors.add(x // i)
    return sorted(divisors)