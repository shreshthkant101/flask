from flask import Flask, jsonify, request

tasks = [{
    "id":1,
    "title":"learn python",
    "description":"You can learn python here, it only takes practice and patience.",
    "done":False
}, 
{
    "id": 2,
    "title":"learn javascript",
    "description":"learn javascript here. it's very easy!",
    "done": False
}
]

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"



@app.route('/add-data', methods=["POST"])
def adddata():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data",

        },400) 
    task = {
        "id":tasks[-1]["id"] + 1,
        "title": request.json["title"],
        "description": request.json.get("description", ""),
        "done": False
    }
    tasks.append(task)

    return jsonify({"status": "successful", "message": "task added successfully"}, 200)

@app.route("/get-data")
def gettask():
    return jsonify({"data":tasks})


if __name__ == "__main__":
    app.run()