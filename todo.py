import time
import ast

#Йо. Этому коду около полугода, поэтому... Ну, как говорится, когда я писал этот код, как он работает знали только я и бог. Теперь знает только бог.


def clear():
    #Эт просто чистилка консоли.
    print("\033c", end="", flush=True)

def show():
    #Это... Ну, простой цикл, который показывает весь список дел.
    for i in dos:
        if dos[i][1] == False:
            print(f"{i}. [ ] {dos[i][0]}")
        else:
            print(f"{i}. [X] {dos[i][0]}")

def out():
    #чё это такое даже знать не хочу. Зачем я сделал из двух строк одну функцию я понятия не имею...
    show()
    input("Нажмите enter чтобы продолжить...")

def app():
    #Это... Ну, судя по всему, функция добавления задачи.
    add = []
    for i in dos:
        a = i+1
        if a not in dos:
            add.append(a)
        else:
            pass
    dos[add[0]] = ['', False]
    dos[add[0]][0] = input("Введите описание задачи: ")
    print("Задача добавлена!")
    input("Нажмите enter чтобы продолжить...")

def vyp():
    #Что за сокращение такое... Даже думать боюсь.
    show()
    a = int(input("Введите номер задачи: "))
    if a in dos:
       dos[a][1] = True
    else:
        print("Этого номера нет в списке!")
    input("Нажмите enter чтобы продолжить...")

def is_one():
    #Просто проверка на последнюю задачу.
    count = 0
    for i in dos:
        count += 1
    if count > 1:
        return True
    else:
        return False

def delete():
    #Это удаление, и... Если я правильно помню, именно оно создало мне не мало проблемок, когда я это писал, хехе.
    deleted = []
    show()
    a = int(input("Введите номер задачи: "))
    if a in dos:
        if is_one() == True:
            del dos[a]
            print("Задача удалена")
        else:
            print("Нельзя удалить последнюю задачу в списке!")
            input()
            return
        
        for i in dos:
            if a < i:
                deleted.append(i)
            else:
                pass
        for el in deleted:
            dos[el-1] = dos.pop(el)
        
    else:
        print("Такой задачи нет в списке!")
    input("Нажмите enter чтобы продолжить...")

with open("safes.txt", 'r', encoding='utf=8') as file:
    #ммм, загрузка задач из файла... мгм.
    dos3 = file.read()
    dos = ast.literal_eval(dos3)

while True:
    #Основной цикл... Интересно я вывожу, конечно, подобие интерфейса. Зато в одну строку записал.
    clear()
    print("===== Список дел =====\nвыберите действие:\n1. Показать все задачи\n2. Добавить задачу\n3. Отметить задачу как выполненную\n4. Удалить задачу\n5. Выйти\n\n")
    try:
        inp = int(input("Ваш выбор: "))
        match inp:
            case 1:
                out()
            case 2:
                app()
            case 3:
                vyp()
            case 4:
                delete()
            case 5:
                print("До свидания!")
                time.sleep(1)
                break
    except ValueError:
        print('Введите число!')
        input("enter чтобы продолжить")
    except IndexError:
        print("такого варианта нет!")
        input("enter чтобы продолжить")

#ну, сохранение выходит.

with open("safes.txt", "w", encoding='utf=8') as file:
    file.write(str(dos)) 