
# import single function from dbhelpers to connect
# execute and close the connection
from dbhelpers import conn_exe_close
# import request, make_response,jsonify from flask
from flask import Flask, make_response
import json

# single function to handle database interactions
# and based on results will send errors
def get_display_results(statement,args_list):
    results = conn_exe_close(statement,args_list)
    # results usuually will be in json format and if it is true 
    # then it wll return the result
    if(type(results) == list):
        # if result is a list but there is no data that client is looking
        # then just a msg will be shown instead of an empty list
        if(len(results) == 0):
            return 'No results matched your search'
        return make_response(json.dumps(results, default=str), 200)
        # if error then probably string will get return 
    elif(type(results) == str):
        return make_response(json.dumps(results, default=str), 400)
        # else just return the result and show the error
    else:
        return make_response(json.dumps(results, default=str) , 500)


# will verifiy end points arguments for presence
# if necessary arguments not sent then remind the user to send
def verify_endpoints_info(sent_data,required_args):
    for data in required_args:
        if(sent_data.get(data) == None):
            return f'The {data} argument is required'