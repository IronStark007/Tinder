from fastapi import APIRouter, status

from app.schemas import CreateSchema, LoginSchema, ResponseSchema
from app.service.db_handler import create_data, create_user, user_login


router = APIRouter(tags=["User Account"])

# creating new user
@router.post('/sign_up',response_model=ResponseSchema,status_code=status.HTTP_200_OK)
def sign_up(data: CreateSchema):
    return create_user(data)

# login with email
@router.post('/login',response_model=ResponseSchema,status_code=status.HTTP_200_OK)
def login(data: LoginSchema):
    return user_login(data)

# add user data
@router.post('/add_user_data')
def add_user_data(data):
    return create_data(data)

# @api.route('/getuserdata/<user_id>')
# class GetUserData(MethodView):
    @api.response(status_code=200, schema=AddUserDataSchema)
    def get(self, user_id):
        store = database()
        data = store.collection("Users").document(user_id).get().to_dict()
        return data
