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


def wich_dish_not_ordered(name, orders):
    order_set = set()
    client_set = set()
    for order in orders:
        order_set.add(order["dish"])
        if order["name"] == name:
            client_set.add(order["dish"])

    return order_set.difference(client_set)


def which_days_not_went(name, orders):
    orders_set = set()
    client_set = set()

    for order in orders:
        if order['name'] == name:
            client_set.add(order['day'])
        orders_set.add(order['day'])
    return orders_set.difference(client_set)

def analyze_log(path_to_file):
    raise NotImplementedError
