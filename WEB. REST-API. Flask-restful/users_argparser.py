from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument("email", required=True, type=str)
parser.add_argument("password", required=True, type=str)
parser.add_argument("surname", required=True, type=str)
parser.add_argument("name", required=True, type=str)
parser.add_argument("age", required=False, type=int)
parser.add_argument("position", required=False, type=str)
parser.add_argument("speciality", required=False, type=str)
parser.add_argument("address", required=False, type=str)
