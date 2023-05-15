dx = 1e-7
i = 0

# TODO: calculate the integrals asynchronously

pi = 0

def f(x):
    return 4 / (1 + (x**2))

while i <= 1:
    pi += f(i)
    print(f"[PI] {pi} {round(i*100, 2)}% complete", end='\r')
    i += dx

print(pi)