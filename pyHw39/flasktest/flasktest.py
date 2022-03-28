from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def sol():
    return "Тестовая страница"


@app.route("/task/1")
def sol1():
    return "Решение задачи 1"


@app.route("/task/2")
def sol2():
    return render_template("solution.html")


if __name__ == '__main__':
    app.run(debug=True)




