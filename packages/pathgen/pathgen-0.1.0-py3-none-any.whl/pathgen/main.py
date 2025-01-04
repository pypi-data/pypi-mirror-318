import os
import random
import string
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def generate_random_filename():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + '.txt'

def generate_paths(base_path, repeat_count):
    output = []
    for i in range(repeat_count):
        if i == 0:
            output.append(base_path)
        else:
            dir_name, filename = os.path.split(base_path)
            name, extension = os.path.splitext(filename)
            if '_' in name:
                prefix, suffix = name.rsplit('_', 1)
                new_filename = f"{prefix}{i+1}_{suffix}{extension}"
            else:
                new_filename = f"{name}{i+1}{extension}"
            new_path = os.path.join(dir_name, new_filename)
            output.append(new_path)
    return output

def main():
    print("Made by Avinion")
    print("Telegram: @akrim")
    print()

    while True:
        lang = input("Выберите язык (R • русский, E • английский) / Choose language (R • Russian, E • English): ").lower()
        if lang in ['r', 'e']:
            break
        print("Некорректный ввод. / Incorrect input.")

    while True:
        clear_console()
        if lang == 'r':
            base_path = input("Введите базовый путь (например, /storage/emulated/0/Download/classes_smali.zip): ")
            repeat_count = int(input("Сколько повторов создать? "))
        else:
            base_path = input("Enter the base path (e.g., /storage/emulated/0/Download/classes_smali.zip): ")
            repeat_count = int(input("How many repetitions to create? "))

        output = generate_paths(base_path, repeat_count)

        current_dir = os.getcwd()
        output_filename = generate_random_filename()
        output_path = os.path.join(current_dir, output_filename)

        with open(output_path, 'w') as f:
            f.write('\n'.join(output))

        if lang == 'r':
            print(f"Файл {output_filename} создан в текущей директории.")
            continue_work = input("Продолжить работу? (Y/N): ").lower()
        else:
            print(f"File {output_filename} created in the current directory.")
            continue_work = input("Continue working? (Y/N): ").lower()

        if continue_work != 'y':
            break

    clear_console()
    if lang == 'r':
        print("Спасибо за использование!")
    else:
        print("Thank you for using!")

if __name__ == "__main__":
    main()
