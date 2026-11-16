import time
import threading
import multiprocessing


def cpu_task(n):
    while n > 0:
        n -= 1


def io_task(seconds):
    time.sleep(seconds)


def run_sequential(task, jobs):
    for job in jobs:
        task(job)


def run_threads(task, jobs):
    threads = []
    for job in jobs:
        thread = threading.Thread(target=task, args=(job,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def run_processes(task, jobs):
    processes = []
    for job in jobs:
        process = multiprocessing.Process(target=task, args=(job,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


def measure(runner, task, jobs):
    start = time.perf_counter()
    runner(task, jobs)
    return time.perf_counter() - start


if __name__ == "__main__":
    cpu_jobs = [10_000_000] * 4
    io_jobs = [1.0] * 4

    print("          | თანმიმდევრულად | thread-ები | პროცესები")

    for label, task, jobs in [("CPU-bound", cpu_task, cpu_jobs), ("I/O-bound", io_task, io_jobs)]:
        sequential_time = measure(run_sequential, task, jobs)
        threads_time = measure(run_threads, task, jobs)
        processes_time = measure(run_processes, task, jobs)

        row = f"{label} | {sequential_time:.2f} წმ ({1:4.1f}x)"
        row = row + f" | {threads_time:.2f} წმ ({sequential_time / threads_time:4.1f}x)"
        row = row + f" | {processes_time:.2f} წმ ({sequential_time / processes_time:4.1f}x)"
        print(row)

# CPU-bound ამოცანა thread-ებით არ დაჩქარდა, რადგან Python-ში GIL-ის გამო ერთ მომენტში
# მხოლოდ ერთი thread ასრულებს კოდს, ამიტომ thread-ები ერთმანეთს რიგრიგობით ელოდებიან.
# I/O-bound ამოცანა დაჩქარდა, რადგან ლოდინის (sleep) დროს thread GIL-ს ათავისუფლებს
# და ყველა thread ერთდროულად ელოდება. პროცესებს თითოეულს საკუთარი GIL აქვს,
# ამიტომ ისინი CPU-bound ამოცანასაც სხვადასხვა ბირთვზე პარალელურად ასრულებენ.
