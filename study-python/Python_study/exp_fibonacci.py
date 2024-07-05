import time

start = time.time()

def fibonacci(n):
    if (n <= 1):
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);

print(fibonacci(4))
print(f"time : {time.time() - start:.2f}")