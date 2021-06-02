from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

launch_put_args = reqparse.RequestParser()
launch_put_args.add_argument('vehicle_name', type=str, help='Name Of Launch Vehicle is REQUIRED', required=True)
launch_put_args.add_argument('launch_date', type=str, help='Date of Vehicle Launch is REQUIRED', required=True)
launch_put_args.add_argument('mission_status', type=str, help='Status of Mission is REQUIRED', required=True)

launches = {
    
}

def abort_check(launch_1d, status):
    if status == 404:
        if launch_1d not in launches:
            abort(404, message="Launch ID not found :(")
    elif status == 406:
        if launch_1d in launches:
            abort(406, message="Launch ID already exists :(")



class Krypton(Resource):
    
    def get(self, launch_id):
        abort_check(launch_id, 404)
        return launches[launch_id]
    
    def post(self, launch_id):
        abort_check(launch_id, 404)
        return launches[launch_id]

    def put(self, launch_id):
        abort_check(launch_id, 406)
        args = launch_put_args.parse_args()
        launches[launch_id] = args
        return launches[launch_id], 201
    
    def delete(self, launch_id):
        abort_check(launch_id, 404)
        del launches[launch_id]
        return '', 204


api.add_resource(Krypton, '/krypton/launches/<int:launch_id>')

if __name__ == '__main__':
    app.run(debug=True)