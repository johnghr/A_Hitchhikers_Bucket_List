from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import visit_repository
from repositories import system_repository

from models.visit import Visit
from models.system import System

visits_blueprint = Blueprint("visits", __name__)

# route for list of visits
@visits_blueprint.route("/visits")
def visits():
    visits = visit_repository.select_all()
    return render_template("visits/index.html", visits = visits)

# GET - Returns html form to the browser
@visits_blueprint.route("/visits/new", methods=['GET'])
def new_visit():
    systems = system_repository.select_all()
    return render_template("visits/new.html", all_systems = systems)

# CREATE - Receives data from form and inputs into
@visits_blueprint.route("/visits", methods=['POST'])
def create_visit():
    goal = request.form['goal']
    system_id = request.form['system_id']
    achieved = request.form['achieved']
    system = system_repository.select(system_id)
    visit = Visit(goal, system, achieved)
    visit_repository.save(visit)
    return redirect('/visits')

@visits_blueprint.route("/visits/<id>", methods=['GET'])
def show_task(id):
    visit = visit_repository.select(id)
    return render_template('visits/show.html', visit = visit)


