import json

import requests
from app import Seat, Train


def test_reserve_seats_from_empty_train():
    seat_count = 4
    fake_train = Train(id="express_2000", seats = [
        Seat(1, coach="A"), 
        Seat(2, coach="A"),
        Seat(3, coach="A"),
        Seat(4, coach="A"),
        ])

    reservation = create_reservation(seat_count, 123456790, fake_train)

    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["1A", "2A", "3A", "4A"]

from app import create_reservation


def test_reserve_four_additional_seats():
    fake_train = Train(id="express_2000", seats = [
        Seat(1, "A", "1"), 
        Seat(2, "A", "1"),
        Seat(3, "A", "1"),
        Seat(4, "A", "1"),
        Seat(5, "A"), 
        Seat(6, "A"),
        Seat(7, "A"),
        Seat(8, "A"),
        ])
    seat_count = 4

    reservation = create_reservation(seat_count, 123456790, fake_train)

    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["5A", "6A", "7A", "8A"]

