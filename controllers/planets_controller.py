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
    return render_template('planets/index.html', planets = planets)
