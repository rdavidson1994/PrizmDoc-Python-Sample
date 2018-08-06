import os
import requests

from flask import Flask, request, url_for

method_dict = {'GET':requests.get,
               'POST':requests.post,
               'PUT':requests.put,
               'DELETE':requests.delete,}

app = Flask(__name__)
@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/splash')
def api_articles():
    return 'Splash page goes here?'

@app.route('/pas-service/<arg>', methods=list(method_dict.keys()))
def api_pas(arg):
    new_request = method_dict[request.method]
    header_dict = dict(request.headers)
    header_dict.update({"Accusoft-Secret": "mysecretkey"})
    r = requests.request(method, "http://localhost:3000/"+arg, headers=header_dict, json=request.get_json())
    return r.text

if __name__ == '__main__':
    app.run()