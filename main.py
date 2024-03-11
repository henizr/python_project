class Account:
    def __init__(self, id: int = 1):
        self.id = id
        self.name = None

    def __str__(self):
        return str(self.id)

    def get_id(self):
        return str(self.id)



account = Account()
print(account.get_id())