from pprint import pprint
with open('cook_book.txt', encoding='utf-8') as f:
    lines = f.readlines()
    list_ = [[]]
    for string in lines:
        if string != '\n':
            if '|' in string:
                list_[-1].append(string.strip().split('|'))
            else:
                list_[-1].append(string.strip())
        else:
            list_.append([])
    cook_book = {}
    for dish in list_:
        value = []
        for ingredient in dish:
            if type(ingredient) == list:
                dict_ingredient = dict(ingredient_name=ingredient[0], quantity=ingredient[1], measure=ingredient[2])
                value.append(dict_ingredient)
        cook_book[dish[0]] = value

print(cook_book)