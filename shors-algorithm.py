def find_factor_of_prime_power(n: int) -> Optional[int]:
    """Returns non-trivial factor of n if n is a prime power, else None."""
    for k in range(2, math.floor(math.log2(n)) + 1):
        c = math.pow(n, 1 / k)
        c1 = math.floor(c)
        if c1**k == n:
            return c1
        c2 = math.ceil(c)
        if c2**k == n:
            return c2
    return None


def find_factor(
    n: int,
    order_finder: Callable[[int, int], Optional[int]] = quantum_order_finder,
    max_attempts: int = 30
) -> Optional[int]:
    """Kthen faktorë jo-trivial të numrit të plotë n.

    Argumentet:
        n: numri i plotë për tu faktorizuar.
        order_finder: Funksioni për gjetjen e rendit të elementeve të
 grupit multiplikativ të numrave të plotë modulo n.
        max_attempts: limiti i epërm i numrit të thirrjes së metodës order_finder

    Si rezultat kthen:
        Faktorin jo-trivial të n apo None nëse ai nuk është gjetur.
        Faktori k i n është trivial në qoftë se është 1 apo n.
    """
    # Nëse numri është i thjeshtë, nuk ka faktorë jo-trivialë
    if sympy.isprime(n):
        print("n is prime!")
        return None

    # Nëse numri është çift, dyshi është një faktor jo-trivial
    if n % 2 == 0:
        return 2

    # Nëse n është fuqi e një numri të thjeshtë, gjendet faktori jo-trivial 
    c = find_factor_of_prime_power(n)
    if c is not None:
        return c

    for _ in range(max_attempts):
        # Zgjedhja e një numri të rastësishëm mes 2 dhe n-1
        x = random.randint(2, n - 1)

        
        c = math.gcd(x, n)

        if 1 < c < n:
            return c

        # Llogaritja e rendit r të x modulo n 
        r = order_finder(x, n)

        # Nëse përcaktuesi i rendit kthen None
        if r is None:
            continue

        # Nëse rendi është tek:
        if r % 2 != 0:
            continue

        # Compute the non-trivial factor.
        y = x**(r // 2) % n
        assert 1 < y < n
        c = math.gcd(y - 1, n)
        if 1 < c < n:
            return c

    print(f"Failed to find a non-trivial factor in {max_attempts} attempts.")
    return None
