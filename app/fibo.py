from flask import Flask
import redis
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
r_server=redis.StrictRedis(host='redis',port=6379,charset="utf-8", decode_responses=True)

def get_fibo(number):
    if (number == 0) or (number == 1):
        return number
    return get_fibo(number-1) + get_fibo(number-2)

@app.route('/', methods=['GET'])
def hello():
    return 'Привет! Для получения значения k-ого числа Фибоначчи добавь цифру в адресную строку после слэша. Например, 127.0.0.1:8081/1'

@app.route('/<k>', methods=['GET'])
def fibo_number(k):
    number = int(k)
    q = r_server.get(number)
    if q:
        return '{} число Фибонначи = {} - (число взято из кэша)'.format(number, q)
    else:
        result = get_fibo(number)
        r_server.set(number,result)
    return '{} число Фибонначи = {}'.format(number,result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

