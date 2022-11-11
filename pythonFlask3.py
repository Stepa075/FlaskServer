from flask import Flask
from flask import request

import Variables

app = Flask(__name__)

# Пока что по умолчанию считаем что все обЪекты есть в "Базе", т.е. в list_of_object.тхт и в Variables.list_of_object
# и в Variables.dictionary_of_object

lines1 = []
with open('data/list_of_objects/list_of_objects.txt', 'r', encoding="UTF-8") as fp:  # Считываем объекты из файла в лист
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
    getdatetime = request.args.get('datetime')
    sendid = request.args.get('id')
    getdata = request.args.get('data')

    Variables.dictionary_of_object[str(getdatetime)] = str(
        sendid + ' ' + getdata)  # - обновляем словарь по ID и пишем в него значение

    try:
        Variables.dictionary_of_object[str(getdatetime)] = str(sendid + ' ' + getdata)
        with open("data/dictionary_of_objects/dictionary_of_objects.txt", "a",
                  encoding="UTF-8") as f:  # Пишем событие в файл и в словарь
            f.write(str(getdatetime) + ': ' + str(sendid) + ' ' + str(getdata) + '\n')

        return "Ok"
    except:
        return "Error"


@app.route("/data_get", methods=['GET', ])
def getinfo():
    getid = request.args.get('id')  # Получаем значение ID из запроса
    # with open("data/" + str(getid) + ".txt", 'r') as f:     # получаем значение из файла, что уже по сути не нужно
    #     a = f.read()  # .split('\n')
    # получаем значение из словаря (ключ не удаляется, при его отсутствии будет None
    return Variables.dictionary_of_object


@app.route("/data_get_file", methods=['GET', ])
def getinfo_from_file():
    getid = request.args.get('id')  # Получаем значение ID из запроса
    with open("data/dictionary_of_objects/dictionary_of_objects.txt", 'r') as f:     # получаем значение из файла, что уже по сути не нужно
        a = f.read()
    # lines = [line.rstrip('\n') for line in open('data/dictionary_of_objects/dictionary_of_objects.txt')]

    # with open('data/dictionary_of_objects/dictionary_of_objects.txt', 'r') as fp:
    #     for n, line in enumerate(fp, 1):
    #         line = line.rstrip('\n')
    #         lines1.append(line)
    return a


@app.route("/data_set", methods=['GET', ])
def get_all_info():
    getcommand = request.args.get('command')
    getid = request.args.get('id')  # Получаем значение ID из запроса
    getvalue = request.args.get('value')
    if str(getcommand) == "add_object":
        Variables.list_of_object.append(str(getid))
        Variables.dictionary_of_object[str(getid)] = str(getvalue)  # - обновляем словарь по ID и пишем в него значение
        with open("data/list_of_objects/list_of_objects.txt", "a",
                  encoding="UTF-8") as f:  # и пишем объект в файл списка объектов
            f.write(str(getid) + "\n")
    elif str(getcommand) == "delete_object":
        pass  # Написать функцию удаления обЪекта из базы, возможно нужно сделать специальную функцию,
        # которая запускается с ПЦН.
    return "Ok"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
