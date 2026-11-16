import asyncio
import time


async def deliver(order, seconds):
    print(f"{order}: გაიგზავნა")
    await asyncio.sleep(seconds)
    print(f"{order}: მიტანილია")


orders = [("შეკვეთა #1", 1.0), ("შეკვეთა #2", 1.5), ("შეკვეთა #3", 2.0)]


async def main():
    # 1. ზედიზედ
    start = time.perf_counter()
    for order, seconds in orders:
        await deliver(order, seconds)
    one_by_one_time = time.perf_counter() - start
    print(f"ზედიზედ: {one_by_one_time:.1f} წმ")

    # 2. ერთდროულად
    start = time.perf_counter()
    await asyncio.gather(*(deliver(o, s) for o, s in orders))
    together_time = time.perf_counter() - start
    print(f"ერთდროულად: {together_time:.1f} წმ")

    # 3. დაჩქარება
    print(f"დაჩქარება: {one_by_one_time / together_time:.1f}x")


asyncio.run(main())

# 4. gather-ით სამივე შეკვეთა ერთდროულად იწყებს ლოდინს, ამიტომ პროგრამა მხოლოდ მანამდე ელოდება,
#    სანამ ყველაზე ხანგრძლივი შეკვეთა (შეკვეთა #3, 2 წმ) არ მიიტანება.
