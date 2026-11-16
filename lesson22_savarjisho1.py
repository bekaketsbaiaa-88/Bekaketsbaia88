import time
import threading


def make_tea(name, seconds):
    print(f"{name}: იწყება")
    time.sleep(seconds)
    print(f"{name}: მზადაა")


teas = [("მწვანე ჩაი", 1.0), ("შავი ჩაი", 1.5), ("ბალახის ჩაი", 2.0)]

# 1. თანმიმდევრულად
start = time.perf_counter()
for name, seconds in teas:
    make_tea(name, seconds)
sequential_time = time.perf_counter() - start
print(f"თანმიმდევრულად: {sequential_time:.1f} წმ")

# 2. thread-ებით
start = time.perf_counter()
threads = []
for name, seconds in teas:
    thread = threading.Thread(target=make_tea, args=(name, seconds))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
threads_time = time.perf_counter() - start
print(f"thread-ებით: {threads_time:.1f} წმ")

# 3. დაჩქარება
print(f"დაჩქარება: {sequential_time / threads_time:.1f}x")

# 4. სამივე ჩაი ერთდროულად იწყებს ლოდინს, ამიტომ პროგრამა მხოლოდ მანამდე ელოდება,
#    სანამ ყველაზე ხანგრძლივი ჩაი (ბალახის ჩაი, 2 წმ) არ მომზადდება.
