import os

from flask import Flask, request, send_from_directory

app = Flask(__name__)

jsons = []

root_folder = '/scoogle'
for _, _, files in os.walk(root_folder + '/json'):
    for j in files:
        jsons.append(j)
        

json_counter = -1
@app.route('/<path:path>')
def send_report(path): 
    return send_from_directory(root_folder, path)

@app.route('/get_json')
def get_json():
    global json_counter 
    json_counter += 1    
    return open(root_folder + '/json/' + jsons[json_counter], 'r')

@app.route('/submit', methods=['POST'])
def recive_tagged_video():
    global json_counter
    result_json = open(root_folder + "/results/" + jsons[json_counter], 'wb')
    result_json.write(str(request.json).replace("'",'"').encode("utf-8"))
    return "200"



@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')


app.run(host='0.0.0.0', port=1583)
