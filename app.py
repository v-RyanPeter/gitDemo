from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "Hi"

@app.get("/abc")
def index():
    return "Hiabc"

if __name__ == '__main__':
    app.run(debug=True)


'''
CI

'''