#!/usr/bin/env python

import urllib
import json
import os
import re

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "search.book.title":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    find_book = parameters.get("title")

    speech="hello"
    books=[u'Discrete Mathematics', u'Algorithms I', u'Programming and Data Structures', u'Software Engineering', u'Switching Circuits and Logic Design', u'Formal Languages and Automata Theory', u'Operating Systems', u'Compilers', u'Foundations of Computing', u'Computer Organization and Architecture', u'Theory of Computation', u'Algorithms \u2013 II', u'Computer-Networks', u'Symbolic Logic and Automated Reasoning', u'Principles of Programming Languages', u'Symbolic Logic and Automated Reasoning', u'Artificial Intelligence', u'Electronic Design Automation', u'Image Processing', u'Applied Graph Theory', u'Computational Geometry', u'Computational Complexity', u'Advanced Computer Architecture', u'VLSI System Design', u'Multimedia Applications', u'Microprocessors and Microcontrollers', u'Digital System Testing and Testable Design', u'Database Management Systems', u'Distributed Systems', u'High Performance Computer Architecture', u'Logic for Computer Science', u'Database Engineering', u'Embedded Systems', u'Testing and Verification of Circuits', u'Cryptography and Network Security', u'Advances in Compiler Construction', u'Real Time Systems', u'Advanced Graph Theory', u'Theory of Programming Languages', u'Machine Learning', u'Low Power Circuits and Systems', u'Speech and Natural Language Processing', u'Object Oriented Systems', u'Formal Systems', u'Multimedia Systems', u'Advances in Digital and Mixed Signal Testing', u'Complex Networks', u'Information Retrieval', u'Information Theory and Coding', u'Error Control Coding', u'Fundamentals of information theory', u'Linear networking theory', u'linear and nonlinear circuits', u'network theory', u'Understanding UMAT radio networing modelling', u'ies gates psus networking theory', u'networking coding thoery', u'Building scalable networking servies', u'theories of communication networks', u'Silicon VLSI Technology', u'The Science and engineering of microelectronic fabrication', u'VLSI Technology', u'Technologies for VLSI packages', u'VLSI ceramic research and development', u'low power phase locked loop with multiple', u'VLSI Technology: fundamentals and Application', u'VLSI signal processing technologies', u'Discrete - time signal processing', u'Digital Signal processing', u'Theory and applications of digital signal processing', u'introduction of digital signal processing', u'digital signal processing: fundamentals and applications', u'digital signal processing: principals, algorithms', u"Schaum's outline of digital signal processing", u'digital signal processing techniques and applications', u'Introduction of computer science', u'Computer science question books', u'lectures notes in computer science', u'Graded problems in computer science', u'Algebra for computer science', u'Advance computer science', u'Computer science with C#', u'Probality with R: introduction with computer science', u'Century of electical engineering and computer scienceat MIT', u'Computer Science and scientific scoputing', u'Discrete structure of computer science', u'mathematics for computer science', u'Big data for dummies']
'''
    matches = [x for x in books if re.search( find_book, x, re.M|re.I)]

    for i in matches:
        speech=speech+i+","




    print("Response:")
    print(speech)
'''
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "python_stubot"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

app.run(debug=True, port=port, host='0.0.0.0')
