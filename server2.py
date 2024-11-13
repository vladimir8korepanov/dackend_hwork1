from flask import Flask, request, render_template

app = Flask(__name__) # Coздание объекта приложения Flask. 

@app.route('/') #Flask использует декораторы @app.route() для сопоставления URL-адресов с функциями, которые обрабатывают запрсоы.
def index():
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST']) #Декоратор который обрабатывает POST запрос
def calculate():
    data = request.get_json() #Получение данных в формате json
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')
    
    if not all([num1, num2, operation]):
        return {'error': 'Missing parameters'}, 400 #Обработка ошибки
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return {'error': 'Invalid numbers'}, 400 #Обработка ошибки когда нельзя привести числа к дробному числу
    
    if operation == 'add': # Конструкция if else для выбора операции над числами
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return {'error': 'Ошибка: Деление на 0'}, 400
        result = num1 / num2 
    else:
        return {'error': 'Ошибка: Недопустимая операция'}, 400
    print(result)
    return {'result': result}, 200

@app.route('/man') # Использую декоратор для связки URL-адреса /man с функцией man
def man():
    name = "Vladimir"
    age = 666
    return render_template('index1.html', name=name, age=age) #Вызываю render_template, чтобы отобразить index1.html с переменными

if __name__ == '__main__': #Конструкция, которая проверяет то как запущено приложение
    app.run(debug=True, port=80) # Запуск приложения Flsck в режиме отладки
    
