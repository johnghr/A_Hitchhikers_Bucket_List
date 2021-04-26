from flask import Flask, render_template

from controllers.visits_controller import visits_blueprint
from controllers.systems_controller import systems_blueprint
from controllers.planets_controller import planets_blueprint


app = Flask(__name__)

app.register_blueprint(visits_blueprint)
app.register_blueprint(systems_blueprint)
app.register_blueprint(planets_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
