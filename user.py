import json


class User:
    @staticmethod
    def add_users_to_json(Vorname, Nachname):
        file = "user_data.json"

        # load data
        with open(file, "r") as f:
            users = json.load(f)

        # adds a unique ID to every entry
        if len(users) == 0:
            id = 1
        else:
            id = users[-1]["ID"] + 1

        new_user = {"ID": id, "Vorname": Vorname, "Nachname": Nachname}

        # add user
        users.append(new_user)

        # safe user in Json
        with open(file, "w") as f:
            json.dump(users, f, indent=4)

    def __init__(self):
        pass
