# import traceback
# from flask import Flask, jsonify


# from app.routers import common, user_account


# def create_app():
#     app = Flask(__name__)

#     app.config.from_pyfile('config.py')

#     app.register_blueprint(common.api,url_prefix=app.config.get('URL_PREFIX'))
#     app.register_blueprint(user_account.api,url_prefix=app.config.get('URL_PREFIX'))

#     app.logger.info("Starting APP")

#     @app.errorhandler(Exception)
#     def handle_exception(error):
#         d = {
#             "type": type(error).__name__,
#             "message": str(error),
#             "traceback": traceback.format_exc(),
#         }
#         http_code = 500
#         result = {"errors": [d]}
#         response = jsonify(result)
#         response.status_code = http_code
#         return response
#     return app

# # # getting feed based on city
# # @app.route('/feed', methods=['POST'])
# # def feed():
# #     data = request.get_json(force=True)
# #     uid = data.get('userid')
# #     city = data.get('city')
# #     gender = data.get('gender')
# #     docs = store.collection('Users').where("gender", "==", gender).stream()
# #     swipes = store.collection('Swipes').stream()
# #     visited = []
# #     for swipe in swipes:
# #         if (swipe.to_dict().get('uid_a') == uid):
# #             visited.append(swipe.to_dict().get('uid_b'))
# #     result = {}
# #     # if person is not shown in feed
# #     for doc in docs:
# #         # if he/she is a new user
# #         if (len(visited) == 0) and (doc.to_dict().get('location').get('city') == city):
# #             result[doc.id] = doc.to_dict()
# #         if ((len(visited) != 0) and (doc.id not in visited)) and (doc.to_dict().get('location').get('city') == city):
# #             result[doc.id] = doc.to_dict()
# #     return jsonify(result)
# #     # return jsonify({"Name":result.get('name'),"Visited":visited,"Image":result.get('image'),"Description":result.get('desp'),"Passion":result.get('passion')})

# # # for swipe


# # # @app.route('/swipe', methods=['POST'])
# # # def swipe():
# #     data = request.get_json(force=True)
# #     userid_A = data['uid_a']
# #     userid_B = data['uid_b']
# #     is_right = data['is_right']
# #     is_left = data['is_left']
# #     result = {}
# #     result['uid_a'] = userid_A
# #     result['uid_b'] = userid_B
# #     result['is_right'] = is_right
# #     result['is_left'] = is_left
# #     store.collection('Swipes').document(userid_A).set(result)
# #     return jsonify({"Response": 200})

# # # # getting match


# # # @app.route('/match', methods=['POST'])
# # # def match():
# #     data = request.get_json(force=True)
# #     userid_A = data['uid_a']
# #     userid_B = data['uid_b']
# #     result = {}
# #     docs = store.collection('Swipes').stream()
# #     for doc in docs:
# #         if (userid_A in doc.id or userid_B in doc.id) and (doc.to_dict().get('is_right')):
# #             result['uid_a'] = userid_A
# #             result['uid_b'] = userid_B
# #             result['Matched'] = True
# #             store.collection('Matched_Yes').document(userid_B).set(result)
# #             message = 'Congratulations !!! you both matched'
# #             return jsonify({'Message': message, "Result": result, "Response": 200})

# #         else:
# #             result['uid_a'] = userid_A
# #             result['uid_b'] = userid_B
# #             result['Matched'] = False
# #             store.collection('Matched_Yes').document(userid_B).set(result)
# #             message = ""
# #             return jsonify({'Message': message, "Result": result, "Response": 200})
