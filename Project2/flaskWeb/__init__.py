from flask import Flask

app = Flask(__name__)


app.config['SECRET_KEY'] = 'COP4813'



from flaskWeb import routes