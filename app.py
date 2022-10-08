# import two functions related to api interaction with stored procedures
# get display results will run the stored procedures and bring back the json results
#verify endpoints info will check the existence of arguments sent
from apihelpers import get_display_results, verify_endpoints_info
# import inbuilt libraries
from flask import Flask, request, make_response
# import json
import json

app = Flask(__name__)

# get request to return all the philosophers in the data base
@app.get('/api/philosopher')
def all_philosophers():
    # executing the below function to get results
    results_json = get_display_results('call all_philosophers()',[])
    return results_json

# endpoint for post request
# will create a new philospher given the 5 different arguments in a json format
# invalid variable will store the data from the function and if not none then everything is working
# then after verify the existence of all the arguments it will proceed with further request
@app.post('/api/philosopher')
def add_philosopher():
    invalid = verify_endpoints_info(request.json, ['name','bio','date_of_birth','date_of_death','image_url'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)
    results_json = get_display_results('call add_philosopher(?,?,?,?,?)',
    [request.json.get('name'),request.json.get('bio'),request.json.get('date_of_birth'),request.json.get('date_of_death'),request.json.get('image_url')])
    return results_json

# get request for getting all the quotes for one particular philosopher
# it will seek for an id of a philosopher and return the results in json
@app.get('/api/quote')
def philosopher_quotes_history():
    invalid = verify_endpoints_info(request.args,['id'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)
    results_json = get_display_results('call philosopher_quotes_history(?)',[request.args.get('id')])
    return results_json

# post request to insert the new post specific for the philospher
# given the id of a philosopher
@app.post('/api/quote')
def insert_quote_content():
    invalid = verify_endpoints_info(request.json,['id', 'content'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str), 400)
    results_json = get_display_results('call insert_quote_content(?,?)',
    [request.json.get('id'),request.json.get('content')])
    return results_json


app.run(debug=True)
