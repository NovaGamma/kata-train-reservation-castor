import json

import requests
from flask import Flask, request

class TrainData():
    def __init__(self):
        self.session = requests.Session()

    def train(self, id):
        train_data = self.session.get(
            f"http://localhost:8081/data_for_train/" + id
        ).json()
        return train_data
    
    def bookingReference(self):
        return self.session.get("http://localhost:8082/booking_reference").text

def get_available_seats(train):
    return (
        s
        for s in train["seats"].values()
        if s["coach"] == "A" and not s["booking_reference"]
    )

def create_reservation(seat_count, train_id, booking_reference, train):
    available_seats = get_available_seats(train)
    to_reserve = []
    for i in range(seat_count):
        to_reserve.append(next(available_seats))
    seat_ids = [s["seat_number"] + s["coach"] for s in to_reserve]
    return {
        "train_id": train_id,
        "booking_reference": booking_reference,
        "seats": seat_ids,
    }

def create_app():
    app = Flask("ticket_office")

    @app.post("/reserve")
    def reserve():
        payload = request.json
        seat_count = payload["count"]
        train_id = payload["train_id"]

        train_data = TrainData()

        booking_reference = train_data.bookingReference()
        train = train_data.train(train_id)

        reservation = create_reservation(seat_count, train_id, booking_reference, train)

        reservation_payload = {
            "train_id": reservation["train_id"],
            "seats": reservation["seats"],
            "booking_reference": reservation["booking_reference"],
        }

        response = requests.post(
            "http://localhost:8081/reserve",
            json=reservation_payload,
        )
        assert response.status_code == 200, response.text
        response = response.json()

        return json.dumps(reservation)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8083)
