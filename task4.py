dict_int = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("test.txt", encoding='utf-8') as f_obj:
    for line in f_obj:
        for key in dict_int.keys():
            line = line.replace(key, dict_int[key])
        print(line)
        with open("test.txt", "a") as f_rus:
            f_rus.write(f"\n {line}")