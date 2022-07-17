from crypt import methods
from pickle import FALSE
from pydoc import plain
from datetime import datetime
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)


app = Flask(__name__)
CORS(app)
db = firestore.client()


@app.route("/")
def home():
    return "<h1>Server is LIVE.</h1>"


@app.route("/users", methods=["GET"])
def get_user():
    try:
        docs = db.collection("users").stream()
        user_data = {}

        for doc in docs:
            user_data[doc.id] = doc.to_dict()
        user_data["success"] = True
        response = jsonify(user_data)
        response.status_code = 200
        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/questions", methods=["POST"])
def get_questiosn():
    try:
        quiz_id = request.json['quiz_id']
        response = {}
        docs = db.collection(u"quizzes").document(
            quiz_id).collection("questions").stream()

        response['quizQuestions'] = {}
        for doc in docs:
            data = doc.to_dict()
            del data['correctOptionId']
            response['quizQuestions'][doc.id] = data

        doc = db.collection(u"quizzes").document(
            quiz_id).get()

        response['quizDetails'] = doc.to_dict()
        response['success'] = True
        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/newquiz", methods=['POST'])
def add_quiz():
    try:
        data = request.json

        quizzes = db.collection(u'users').document(
            data[u'admin_id']).get(field_paths={'quizzes'}).to_dict().get('quizzes')

        if data['id'] in quizzes.keys():
            raise Exception("Duplicate Quiz")

        quizzes[data['id']] = data['quizDetails']['quizName']
        quizzes = db.collection(u'users').document(
            data[u'admin_id']).update({'quizzes': quizzes})

        db.collection(u"quizzes").document(data["id"]).set(data["quizDetails"])

        quiz_questions = data['quizQuestions']

        for key, val in quiz_questions.items():
            db.collection(u"quizzes").document(data["id"]).collection(
                "questions").document(key).set(val)

        response = {
            "Success": True
        }

        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/check", methods=['POST'])
def match_ans():
    try:
        data = request.json

        doc = db.collection(u"quizzes").document(data["quiz_id"]).get()
        doc_data = doc.to_dict()

        endTime = doc_data['endTime']
        endDate = doc_data['endDate']
        print(endDate+" "+endTime)

        date_time_obj = datetime.strptime(
            endDate+" "+endTime, "%Y-%m-%d %H:%M")
        if datetime.today() > date_time_obj:
            raise Exception("Quiz over")

        question_data = db.collection(u"quizzes").document(data["quiz_id"]).collection("questions").document(
            data[u"question_id"]).get()

        q_data_dict = question_data.to_dict()
        correct_id = q_data_dict['correctOptionId']
        q_score = int(q_data_dict['marks'])
        response = {"success": True}
        response['correct'] = (
            correct_id == data['option_id'])

        doc = db.collection("quizzes").document(data['quiz_id']).collection(
            "players").document(data['player_id']).get()
        if doc.exists:
            print("here")
            doc = doc.to_dict()
            questions = doc['questions']
            questions[data['question_id']] = data['option_id']
            score = doc['score']
            if correct_id == data['option_id']:
                score += q_score
        else:
            questions = {}
            questions[data['question_id']] = data['option_id']
            score = 0
            if correct_id == data['option_id']:
                score += q_score

        db.collection("quizzes").document(data['quiz_id']).collection(
            "players").document(data['player_id']).set({"questions": questions, "score": score})

        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/checkattempt", methods=['POST'])
def check_attempt():
    try:
        body = request.json
        player = db.collection("quizzes").document(body['quiz_id']).collection(
            "players").document(body['player_id']).get()

        if player.exists:
            # print(player.to_dict())
            player_data = player.to_dict()
            if body['question_id'] in player_data['questions'].keys():
                return {"success": True, "duplicate": True, "option_id": player_data['questions'][body['question_id']]}
            else:
                return {"success": True, "duplicate": False}
        else:
            return {"success": True, "duplicate": False}

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/score", methods=['POST'])
def get_score():
    try:
        data = request.json
        player = db.collection("quizzes").document(data['quiz_id']).collection(
            "players").document(data['player_id']).get()

        response = {"success": True}

        if player.exists:
            doc = player.to_dict()
            response["score"] = int(doc["score"])
        else:
            response["score"] = 0

        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/signup", methods=['POST'])
def signup():
    try:
        data = request.json
        user = db.collection("users").document(data['user_id']).get()

        if user.exists == False:
            db.collection("users").document(data['user_id']).set(
                {"email": data['email'], "name": data["name"], "quizzes": {}})
        response = {"success": True}
        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/allquiz", methods=['POST'])
def get_quiz_id():
    try:
        body = request.json
        doc = db.collection("users").document(body['user_id']).get()
        response = doc.to_dict()
        response['success'] = True
        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response


@app.route("/quizinfo", methods=['POST'])
def get_quiz_info_by_id():
    try:
        body = request.json
        response = {}
        docs = db.collection(u"quizzes").document(
            body['quiz_id']).collection("questions").stream()

        response['quizQuestions'] = {}

        for doc in docs:
            data = doc.to_dict()
            response['quizQuestions'][doc.id] = data

        doc = db.collection(u"quizzes").document(body['quiz_id']).get()
        response['quizDetails'] = doc.to_dict()

        docs = db.collection(u"quizzes").document(
            body['quiz_id']).collection("players").stream()
        response['player_info'] = {}
        for doc in docs:
            data = doc.to_dict()
            response['player_info'][doc.id] = data

        response['success'] = True
        return response

    except Exception as e:
        response = {
            "Success": False,
            "Error": str(e)
        }
        return response
