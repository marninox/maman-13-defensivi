class AppleBasket:
    def __init__(self, color, quantity):
        self.color_apple = color
        self.quantity_apple = quantity

    def increase(self):
        self.quantity_apple += 1

    def __str__(self):
        return f"A basket of {self.quantity_apple} {self.color_apple} apples."


class GreenAppleBasket(AppleBasket):
    def __init__(self, quantity):
        super().__init__('green', quantity)


# Testing the classes according to the MAMAN examples 
basket1 = AppleBasket('red', 3)
basket1.increase()

basket2 = GreenAppleBasket(49)
basket2.increase()

print(basket1)
print(basket2)