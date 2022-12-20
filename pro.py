from flask import Flask,jsonify, request
app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Doraemon',
        'Contact': u'9446015014', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Shinchan',
        'Contact': u'9446423614', 
        'done': False
    }
]

@app.route("/") 
def hello_world():
     return "Hello!"

@app.route("/get-data") 
def get_task():
     return jsonify({ "data" : list }) 

@app.route("/add-data", methods=["POST"]) 
def add_task():
     if not request.json:
         return jsonify({ "status":"error", "message": "Please provide the data!" },400) 
     task = { 'id': list[-1]['id'] + 1, 'title': request.json['title'], 'description': request.json.get('description', ""), 'done': False } 
     list.append(task) 
     return jsonify({ "status":"success", "message": "Task added succesfully!" })       

if (__name__ == "__main__"):
      app.run(debug=True)       