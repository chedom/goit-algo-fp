from greedy_algo import greedy_algorithm
from dp_programming import dynamic_programming


def demo():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    print("DP and greedy provide the same results")
    run_algorithms(items, 50)  # the same result
    print("Greedy doesnt provide optimal result")
    run_algorithms(items, 70)  # greedy doesnt provide optimal solution


def run_algorithms(items, budget):
    selected_greedy, total_greedy = greedy_algorithm(items, budget)
    print(f"Greedy: total: {total_greedy}, selected: {sorted(selected_greedy)}")
    selected_dp, total_dp = dynamic_programming(items, budget)
    print(f"DP    : total: {total_dp}, selected: {sorted(selected_dp)}")


def main():
    demo()


if __name__ == "__main__":
    main()
