from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import planet_repository
from repositories import system_repository

from models.planet import Planet
from models.system import System

planets_blueprint = Blueprint("planets", __name__)

@planets_blueprint.route("/planets")
def planets():
    systems = system_repository.select_all()
    planets = planet_repository.select_all()
    return render_template('planets/index.html', planets = planets, systems = systems)

@planets_blueprint.route("/planets", methods=['GET'])
def list_planets():
    systems = system_repository.select_all()
    planets = planet_repository.select_all()
    return render_template('planets/index.html', systems = systems, planets = planets)

@planets_blueprint.route("/planets", methods=['POST'])
def create_planet():
    system_name = request.form
    system_id = request.form['system_id']
    system = system_repository.select(system_id)
    name = request.form['planet']
    planet = Planet(name, system) 
    planet_repository.save(planet)
    return redirect('/planets')

@planets_blueprint.route("/planets/<id>/delete", methods=['POST'])
def delete_planet(id):
    planet_repository.delete(id)
    return redirect('/planets')


