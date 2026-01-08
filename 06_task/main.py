from greedy_algo import greedy_algorithm


def demo_greedy_algorithm():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    selected, total = greedy_algorithm(items, 50)
    print(f"Total {total} with items {selected}")  # ['cola', 'potato', 'pepsi']


def main():
    demo_greedy_algorithm()


if __name__ == "__main__":
    main()
