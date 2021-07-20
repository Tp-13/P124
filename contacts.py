from flask import Flask, app, json, jsonify, request

app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "name": "Tanush P.",
        "number": "+1 (740)602-7535",        
    },
    {
        "id": 2,
        "name": "Swati S.",
        "number": "+1 (732)397-5896",
    },
]
@app.route("/add-data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        }, 400)
    
    task = {
        "id": tasks[-1]["id"] + 1,
        "name": request.json["name"],
        "number": request.json.get("number", ""),
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"Contact added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)