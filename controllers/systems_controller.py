from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import system_repository

from models.system import System

systems_blueprint = Blueprint("systems", __name__)

@systems_blueprint.route("/systems")
def systems():
    systems = system_repository.select_all()
    return render_template('systems/index.html', systems = systems)