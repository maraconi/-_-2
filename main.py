from pprint import pprint

def get_shop_list_by_dishes(dishes, cook_book, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list_by_dishes = dict(ingredient)
            shop_list_by_dishes['quantity'] *= person_count
            if shop_list_by_dishes['ingredient_name'] not in shop_list:
                shop_list[shop_list_by_dishes['ingredient_name']] = shop_list_by_dishes
            else:
                shop_list[shop_list_by_dishes['ingredient_name']]['quantity'] += shop_list_by_dishes['quantity']
    return shop_list

def get_cook_book_by_dishes():
    cook_book = {}
    with open('Список рецептов.txt', 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            counter = f.readline().strip()
            list_of_ingredient = []
            for i in range(int(counter)):
                ingredient = f.readline().strip().split(" | ")
                ingredients_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                list_of_ingredient += [ingredients_dict]
            cook_book[dish_name] = list_of_ingredient
            f.readline().strip()
    return cook_book

def get_comand():
    with open('Список рецептов.txt', 'r', encoding='utf-8') as f:
        dish_list = f.read()
        cook_book = get_cook_book_by_dishes()
        print('Наши блюда:\n', dish_list)
        dishes = input('\nВведите блюдо: ')
        person_count =int(input('Введите количество персон: '))
        pprint(cook_book)
        shop_list = get_shop_list_by_dishes(dishes, cook_book, person_count)
        print(shop_list)

get_cook_book_by_dishes()
get_comand()
get_shop_list_by_dishes()
