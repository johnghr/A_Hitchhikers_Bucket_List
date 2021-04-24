from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import visit_repository
from repositories import system_repository

from models.visit import Visit
from models.system import System

visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def visits():
    visits = visit_repository.select_all()
    return render_template("visits/index.html", visits = visits)

@visits_blueprint.route("/visits/new", methods=['GET'])
def new_visit():
    systems = system_repository.select_all()
    return render_template("visits/new.html", all_systems = systems)

@visits_blueprint.route("/tasks", methods=['POST'])
def create_visit():
    goal = request.form['goal']
    system_name = request.form['system']
    achieved = request.form['achieved']
    system = System(system_name)
    visit = Visit(goal, system, achieved, id)
    visit_repository.save(visit)
    return redirect('/visits')


