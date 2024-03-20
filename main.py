from pathlib import Path
BASE_PATH = str(Path(__file__).resolve().parent / Path("img"))



print(BASE_PATH)

class Account:
    def __init__(self, id: int = 1):
        self.id = id
        self.name = None

    def __str__(self):
        return self.id

    def get_id(self):
        return str(self.id)



# account = Account()
# print(account.get_id())