#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify

from operat import Operator
from constants import PORT

operator = Operator()
app = Flask(__name__)


@app.route('/askmeanything/')
def askMe():
    question = request.args.get('q', '')  # parse question from url
    botAnswer = operator.getAnswer(question)
    response = {'response': None}
    response['response'] = botAnswer
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
