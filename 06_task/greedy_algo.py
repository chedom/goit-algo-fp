def greedy_algorithm(items, budget):
    # sort by calories per dollar ratio
    sorted_by_calories_ration = sorted(
        [(k, v) for k, v in items.items()],
        key=lambda item: item[1]["calories"]/item[1]["cost"],
        reverse=True)

    total_calories = 0
    selected_items = []

    for item in sorted_by_calories_ration:
        if item[1]["cost"] > budget:  # do not have enough budget to buy the item
            continue

        budget -= item[1]["cost"]
        total_calories += item[1]["calories"]
        selected_items.append(item[0])

    return (selected_items, total_calories)
