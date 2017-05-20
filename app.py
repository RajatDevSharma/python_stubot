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
    #find_book = parameters.get("title")
    find_book="data structures"
    #speech="hello"
    books=[u'Discrete Mathematics', u'Algorithms I', u'Programming and Data Structures']

    matches = [x for x in books if re.search(find_book, x, re.M|re.I)]

    #for i in matches:
    #    speech="hello "
            
    speech=i

    

    print("Response:")
    print(speech)

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
