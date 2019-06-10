class CombTools(object):
    def __init__(self, cap: int, mod: int):
        self.cap = cap
        self.mod = mod
        self.inv = self._calc_inv()
        self.fac = self._calc_fac()
        self.fac_inv = self._calc_fac_inv()

    def _calc_inv(self):
        inv = [0, 1]
        for i in range(2, self.cap+1):
            inv.append((self.mod - (self.mod // i) * inv[self.mod % i]) % self.mod)

        return inv

    def _calc_fac(self):
        fac = [1]
        for i in range(1, self.cap+1):
            fac.append((i * fac[-1]) % self.mod)

        return fac

    def _calc_fac_inv(self):
        fac_inv = [1]
        for i in range(1, self.cap+1):
            fac_inv.append((self.inv[i] * fac_inv[-1]) % self.mod)

        return fac_inv

    def nCr(self, n: int, r: int):
        # validation
        if r > n:
            raise ValueError("n must be larger than r (n={}, r={})".format(n, r))

        # calculation
        return self.fac[n] * self.fac_inv[n-r] * self.fac_inv[r] % self.mod

    def nPr(self, n: int, r: int):
        # validation
        if r > n:
            raise ValueError("n must be larger than r (n={}, r={})".format(n, r))

        # calculation
        return self.fac[n] * self.fac_inv[n-r] % self.mod

    def nHr(self, n: int, r: int):
        return self.nCr(n+r-1, n)

