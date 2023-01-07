from selenium import webdriver
from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from flask_cors import CORS
from flask import send_from_directory

app = Flask(__name__)
CORS(app)  # эта команда необходима для работы с API из React-приложений

# Функция получения скриншота сайта
@app.route('/get_url_preview/<url>', methods=['GET', 'POST'])
def get_url_preview(url):
    print(url)
    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    driver.get('http://' + url)
    screenshot = driver.save_screenshot('my_screenshot.png')
    driver.quit()
    return send_from_directory(directory='C://Users//User//Desktop//ANC Site WW//src//', path='my_screenshot.png')

###########################
# Запуск службы, не трогать
if __name__ == "__main__":
    app.run()
