
from apihelpers import get_display_results, verify_endpoints_info
from flask import Flask, request, make_response
import json

app = Flask(__name__)

@app.get('/api/philosopher')
def all_philosophers():
    results_json = get_display_results('call all_philosophers()',[])
    return results_json

@app.post('/api/philosopher')
def add_philosopher():
    invalid = verify_endpoints_info(request.json, ['name','bio','date_of_birth','date_of_death','image_url'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)
    results_json = get_display_results('call add_philosopher(?,?,?,?,?)',
    [request.json.get('name'),request.json.get('bio'),request.json.get('date_of_birth'),request.json.get('date_of_death'),request.json.get('image_url')])
    return results_json

@app.get('/api/quote')
def philosopher_quotes_history():
    invalid = verify_endpoints_info(request.args,['id'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)
    results_json = get_display_results('call philosopher_quotes_history(?)',[request.args.get('id')])
    return results_json

@app.post('/api/quote')
def insert_quote_content():
    invalid = verify_endpoints_info(request.json,['id', 'content'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)
    results_json = get_display_results('call insert_quote_content(?,?)',
    [request.json.get('id'),request.json.get('content')])
    return results_json


app.run(debug=True)
