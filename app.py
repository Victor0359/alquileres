from flask import Flask

aplication  = Flask("__name__")

@ aplication.route('/')
def index():
    return ' Sería bueno que anduviese'

if __name__ == '__main__':
    aplication.run(debug=True)
