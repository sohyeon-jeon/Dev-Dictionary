from flask import Flask,jsonify
import json

app=Flask(__name__)

@app.route("/",methods=["GET"])
def check_server():
    return jsonify({"message": "server check"})

@app.route("/sum", methods=["GET"])
def sum_post_counts():
    with open('data/input/user.json', 'r') as f:
        user_data = json.load(f)
    post_counts=[user['post_count'] for user in user_data]
    return jsonify({"sum": sum(post_counts)})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5678)