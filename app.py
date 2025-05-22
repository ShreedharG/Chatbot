from flask import Flask, render_template, request, jsonify
import db_helper
import function as fnc
from chatbot import predict_class, get_response
import json
import sys

app = Flask(__name__)
intents = json.loads(open('intents.json').read())

@app.route("/")
def home():
    welcome_msg = fnc.read_welcome_message()
    return render_template("index.html", welcome_msg=welcome_msg)


@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message")
    intents_list = predict_class(user_message)
    
    if intents_list:
        tag, response = get_response(intents_list, intents)
        if tag == "order_status":
            return jsonify({"trigger_order_status_popup": True})       
        elif tag == "place_order":
            return jsonify({"trigger_order_popup": True})
    else:
        response = "I'm sorry, I didn't understand that. Can you please rephrase?"
    
    return jsonify({"reply": response})


@app.route("/place_order", methods=["POST"])
def place_order():
    data = request.json
    item_index = int(data["item"])
    quantity = int(data["quantity"])

    if item_index not in db_helper.items_dict or not (1 <= quantity <= 4):
        return jsonify({"error": "Invalid item or quantity"}), 400

    order_id = fnc.generator.generate()
    item = db_helper.items_dict[item_index]['item']
    price_per_unit = db_helper.items_dict[item_index]['price']
    total_price = price_per_unit * quantity

    db_helper.insert_order(order_id, item, quantity, total_price)

    return jsonify({
        "order_id": order_id,
        "item": item,
        "quantity": quantity,
        "price": total_price
    })

@app.route("/order_status", methods=["POST"])
def order_status():
    data = request.json
    order_ID = int(data["orderID"])
    order_status = db_helper.fetch_order_status(order_ID)
    if order_status:
        return jsonify({
            "order_ID": order_status['order_ID'],
            "item": order_status['Item'],
            "quantity": order_status['Quantity'],
            "price": order_status['Price'],
            "status": order_status['status']
        })
    else:
        return jsonify({"error": "Invalid Order ID"}), 400

@app.route('/menu')
def get_menu():
    db_helper.fetch_menu() 
    return jsonify(db_helper.items_dict)

if __name__ == "__main__":
    app.run(debug=True)
