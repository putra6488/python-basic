import time
start_time = time.time()

print('hello world')
a = 10
print(a)
for i in range(1, 1000):
    a = 10

print(time.time() - start_time)
