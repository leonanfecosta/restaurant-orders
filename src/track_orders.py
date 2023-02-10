class TrackOrders:
    def __init__(self):
        self.list_of_orders = []

    def __len__(self):
        return len(self.list_of_orders)

    def add_new_order(self, customer, order, day):
        self.list_of_orders.append(
            {"name": customer, "dish": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        count_orders = {}
        for order in self.list_of_orders:
            if order["name"] == customer:
                if order["dish"] not in count_orders:
                    count_orders[order["dish"]] = 1
                else:
                    count_orders[order["dish"]] += 1

        return max(count_orders, key=count_orders.get)

    def get_never_ordered_per_customer(self, customer):
        order_set = set()
        client_set = set()
        for order in self.list_of_orders:
            order_set.add(order["dish"])
            if order["name"] == customer:
                client_set.add(order["dish"])

        return order_set.difference(client_set)

    def get_days_never_visited_per_customer(self, customer):
        orders_set = set()
        client_set = set()

        for order in self.list_of_orders:
            if order['name'] == customer:
                client_set.add(order['day'])
            orders_set.add(order['day'])
        return orders_set.difference(client_set)

    def get_busiest_day(self):
        count_orders = {}
        for order in self.list_of_orders:
            if order["day"] not in count_orders:
                count_orders[order["day"]] = 1
            else:
                count_orders[order["day"]] += 1

        return max(count_orders, key=count_orders.get)

    def get_least_busy_day(self):
        count_orders = {}
        for order in self.list_of_orders:
            if order["day"] not in count_orders:
                count_orders[order["day"]] = 1
            else:
                count_orders[order["day"]] += 1

        return min(count_orders, key=count_orders.get)
