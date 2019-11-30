pizza = {"salt", "ground pepper", "cheese", "dough", "sweet basil",
         "oregano", "pepperoni", "garlic", "tomatoes", "onion"}

shaverma = {"cabbage", "fried chicken", "cucumbers", "sauce",
            "lavash", "tomatoes", "onion"}


bynary_and, intersection = pizza & shaverma, pizza.intersection(shaverma)
print(bynary_and)

substraction, difference = pizza - shaverma, pizza.difference(shaverma)
print(substraction)

bynary_ex_or, symmetric_difference = pizza ^ shaverma, pizza.symmetric_difference(shaverma)
print(bynary_ex_or)

equality = pizza == shaverma
print(equality)

_in1, _in2 = "salt" in pizza, "onion" in shaverma
print(_in1, _in2)

_is = pizza is shaverma
print(_is)

elements_one_enter_two = pizza < shaverma  # NOTE one should not be equal two (return False)
print(elements_one_enter_two)

elements_two_enter_one = pizza > shaverma  # NOTE one should not be equal two (return False)
print(elements_two_enter_one)

issubset_1, issubset_2, issubset_3 = pizza <= shaverma, \
                                     pizza.issubset(shaverma), \
                                     pizza.issubset(pizza | shaverma)
print(issubset_1, issubset_2, issubset_3)

issuperset_1, issuperset_2, issuperset_3 = pizza >= shaverma, \
                                           pizza.issuperset(shaverma), \
                                           (pizza | shaverma).issuperset(shaverma)

print(issuperset_1, issuperset_2, issuperset_3)

is_dis_joint = pizza.isdisjoint(shaverma)
print(is_dis_joint)

bynary_or, update = pizza | shaverma, pizza.update(shaverma)
print(bynary_or)

clear = pizza.clear() is None
print(clear)
