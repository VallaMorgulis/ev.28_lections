from colorama import Fore


speach = input()
list_ = speach.split(' ')
filter_list = [Fore.BLUE + x if x.istitle() else Fore.RESET + x for x in list_]
color_speach = ' '.join(filter_list)
print(color_speach)


# print(Fore.BLACK + 'Черный')
# print(Fore.WHITE + 'Белый')
# print(Fore.RED + 'Красный')
# print(Fore.GREEN + 'Зеленый')
# print(Fore.YELLOW + 'Желтый')
# print(Fore.BLUE + 'Синий')
# print(Fore.MAGENTA + 'Пурпурный')

# # Fore.RESET устанавливает цвет таким, каким он был 
# # до первой покраски
# print(Fore.RESET + 'Цвет по-умолчанию')
