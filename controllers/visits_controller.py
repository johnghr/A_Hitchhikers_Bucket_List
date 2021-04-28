from flask import Flask, render_template, redirect, request, Blueprint

from repositories import visit_repository
from repositories import system_repository
from repositories import planet_repository

from models.visit import Visit
from models.system import System

visits_blueprint = Blueprint("visits", __name__)

# route for list of visits
@visits_blueprint.route("/visits")
def visits():
    visits = visit_repository.select_all()
    planets = planet_repository.select_all()
    return render_template("visits/index.html", visits = visits, planets = planets)

# GET - Returns html form to the browser
@visits_blueprint.route("/visits/new", methods=['GET'])
def new_visits():
    systems = system_repository.select_all()
    planets = planet_repository.select_all()
    return render_template("visits/new.html", systems = systems, planets = planets)

# CREATE - Receives data from form and inputs into db
@visits_blueprint.route("/visits", methods=['POST'])
def create_visit():
    goal = request.form['goal']
    planet_id = request.form['planet_id']
    achieved = request.form['achieved']
    planet = planet_repository.select(planet_id)
    visit = Visit(goal, planet, achieved)
    visit_repository.save(visit)
    return redirect('/visits')

@visits_blueprint.route("/visits/<id>", methods=['GET'])
def show_visit(id):
    visit = visit_repository.select(id)
    return render_template('visits/show.html', visit = visit)

@visits_blueprint.route("/visits/<id>/edit", methods=['GET'])
def edit_visit(id):
    visit = visit_repository.select(id)
    return render_template('visits/edit.html', visit = visit)

@visits_blueprint.route("/visits/<id>", methods=["POST"])
def update(id):
    print("hit edit controller")
    visit = visit_repository.select(id)
    if request.form.get('achieved'):
        visit.achieved = True
    else:
        visit.achieved = False
    visit_repository.update(visit)
    return redirect(f'/visits/{id}')


# @visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
# def delete_planet(id):
#     visit = visit_repository.select(id)
#     visit.planet.name = "None"
#     planet_repository.update(planet)
#     visit_repository.update(visit)
#     return redirect(f'/visits/{id}')

# @visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
# def delete_visit(id):
#     visit_repository.delete(id)
#     return redirect('/visits')


    





