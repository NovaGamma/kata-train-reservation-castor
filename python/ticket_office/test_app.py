import json

import requests


def test_reserve_seats_from_empty_train():
    train_id = "express_2000"
    seat_count = 4
    fake_train = { "seats" : {"1A": { "coach" : "A", "seat_number" : "1", "booking_reference" : ""},
                              "2A": { "coach" : "A", "seat_number" : "2", "booking_reference" : ""}, 
                              "3A": { "coach" : "A", "seat_number" : "3", "booking_reference" : ""},
                              "4A": { "coach" : "A", "seat_number" : "4", "booking_reference" : ""},
                              "1B": { "coach" : "B", "seat_number" : "1", "booking_reference" : ""},
                              "2B": { "coach" : "B", "seat_number" : "2", "booking_reference" : ""}, 
                              "3B": { "coach" : "B", "seat_number" : "3", "booking_reference" : ""},
                              "4B": { "coach" : "B", "seat_number" : "4", "booking_reference" : ""},
                              "5B": { "coach" : "B", "seat_number" : "5", "booking_reference" : ""},
                              "6B": { "coach" : "B", "seat_number" : "6", "booking_reference" : ""},
                              "7B": { "coach" : "B", "seat_number" : "7", "booking_reference" : ""},
                              "8B": { "coach" : "B", "seat_number" : "8", "booking_reference" : ""},
                              "1C": { "coach" : "C", "seat_number" : "1", "booking_reference" : ""},
                              "2C": { "coach" : "C", "seat_number" : "2", "booking_reference" : ""},
                              "3C": { "coach" : "C", "seat_number" : "3", "booking_reference" : ""},
                              "4C": { "coach" : "C", "seat_number" : "4", "booking_reference" : ""}
                             }
                  }

    reservation = create_reservation(seat_count, train_id, 123456790, fake_train)


    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["1A", "2A", "3A", "4A"]

from app import create_reservation, get_available_seats

def test_available_seats():
    fake_train = { "seats" : {"1A": { "coach" : "A", "seat_number" : "1", "booking_reference" : ""},
                              "2A": { "coach" : "A", "seat_number" : "2", "booking_reference" : ""}, 
                              "3A": { "coach" : "A", "seat_number" : "3", "booking_reference" : ""},
                              "4A": { "coach" : "A", "seat_number" : "4", "booking_reference" : ""},
                              "1B": { "coach" : "B", "seat_number" : "1", "booking_reference" : ""},
                              "2B": { "coach" : "B", "seat_number" : "2", "booking_reference" : ""}, 
                              "3B": { "coach" : "B", "seat_number" : "3", "booking_reference" : ""},
                              "4B": { "coach" : "B", "seat_number" : "4", "booking_reference" : ""},
                              "5B": { "coach" : "B", "seat_number" : "5", "booking_reference" : ""},
                              "6B": { "coach" : "B", "seat_number" : "6", "booking_reference" : ""},
                              "7B": { "coach" : "B", "seat_number" : "7", "booking_reference" : ""},
                              "8B": { "coach" : "B", "seat_number" : "8", "booking_reference" : ""},
                              "1C": { "coach" : "C", "seat_number" : "1", "booking_reference" : ""},
                              "2C": { "coach" : "C", "seat_number" : "2", "booking_reference" : ""},
                              "3C": { "coach" : "C", "seat_number" : "3", "booking_reference" : ""},
                              "4C": { "coach" : "C", "seat_number" : "4", "booking_reference" : ""}
                             }
                  }
    available_seats = get_available_seats(fake_train)
    assert [s for s in available_seats] == [{ "coach" : "A", "seat_number" : "1", "booking_reference" : ""},
                              { "coach" : "A", "seat_number" : "2", "booking_reference" : ""}, 
                              { "coach" : "A", "seat_number" : "3", "booking_reference" : ""},
                              { "coach" : "A", "seat_number" : "4", "booking_reference" : ""}]

def test_reserve_four_additional_seats():
    fake_train = { "seats" : {"1A": { "coach" : "A", "seat_number" : "1", "booking_reference" : "123456789"},
                              "2A": { "coach" : "A", "seat_number" : "2", "booking_reference" : "123456789"}, 
                              "3A": { "coach" : "A", "seat_number" : "3", "booking_reference" : "123456789"},
                              "4A": { "coach" : "A", "seat_number" : "4", "booking_reference" : "123456789"},
                              "1B": { "coach" : "B", "seat_number" : "1", "booking_reference" : ""},
                              "2B": { "coach" : "B", "seat_number" : "2", "booking_reference" : ""}, 
                              "3B": { "coach" : "B", "seat_number" : "3", "booking_reference" : ""},
                              "4B": { "coach" : "B", "seat_number" : "4", "booking_reference" : ""},
                              "5B": { "coach" : "B", "seat_number" : "5", "booking_reference" : ""},
                              "6B": { "coach" : "B", "seat_number" : "6", "booking_reference" : ""},
                              "7B": { "coach" : "B", "seat_number" : "7", "booking_reference" : ""},
                              "8B": { "coach" : "B", "seat_number" : "8", "booking_reference" : ""},
                              "1C": { "coach" : "C", "seat_number" : "1", "booking_reference" : ""},
                              "2C": { "coach" : "C", "seat_number" : "2", "booking_reference" : ""},
                              "3C": { "coach" : "C", "seat_number" : "3", "booking_reference" : ""},
                              "4C": { "coach" : "C", "seat_number" : "4", "booking_reference" : ""}
                             }
                  }
    train_id = "express_2000"
    seat_count = 4

    reservation = create_reservation(seat_count, train_id, 123456790, fake_train)

    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["5A", "6A", "7A", "8A"]
   
