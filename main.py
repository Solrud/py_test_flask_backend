from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from colorama import Fore, Style, init, Back

init(autoreset=True)
app = Flask(__name__)
CORS(app)
logging.basicConfig(filename='app.log', level=logging.INFO, encoding='utf-8')
# logger = logging.getLogger('main_LOGS_info')

users_second_list = [{'id': 0, 'firstName': 'Матвей', 'lastName': 'Ильин', 'email': 'matthew.avid.ng@gmail.com'},
                     {'id': 1, 'firstName': 'Вася', 'lastName': 'Петечкин', 'email': 'V4sY4.proGamer@mail.com'},
                     {'id': 2, 'firstName': 'Игорь', 'lastName': 'Крутой', 'email': 'coolIgor@yandex.ru'},
                     {'id': 3, 'firstName': 'Петр', 'lastName': 'Петрович', 'email': 'manPentr1999@ya.ru'},
                     {'id': 4, 'firstName': 'Коля', 'lastName': 'Коля', 'email': 'kolya@gmail.com'}
                     ]


@app.route('/api/user', methods=['GET'])
def get_user():
    user_data = {
        'name': 'Matveyka',
        'email': 'mathhew@mail.ru'
    }
    return jsonify(user_data)


@app.route('/api/search-user', methods=['POST'])
def get_user_by_name_lastname():
    try:
        request_data = request.get_json()
        first_name = request_data.get('firstName')
        last_name = request_data.get('lastName')

        if not first_name or not last_name:
            app.logger.warning('__WARNING --> some field is empty'
                               ' [checkFIELDS]==>> NAME: [' + first_name + '] AND LAST_NAME: [' + last_name + ']')
            raise ValueError('Имя или фамилия не заполнены')

        for user in users_second_list:
            if first_name == user['firstName'] and last_name == user['lastName']:
                app.logger.info(f"__SUCCESS --> finding user:" + first_name + ' ' + last_name)
                return jsonify(user)

        app.logger.error('__NOT FOUND --> user [CHECK_USER] ==>> NAME: ['
                         + first_name + '] AND LAST_NAME: [' + last_name + ']')
        return jsonify({'message': 'Пользователь не найден'}), 404


    except ValueError as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    app.run()
