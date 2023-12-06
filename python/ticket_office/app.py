import json
from dataclasses import dataclass
import requests
from flask import Flask, request


class TrainData:
    def __init__(self):
        self.session = requests.Session()

    def train(self, id):
        
        return train_data
    
    def bookingReference(self):
        return 

@dataclass
class Seat:
    number: int
    coach: str
    booking_reference: str = ''
@dataclass
class Train:
    id: str
    seats: Seat

    def load(self, train_data, train_id):
        self.id = train_id
        for s in train_data["seats"].values():
            self.seats.append(Seat(s["seat_number"], s["booking_reference"], s["coach"]))

    def getAvailableSeats(self):
        return (s for s in self.seats if s.coach == "A" and not s.booking_reference)

def get_available_seats(train):
    return (
        s
        for s in train["seats"].values()
        if s["coach"] == "A" and not s["booking_reference"]
    )

def create_reservation(seat_count, booking_reference, train: Train):
    available_seats = train.getAvailableSeats()
    to_reserve = []
    for i in range(seat_count):
        to_reserve.append(next(available_seats))
    seat_ids = [f"{s.number}{s.coach}" for s in to_reserve]
    return {
        "train_id": train.id,
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

        session = requests.Session()

        booking_reference = session.get("http://localhost:8082/booking_reference").text

        train_data = session.get(
            f"http://localhost:8081/data_for_train/" + train_id
        ).json()

        train = Train().load(train_data, train_id)

        reservation = create_reservation(seat_count, booking_reference, train)

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
