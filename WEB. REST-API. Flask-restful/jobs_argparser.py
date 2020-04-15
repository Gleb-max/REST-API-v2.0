from flask_restful import reqparse
import datetime


parser = reqparse.RequestParser()
parser.add_argument("team_leader", required=True, type=int)
parser.add_argument("job", required=True, type=str)
parser.add_argument("work_size", required=True, type=float)
parser.add_argument("collaborators", required=False, type=str)
parser.add_argument("start_date", required=False, type=datetime.datetime)
parser.add_argument("end_date", required=False, type=datetime.datetime)
parser.add_argument("is_finished", required=False, type=bool)
