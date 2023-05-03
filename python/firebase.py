import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class CloudData:
    def __init__(self, reference):
        cred_obj = credentials.Certificate(
            "accident-detection-c160e-firebase-adminsdk-w3jro-8c4563d818.json"
        )

        self.default_app = firebase_admin.initialize_app(
            cred_obj,
            {"databaseURL": "https://accident-detection-c160e-default-rtdb.asia-southeast1.firebasedatabase.app/"},
        )
        self.ref = db.reference(reference)

    def upload(self, isSleeping):
        data = {
            "devices": {
                "LxjBZjUk76ZAFhCijKcXSERoHvX2":{
                    "reading2": {
                        "isSleeping": isSleeping,
                    }
                }
            }
        }
        self.ref.set(data)


# import json
# with open("book_info.json", "r") as f:
# file_contents = json.load(f
