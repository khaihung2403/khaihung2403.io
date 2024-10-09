class py_solution:
    def int_to_Roman(self, num):
        so = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        kitu = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        mangmoi = ""
        for i in range(len(so)):
            solan = num//so[i]
            mangmoi += kitu[i]*solan
            num = num - so[i]*solan
        return mangmoi

    
print(py_solution().int_to_Roman(4000))

