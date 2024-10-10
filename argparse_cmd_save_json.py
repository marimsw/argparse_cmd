import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Мой парсер')
    parser.add_argument('-c', '--creator', help='Создатель',type=str, required=True) # создатель:"создатель": "компания_Russ"
    parser.add_argument('-u', '--use', help='Применение', type=str, required=True) # применение: "применение": "модерация_макетов"
    parser.add_argument('-y', '--year', help='Год создания нейросети',type=int, default=2024) # "год создания нейросети": "2024"
    parser.add_argument('-a', '--architecture', help='Архитектура', type=str, default='Обучение с учителем') # "архитектура": "Обучение_с_учителем"
    parser.add_argument('-s', '--stage', help='Этап', type=str, default='сбор данных') # "этап": "сбор данных"

    args = parser.parse_args()

    # Сохраняем входные значения в формате JSON
    data = {
        'creator': args.creator,
        'use': args.use,
        'year': args.year,
        'architecture': args.architecture,
        'stage': args.stage
    }
    with open('input_values1.json', 'a', encoding='utf-8') as f:
       try:
           f.seek(0, 2)  # переместить указатель в конец файла
           f.seek(f.tell() - 1, 0)  # переместить указатель на последний символ
           if f.read(1) == ']':  # если последний символ - ]
               f.seek(f.tell() - 1, 0)  # переместить указатель на предпоследний символ
               f.truncate()  # удалить последний символ
           f.write(',\n')
           json.dump(data, f, indent=4, ensure_ascii=False)
           f.write('\n]')
       except ValueError:
           f.seek(0, 0)  # переместить указатель в начало файла
           f.write('[\n')
           json.dump(data, f, indent=4 , ensure_ascii=False)
           f.write('\n]')

    print('Входные значения сохранены в файле input_values.json')

if __name__ == '__main__':
    main()
