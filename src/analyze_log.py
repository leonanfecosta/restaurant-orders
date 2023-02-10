def favorite_order(name, orders):
    count_orders = {}
    for order in orders:
        if order["name"] == name:
            if order["dish"] not in count_orders:
                count_orders[order["dish"]] = 1
            else:
                count_orders[order["dish"]] += 1

    return max(count_orders, key=count_orders.get)


def many_times_ordered(name, dish, orders):
    count = 0
    for order in orders:
        if order["name"] == name and order["dish"] == dish:
            count += 1

    return count


def analyze_log(path_to_file):
    raise NotImplementedError
