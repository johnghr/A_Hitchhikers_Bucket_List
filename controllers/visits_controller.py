from flask import Flask, render_template, redirect, request
from flask import Blueprint

from repositories import visit_repository
from repositories import system_repository

from models.visit import visit