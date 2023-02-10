import csv


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
    if not str(path_to_file).endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")
    try:
        orders_list = []
        with open(path_to_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                orders_list.append(
                    {"name": row[0], "dish": row[1], "day": row[2]})

        favorite_order_maria = favorite_order("maria", orders_list)
        many_times_ordered_arnaldo = many_times_ordered(
            "arnaldo", "hamburguer", orders_list)
        wich_dish_not_ordered_joao = wich_dish_not_ordered("joao", orders_list)
        which_days_not_went_joao = which_days_not_went("joao", orders_list)

        with open("data/mkt_campaign.txt", "w") as f:
            f.write(
                f"{favorite_order_maria}\n"
                f"{many_times_ordered_arnaldo}\n"
                f"{wich_dish_not_ordered_joao}\n"
                f"{which_days_not_went_joao}\n"
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")
