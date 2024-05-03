from queue import Queue
import random

queue = Queue()
id_gen = 1

def generate_request():
  global id_gen
  text = input('Введіть текст заявки: \n')
  newItem = {
    "id": id_gen,
    "text": text
  }
  queue.put(newItem)
  print(f"\nВаша заявка з ID {newItem['id']} успішно добавлена\n1")
  id_gen = id_gen + 1

def process_request():
  if not queue.empty():
    item = queue.get()
    print(f"\nЗаявка ID: {item['id']} \n {item['text']} \n\n Заявка успішно оброблена \n")
  else:
    print("\nЧерга пуста\n")
    
def main():
    print("Черга заявок\n")
    while True:
        user_input = input("Введіть команду: \n 1: Додати заявку \n 2: Обробити заявку \n 3: Вийти \n\n $ ")

        if user_input == "3":
            break
        elif user_input == "1":
            generate_request()
        elif user_input == "2":
            process_request()
        else:
            print("Невірна команда")

if __name__ == "__main__":
    main()
