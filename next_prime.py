import sys
from timeit import default_timer as timer



def main() -> int:
    try:
        n = int(sys.argv[1])
    except:
        print("Please enter a n: int > 2 as an argument\nGenerates primes < n.")
        return 1

    primes = gen_prime(n)
    running = True
    stuckLoop = False
    i = 0

    while running:
        if i >= len(primes):
            print("ERROR::Index out of scope")
            break
        if not stuckLoop:
            print("Prime: ", primes[i])
        end_or_what = input("Options:\n\tNext prime - n\n\tSkip couple indexs - i=[number]\n\tEnd - q\n")
        if end_or_what == 'q':
            running = False
            stuckLoop = False
        elif end_or_what == 'n':
            i += 1
            stuckLoop = False
        elif end_or_what:
            if end_or_what[0] == 'i':
                try:
                    i += int(end_or_what[2:])
                    stuckLoop = False
                except:
                    print("Invalid input")
        else:
            print("The option you picked does not exist.")
            stuckLoop = True


    return 0


def gen_prime(x: int) -> bool:
    """
    Args:
        x: int

    Returns:
        primes: list[int]

    Generates a list from 2 to x and returns it.
    """
    sieve = [True] * (x // 2)
    for i in range(3, int(x ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i*i//2::i] = [False] * ((x - i * i -1)//(2 * i) + 1)
    
    return [2] + [2*i + 1 for i in range(1, x // 2) if sieve[i]]



if __name__ == "__main__":
    start = timer()
    main()
    print("The program ran for {} seconds".format(timer() - start))
    print("Exiting")
