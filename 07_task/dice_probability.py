import random
import matplotlib.pyplot as plt


def get_dice_value() -> int:
    return random.randint(1, 6)


def roll_dice() -> int:
    return get_dice_value() + get_dice_value()


def dice_experiment(roll_num: int):
    stats = {key: 0 for key in range(2, 13)}

    for _ in range(roll_num):
        sum = roll_dice()
        stats[sum] += 1

    print_experiment_result(stats, roll_num)
    build_experiment_plot(stats, roll_num)


def print_experiment_result(result: dict[int, int], roll_num):
    print(f"Experiment with {roll_num} rolls")
    print(f"{"Sum":<3} | {"Probability":<20}")
    print("-" * 25)

    for i in range(2, 13):
        hit_count = result.get(i, 0)
        hit_probability = (hit_count/roll_num)
        num_from_36 = round(hit_probability * 36)
        print(f"{i:<3} | {f"{hit_probability * 100:.2f}% ({num_from_36}/{36})":<20}")

    print("-" * 25)


def build_experiment_plot(result, roll_num):
    x = []  # for sums
    y = []  # for probabilities

    for k, v in result.items():
        x.append(k)
        y.append(v/roll_num)

    plt.figure(num=f"Experiment with {roll_num} rolls")
    # 2. Plot Y vs X
    plt.plot(x, y)

    # 3. Display the plot
    plt.show()

