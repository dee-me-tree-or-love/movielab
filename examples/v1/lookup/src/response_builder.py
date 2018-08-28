from flask import jsonify


class ResponseBuilder:
    @staticmethod
    def build_json_response(data):
        return jsonify(data)
