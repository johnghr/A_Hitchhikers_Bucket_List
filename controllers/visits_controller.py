from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import visit_repository
from repositories import system_repository

from models.visit import Visit

visits_blueprint = Blueprint("visits", __name__)

@visits_blueprint.route("/visits")
def visits():
    
    visit = visit_repository.select_all()
    return render_template("visits/index.html", visit=visit)

@visits_blueprint.route("/visits/new", methods['GET'])