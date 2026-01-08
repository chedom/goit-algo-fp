def dynamic_programming(items, budget):
    ordered_items = [(k, v) for k, v in items.items()]
    items_count = len(ordered_items)
    # initialize table with partial solutions
    K = [[0 for w in range(budget + 1)] for i in range(items_count + 1)]
    # fill the table with partial solutions
    for i in range(items_count+1):
        for w in range(budget+1):
            if i == 0 or w == 0:  # no calories if 0 budget or 0 items
                K[i][w] = 0
                continue

            item_name, item_val = ordered_items[i-1]
            # the cost of the item is equal or lower than the budget
            if item_val["cost"] <= w:
                # calories of the item + calories for left budget
                calories_with_item = item_val["calories"] + K[i-1][w-item_val["cost"]]
                calories_without_item = K[i-1][w]  # calories without the item
                # save the bigger value
                K[i][w] = max(calories_with_item, calories_without_item)
            else:  # the cost of the item is bigger than the budget
                K[i][w] = K[i-1][w]
    # find selected products
    selected_items = []
    left_budget = budget
    # go backward to restore selected products
    for i in range(items_count, 0, -1):
        # no reason to check out of boundary as the last iteration is `i = 1`
        if K[i][left_budget] == K[i-1][left_budget]:
            continue  # item has not been selected

        item_name, item_val = ordered_items[i-1]

        if left_budget - item_val["cost"] < 0:
            continue

        left_budget -= item_val["cost"]
        selected_items.append(item_name)

    return (selected_items, K[items_count][budget])
