class JsonHandler:

    def __init__(self, response):
        self.json_file = response.json()
        print("Response from API:\n", self.json_file)

    def get_data(self):
        if self.__new_transactions_exist():
            return self.__simplify_json(self.json_file)
        else:
            return []

    # Checks if there are any transactions in json file
    def __new_transactions_exist(self):
        if self.json_file['count'] == 0:
            return False
        else:
            return True

    # TODO make use of timestamp or delete it
    def __simplify_json(self, json_file):
        outcome = []
        for transaction in json_file["transactions"]:
            simplified_transaction = {"symbol": "", "from": "", "to": "", "amount": 0, "amount_usd": 0}

            # This lines checks if key "owner" exists and returns its value, else it returns "Unknown Wallet"
            simplified_transaction["from"] = transaction["from"].get("owner", "Unknown Wallet")
            simplified_transaction["to"] = transaction["to"].get("owner", "Unknown Wallet")
            simplified_transaction["amount"] = transaction["amount"]
            simplified_transaction["amount_usd"] = transaction["amount_usd"]
            outcome.append(simplified_transaction)

        print("Simplified json:\n", outcome)

        return outcome
