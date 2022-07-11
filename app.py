from flask import Flask, render_template
from views import my_view

app = Flask(__name__)
app.register_blueprint(my_view)

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
