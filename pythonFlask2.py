from flask import Flask
from flask import request

import Variables

app = Flask(__name__)

# Пока что по умолчанию считаем что все обЪекты есть в "Базе", т.е. в list_of_object.тхт и в Variables.list_of_object
# и в Variables.dictionary_of_object

lines1 = []
with open('data/list_of_objects/list_of_objects.txt', 'r') as fp:  # Считываем объекты из файла в лист
    for n, line in enumerate(fp, 1):
        line = line.rstrip('\n')
        lines1.append(line)
Variables.list_of_object = lines1
Variables.dictionary_of_object = dict.fromkeys(Variables.list_of_object,
                                               "In run")  # create dictionary from objects and data storage
print(Variables.dictionary_of_object)


@app.route("/data_receive", methods=['GET', ])
def setinfo():
    # Получить значение параметра id во входящем URL http://localhost:5000/data?id=0001&data_time=05.09.2022,
    # 06:23&event=1-1,2-1,3-1,4-0.5-1,6-1,7-0
    sendid = request.args.get('id')
    getdata = request.args.get('data')

    if str(sendid) in Variables.list_of_object:  # Проверяем, что объект есть в листе, если нет
        pass
    else:
        Variables.list_of_object.append(str(sendid))  # - обновляем лист
        Variables.dictionary_of_object[str(sendid)] = str(getdata)  # - обновляем словарь по ID и пишем в него значение
        with open("data/list_of_objects/list_of_objects.txt", "a") as f:   # и пишем объект в файл списка объектов
            f.write(str(sendid) + "\n")
    try:
        Variables.dictionary_of_object[str(sendid)] = str(getdata)
        with open("data/" + str(sendid) + ".txt", "w") as f:  # Пишем событие в файл и в словарь

            f.write(getdata)

        return "Ok"
    except:
        return "Error"


@app.route("/data_get", methods=['GET', ])
def getinfo():
    getid = request.args.get('id')       # Получаем значение ID из запроса
    with open("data/" + str(getid) + ".txt", 'r') as f:     # получаем значение из файла, что уже по сути не нужно
        a = f.read()  # .split('\n')
    dict_value = Variables.dictionary_of_object.pop(str(getid))     # получаем значение из словаря
    return str(a + " " + dict_value)    # и отдаем


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
