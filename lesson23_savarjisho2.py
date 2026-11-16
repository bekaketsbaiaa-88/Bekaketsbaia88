import asyncio
import time


async def square(number):
    await asyncio.sleep(1)
    return number * number


numbers = [1, 2, 3, 4, 5, 6, 7, 8]


async def main():
    start = time.perf_counter()

    # 1. ყველა კვადრატი ერთდროულად
    squares = await asyncio.gather(*(square(number) for number in numbers))

    # 2. თითო ხაზზე N² = X
    for number, result in zip(numbers, squares):
        print(f"{number}² = {result}")

    # 3. ჯამი და დრო
    print("ჯამი:", sum(squares))
    print(f"დრო: {time.perf_counter() - start:.1f} წმ")


asyncio.run(main())

# 4. დრო ≈ 1 წამია, რადგან gather რვავე კორუტინას ერთდროულად უშვებს და ისინი ერთ წამს ერთად ელოდებიან,
#    ერთმანეთის მიყოლებით კი არა (რაც 8 წამი იქნებოდა).
