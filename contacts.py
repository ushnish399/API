from flask import Flask, jsonify, request
app=Flask(__name__)
tasks=[
    {
        'id':1, 
        'Contact':u"7867543424",
        'Name': u"Raju Sarkar",
        'done':False
    },
    {
        'id':2,
        'Contact':u"6754354211",
        'Name':u"Bindi Umami",
        'done':False
    }
]
@app.route("/")
def HELLOWORLD():
    return "HELLO WORLD"
@app.route('/get-data')
def gettask():
    return jsonify({
        'data':tasks
    })
@app.route('/add-data', methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            'status':"ERROR!",
            'message':"PLEASE PROVIDE THE DATA IN JSON FORMAT"
        }, 200)
    task={
        'id':tasks[-1]['id']+1,
        'Contact':request.json['Contact'],
        'Name':request.json.get('Name', ''),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        'status':'succes',
        'message':"TASK ADDED SUCCESFULY"
    })
if(__name__=="__main__"):
    app.run(debug=True)