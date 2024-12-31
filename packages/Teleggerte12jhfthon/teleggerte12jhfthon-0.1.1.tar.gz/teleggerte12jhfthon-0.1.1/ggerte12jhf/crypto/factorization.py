import gmpy2

class Factorization:
    """
    Simple module to factorize large numbers really quickly using gmpy2.
    """
    @classmethod
    def factorize(cls, pq):
        """
        Factorizes the given large integer.

        :param pq: the prime pair pq.
        :return: a tuple containing the two factors p and q.
        """
        pq = gmpy2.mpz(pq)

        if pq % 2 == 0:
            return 2, int(pq // 2)

        # Use gmpy2's random functions
        y = gmpy2.mpz_random(gmpy2.random_state(), pq) + 1
        c = gmpy2.mpz_random(gmpy2.random_state(), pq) + 1
        m = gmpy2.mpz_random(gmpy2.random_state(), pq) + 1
        g = r = q = gmpy2.mpz(1)
        x = ys = gmpy2.mpz(0)
        i = gmpy2.mpz(0)

        while g == 1:
            x = y
            for i in range(r):
                y = (gmpy2.powmod(y, 2, pq) + c) % pq

            k = gmpy2.mpz(0)
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = (gmpy2.powmod(y, 2, pq) + c) % pq
                    q = (q * abs(x - y)) % pq

                g = cls.gcd(q, pq)
                k += m

            r *= 2

        if g == pq:
            while True:
                ys = (gmpy2.powmod(ys, 2, pq) + c) % pq
                g = cls.gcd(abs(x - ys), pq)
                if g > 1:
                    break

        q = pq // g
        return (int(g), int(q)) if g < q else (int(q), int(g))

    def gcd(a, b):
        """
        Calculates the Greatest Common Divisor.

        :param a: the first number.
        :param b: the second number.
        :return: GCD(a, b)
        """
        a = gmpy2.mpz(a)
        b = gmpy2.mpz(b)
        while b:
            a, b = b, a % b

        return a
