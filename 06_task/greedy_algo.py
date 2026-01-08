def greedy_algorithm(items, budget):
    # sort by calories per dollar ratio
    sorted_by_calories_ration = sorted(
        [(k, v) for k, v in items.items()],
        key=lambda item: item[1]["calories"]/item[1]["cost"],
        reverse=True)

    total = 0
    selected_items = []

    for item in sorted_by_calories_ration:
        cost = item[1]["cost"]
        if cost + total > budget:  # do not have enough budget to buy the item
            continue

        total += cost
        selected_items.append(item[0])

    return (selected_items, total)
