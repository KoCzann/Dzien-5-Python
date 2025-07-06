shopping_list = input("Podaj listę zakupów oddzielając elementy przecinkami: ").split(",")
print("Twoja lista zakupów:")
for item in shopping_list:  
    print(f"-> {item.strip()}")  # .strip() usuwa ewentualne spacje z początku i końca każdego elementu