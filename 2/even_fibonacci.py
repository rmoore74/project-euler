fib_total  = [1, 2]
even_total = [2]

while (fib_total[-1] < 4000000):
    fib = fib_total[-1] + fib_total[-2]
    fib_total.append(fib)
    if fib % 2 == 0 : even_total.append(fib)

print "Even Total:      ", sum(even_total)
