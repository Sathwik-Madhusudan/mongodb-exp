from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__, template_folder="templates")


app.config["MONGO_URI"] = "mongodb://myuser:mypassword@mongodb/user-account?authSource=admin"
mongo = PyMongo(app)
users_collection = mongo.db.users

@app.route('/')
def home():
    print('App running on port 5001')
    return render_template("data.html")  # Serves the frontend HTML

@app.route('/test')
def test():
    return "Flask is working!"

@app.route('/update_profile', methods=['POST'])
def update_profile():
    data = request.json
    if not data.get("email"):
        return jsonify({"message": "Email is required"}), 400

    user = users_collection.find_one({"email": data["email"]})

    new_user = {
        "email": data["email"],
        "name": data.get("name", ""),
        "interests": data.get("interests", [])
    }

    if user:
        users_collection.update_one({"email": data["email"]}, {"$set": new_user})
        return jsonify({"message": "Profile updated successfully"})
    else:
        users_collection.insert_one(new_user)
        return jsonify({"message": "New user added successfully"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
