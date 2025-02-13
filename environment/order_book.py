class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def place_order(self, order_type, asset, quantity, price):
        order = {"asset": asset, "quantity": quantity, "price": price}
        if order_type == "buy":
            self.buy_orders.append(order)
        elif order_type == "sell":
            self.sell_orders.append(order)
        self.match_orders()

    def match_orders(self):
        self.buy_orders.sort(key=lambda x: x["price"], reverse=True)
        self.sell_orders.sort(key=lambda x: x["price"])
        
        while self.buy_orders and self.sell_orders:
            buy_order = self.buy_orders[0]
            sell_order = self.sell_orders[0]
            
            if buy_order["price"] >= sell_order["price"]:
                quantity_traded = min(buy_order["quantity"], sell_order["quantity"])
                buy_order["quantity"] -= quantity_traded
                sell_order["quantity"] -= quantity_traded
                
                if buy_order["quantity"] == 0:
                    self.buy_orders.pop(0)
                if sell_order["quantity"] == 0:
                    self.sell_orders.pop(0)
            else:
                break


if __name__ == "__main__":
    order_book = OrderBook()
    order_book.place_order("buy", "AAPL", 10, 150)
    order_book.place_order("sell", "AAPL", 5, 148)
    print("Orders processed.")
