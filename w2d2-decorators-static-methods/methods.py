# instance methods, static methods, class methods

import math

class Pizza:
    base_ingredients = []

    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients
        Pizza.base_ingredients.extend(ingredients)

    def pizza_amount(self):     # instance method
        return self.circle_area(self.radius)

    @staticmethod           # static method
    def circle_area(r):
        return r ** 2 * math.pi   

    @classmethod
    def margharita(cls, radius):
        return cls(radius, ['mozzarella', 'tomatoes'])
    
    @staticmethod
    def margharita2(radius):
        return Pizza(radius, ['mozzarella', 'tomatoes'])


p = Pizza(2, ['cheese'])
print(p.pizza_amount())

m_p = Pizza.margharita2(5)


print(Pizza.base_ingredients)
print(p.ingredients)


print(m_p.ingredients)



# print(Pizza.circle_area(2))