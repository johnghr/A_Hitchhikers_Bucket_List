from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import system_repository

from models.system import System

systems_blueprint = Blueprint("systems", __name__)

@systems_blueprint.route("/systems")
def systems():
    systems = system_repository.select_all()
    return render_template('systems/index.html', systems = systems)

@systems_blueprint.route("/systems/new", methods=['GET'])
def new_system():
    systems = system_repository.select_all()
    return render_template("systems/index.html", systems = systems)

@systems_blueprint.route("/systems", methods=['POST'])
def create_system():
    name = request.form['system']
    system = System(name) 
    system_repository.save(system)
    return redirect('/systems')
