from app import app
from model.user_model import user_model
from flask import request
obj=user_model()

@app.route("/user/gets")
def user_gets():
    return obj.user_gets()

@app.route("/user/get/<id>")
def user_get(id):
    return obj.user_get(id)

@app.route("/user/add", methods=["POST"])
def user_add():
    return obj.user_add(request.form)

@app.route("/user/update", methods=["PUT"])
def user_update():
    return obj.user_update(request.form)

@app.route("/user/delete/<id>", methods=["DELETE"])
def user_delete(id):
    return obj.user_delete(id)