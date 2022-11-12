with open("recipes.txt", 'rt', encoding='utf-8') as recipes_file:
    recipes_dict = {}
    for dish in recipes_file:
        recipes_name = dish.strip()
        count_ingredient = int(recipes_file.readline())
        recipes_dict[recipes_name] = []
        dish_list = []
        for ingredient in range(count_ingredient):
            ing = recipes_file.readline().strip().split(' | ')
            ingredient_name, quantity, measur = ing
            dish_list.append({'ingredient_name' : ingredient_name,
                                           'quantity' : quantity,
                                           'measur' : measur})
            print(ingredient_name, quantity, measur)
        recipes_file.readline()
        recipes_dict[recipes_name] = dish_list
    print(recipes_dict)
recipes_file.close()

def get_shop_list_by_dishes(dish, person_count):
    shop_list_by_dishes = {}
    for dish_name in recipes_dict:
        if dish == dish_name:
            for ingredient in recipes_dict[dish_name]:
                ingredient_name = ingredient['ingredient_name']
                measur = ingredient['measur']
                quantity = ingredient['quantity']
                if ingredient_name in shop_list_by_dishes:
                    shop_list_by_dishes[ingredient_name]['quantity']= int(shop_list_by_dishes[ingredient_name].get('quantity')) + int(quantity) * int(person_count)
                else:
                    shop_list_by_dishes[ingredient_name] = {'measur' : measur, 'quantity' : int(quantity) * int(person_count)}
            print(shop_list_by_dishes)
get_shop_list_by_dishes()





