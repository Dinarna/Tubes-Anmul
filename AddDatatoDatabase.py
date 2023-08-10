from datetime import date

import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("absen.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://absen-fea3a-default-rtdb.asia-southeast1.firebasedatabase.app"
})

ref = db.reference(str(date.today()))
data = {
    "10121060":
    {
        "name": "Dinar Nur Aziz",
        "major": "Informatika",
        "starting_year": 2021,
        "total_attendance": 0,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "10121044":
    {
        "name": "Yulia Anggiani",
        "major": "Informatika",
        "starting_year": 2021,
        "total_attendance": 0,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "10121062":
    {
        "name": "Muhamad Reza Pahlevi ",
        "major": "Informatika",
        "starting_year": 2021,
        "total_attendance": 0,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "10121065":
    {
        "name": "Muhammad Hafizh Arrosyidu",
        "major": "Informatika",
        "starting_year": 2021,
        "total_attendance": 0,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    },
    "10121082":
    {
        "name": "Febi Amelia",
        "major": "Informatika",
        "starting_year": 2021,
        "total_attendance": 0,
        "standing": "G",
        "year": 2,
        "last_attendance_time": "2022-12-11 00:54:34"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
