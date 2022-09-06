from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/<username>')
# def show_user_profile(username):
#     return 'Hello my good friend %s' % username
def show_user_name(username):
    return f'Hello my good friend {username} I love you!'


# @app.route("/data", methods=['GET', ])
# def setinfo():
#     # Получить значение параметра id во входящем URL http://localhost:5000/data?id=666&data=123456
#     sendid = request.args.get('id')
#     getdata = request.args.get('data')
#     with open("data.txt", "w") as f:
#         f.write(getdata)
#     return "Get info id is " + str(sendid)

@app.route("/data", methods=['GET', ])
def setinfo():
    # Получить значение параметра id во входящем URL http://localhost:5000/data?id=666&data=["ander", "bolder", "xyeldeer", "zalupolder"]
    sendid = request.args.get('id')
    getdata = request.args.get('data')

    with open("data.txt", "w") as f:
        if sendid is None:
            f.write("None," + "\n")
            f.write(getdata)
        else:
            f.write(sendid + "\n")
            f.write(getdata)
    return "Get info id is " + str(sendid) + " Get info getdata is " + str(getdata)


@app.route("/data1", methods=['GET', ])
def getinfo():
    with open("data.txt", 'r') as f:
        a = f.read()  # .split('\n')
    return str(a)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
