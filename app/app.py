from flask import Flask, jsonify, request
from flask_cors import CORS
from models.linear_hashing import LinearHashing
from models.extendible_hashing import ExtendibleHashing

app = Flask(__name__)
CORS(app)

linear_hasher = LinearHashing()
extendible_hasher = ExtendibleHashing()


@app.route("/linear/insert", methods=["POST"])
def linear_insert():
    data = request.json
    key = data["key"]
    value = data["value"]
    result = linear_hasher.insert(key, value)
    return jsonify({"inserted": {"key": key, "value": value}, "state": result}), 201


@app.route("/linear/delete", methods=["DELETE"])
def linear_delete():
    data = request.json
    key = data["key"]
    result = linear_hasher.delete(key)
    return (
        jsonify({"message": f"Key {key} deleted successfully.", "state": result}),
        200,
    )


@app.route("/linear/search", methods=["GET"])
def linear_search():
    key = request.args.get("key")
    value = linear_hasher.search(int(key))
    if value is not None:
        return jsonify({"message": value, "state": linear_hasher.get_state()}), 200
    else:
        return (
            jsonify(
                {"message": f"Key {key} not found.", "state": linear_hasher.get_state()}
            ),
            404,
        )


@app.route("/extendible/insert", methods=["POST"])
def extendible_insert():
    data = request.json
    key = data["key"]
    value = data["value"]
    result = extendible_hasher.insert(key, value)
    return jsonify({"inserted": {"key": key, "value": value}, "state": result}), 201


@app.route("/extendible/delete", methods=["DELETE"])
def extendible_delete():
    data = request.json
    key = data["key"]
    result = extendible_hasher.delete(key)
    return (
        jsonify({"message": f"Key {key} deleted successfully.", "state": result}),
        200,
    )


@app.route("/extendible/search", methods=["GET"])
def extendible_search():
    key = request.args.get("key")
    value = extendible_hasher.search(int(key))
    if value is not None:
        return jsonify({"message": value, "state": extendible_hasher.get_state()}), 200
    else:
        return (
            jsonify(
                {
                    "message": f"Key {key} not found.",
                    "state": extendible_hasher.get_state(),
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run(debug=True)
