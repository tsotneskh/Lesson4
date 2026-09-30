age = int(input("შეიყვანეთ თქვენი ასაკი: "))
with_parents = input("მშობელთან ერთად ხართ (კი/არა): ").strip()

if (age >= 18 or with_parents == "კი") and age >= 12:
    print("შესვლა დაშვებულია")
else:
    print("შესვლა აკრძალულია")
    