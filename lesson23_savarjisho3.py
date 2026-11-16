# 1. რა მოხდა გაშვებისას: არაფერი დაიბეჭდა და გამოჩნდა გაფრთხილება
#    RuntimeWarning: coroutine 'main' was never awaited

import asyncio
import time


async def load_user(user_id):
    await asyncio.sleep(1)  # შეცდომა 1: time.sleep მთელ პროგრამას აჩერებს, async-ში await asyncio.sleep უნდა
    return {"id": user_id, "name": f"მომხმარებელი {user_id}"}


async def main():
    start = time.perf_counter()
    users = await asyncio.gather(*(load_user(user_id) for user_id in (1, 2, 3)))  # შეცდომა 2: load_user() await-ის გარეშე მხოლოდ კორუტინის ობიექტს ქმნის და არ სრულდება; gather-ით სამივე ერთდროულად სრულდება
    print(users)
    print(f"დრო: {time.perf_counter() - start:.1f} წმ")


asyncio.run(main())  # შეცდომა 3: main() პირდაპირ გამოძახებით არ ეშვება, კორუტინა asyncio.run()-ით უნდა გაეშვას
