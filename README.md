Проект: Веб-приложение с калькулятором и личной информацией. 
Это простое веб-приложение на Flask, которое включает:
- **API для калькулятора**: позволяет выполнять базовые математические операции (сложение, вычитание, умножение и деление) через POST-запросы.
- **Форма калькулятора** на фронтенде для отправки чисел и операций на сервер.
- **Персонализированная страница**: отображает приветствие с именем и возрастом пользователя.

Структура проекта
- app.py — основной файл серверной части, который реализует Flask-приложение с маршрутизацией и обработкой POST-запросов.
- index.html — шаблон для приветствия пользователя с его именем и возрастом.
- index1.html — шаблон калькулятора, который принимает данные от пользователя и отправляет их на сервер.
- templates/ — папка для шаблонов HTML, в которой будут находиться `index.html` и `index1.html`.
