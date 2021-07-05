from pprint import pprint

def get_cook_book_by_dishes():
    with open('Список рецептов.txt', 'r', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.lower().strip()
            counter = f.readline().strip()
            list_of_ingredient = []
            for i in range(int(counter)):
                ingredients_list = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingredient = f.readline().strip().split(" | ")
                for item in ingredient:
                    ingredients_list['ingredient_name'] = ingredient[0]
                    ingredients_list['quantity'] = ingredient[1]
                    ingredients_list['measure'] = ingredient[2]
                list_of_ingredient.append(ingredients_list)
                cook_list = {dish_name: list_of_ingredient}
                cook_book.update(cook_list)
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book_by_dishes()
    shop_list = {}
    for dish in dishes:
        for item in cook_book[dish]:
            ingredients_list = dict([(item['ingredient_name'],
                                      {'measure': item['measure'], 'quantity': int(item['quantity']) * person_count})])
            if shop_list.get(item['ingredient_name']):
                new_shop_list = (int(shop_list[item['ingredient_name']]['quantity']) +
                                int(ingredients_list[item['ingredient_name']]['quantity']))
                shop_list[item['ingredient_name']]['quantity'] = new_shop_list
            else:
                shop_list.update(ingredients_list)
    return shop_list

def get_command():
    with open('Список рецептов.txt', 'r', encoding='utf-8') as f:
        dish_list = f.read()
        print('Наши блюда:\n', dish_list)
        cook_book = get_cook_book_by_dishes()
        pprint(cook_book)
        dishes = input('\nВведите блюдо: ').lower().split(', ')
        person_count =int(input('Введите количество персон: '))
        shop_list = get_shop_list_by_dishes(dishes, person_count)
        print('Необходимо купить:')
        pprint(shop_list)



get_cook_book_by_dishes()
get_command()
get_shop_list_by_dishes()
