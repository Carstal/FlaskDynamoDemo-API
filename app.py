from flask import Flask, jsonify
import dynamo

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return dynamo.GetAll()

@app.route('/students/name/<name>', methods=["GET"])
def getStudentsByName(name):
    return dynamo.SelectBook(name)


if __name__ == '__main__':
    app.run()
