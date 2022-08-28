from flask import Flask

app = Flask(__name__)


@app.route('/<username>')
# def show_user_profile(username):
#     # показать профиль данного пользователя
#     return 'Hello my good friend %s' % username
def show_user_profile(username):
    # показать профиль данного пользователя
    return f'Hello my good friend { username } I love you!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
