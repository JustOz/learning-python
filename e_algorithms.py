from math import factorial as fact
from math import e




def main() -> int:
    j = euler_e_sequence(100)
    print(e)


    return 0


def euler_classic_limit(n: int) -> float:
    """
    Args:
        n: int
    
    Returns:
        e: float
    """
    return (1 + 1/n) ** n


def euler_e_sequence(n: int) -> float:
    """
    Args:
        n: int
    
    Returns:
        e: float
    """
    e = 0
    for i in range(n):
        e += 1 / fact(i)

    return e


if __name__ == "__main__":
    main()
