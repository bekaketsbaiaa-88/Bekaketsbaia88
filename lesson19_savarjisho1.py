def constant_time(data):
    # O(1) — მონაცემი რამდენიც არ უნდა იყოს, მხოლოდ პირველ ელემენტს ვამოწმებთ
    steps = 0
    for item in data:
        steps = steps + 1
        print("პირველი ელემენტი:", item)
        break
    print("O(1) — შემოწმებების რაოდენობა:", steps)


def linear_time(data):
    # O(n) — თითოეულ ელემენტს ერთხელ ვამოწმებთ
    steps = 0
    total = 0
    for item in data:
        steps = steps + 1
        total = total + item
    print("ჯამი:", total)
    print("O(n) — შემოწმებების რაოდენობა:", steps)


def quadratic_time(data):
    # O(n²) — თითოეულ ელემენტს ყველა ელემენტთან ვადარებთ
    steps = 0
    same_pairs = 0
    for first in data:
        for second in data:
            steps = steps + 1
            if first == second:
                same_pairs = same_pairs + 1
    print("ტოლი წყვილები:", same_pairs)
    print("O(n²) — შემოწმებების რაოდენობა:", steps)


numbers = [5, 3, 8, 1, 9]

constant_time(numbers)
linear_time(numbers)
quadratic_time(numbers)
