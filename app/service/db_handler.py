from app.service import firebase
from app.exception import EmailOrPasswordError, UserAlreadyExistsError

def create_user(data: dict):
    try:
        firebase.auth.create_user_with_email_and_password(
            email=data.email,
            password=data.password)
        return dict(message="user succesfully created")
    except:
        raise UserAlreadyExistsError()

def user_login(data: dict):
    try:
        firebase.auth.sign_in_with_email_and_password(
            email=data.email,
            password=data.password)
        return dict(message="user succesfully login")
    except:
        raise EmailOrPasswordError()

def create_data(data: dict):
    # complete this method by seeing the fastapi youtube tutorial https://www.youtube.com/watch?v=s-Ga8c3toVY&t=1049s
    pass
        # store = firebase.database.
        # user_id = body.pop("user_id")
        # try:
        #     store.collection("Users").document(user_id).set(body)
        #     return jsonify({"message": "succesfully update user data"})
        # except:
        #     return jsonify({"message": "Some error occured while adding user data"})

