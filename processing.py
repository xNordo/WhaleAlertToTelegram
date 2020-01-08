class Json:

    def __init__(self, api_response):
        self.json_file = api_response.json()

    def get_data(self):
        if self.__new_transactions_exist():
            return self.__simplify_json()
        else:
            return []

    # Checks if there are any transactions in json file
    def __new_transactions_exist(self):
        if self.json_file['count'] == 0:
            return False
        else:
            return True

    def __simplify_json(self):
        outcome = []

        for transaction in self.json_file["transactions"]:
            simplified_transaction = {"symbol": '', "from": "", "to": "", "timestamp": 0, "amount": 0, "amount_usd": 0}

            simplified_transaction["symbol"] = transaction["symbol"]

            # This lines checks if key "owner" exists and returns its value, else it returns "Unknown Wallet"
            simplified_transaction["from"] = transaction["from"].get("owner", "Unknown Wallet")
            simplified_transaction["to"] = transaction["to"].get("owner", "Unknown Wallet")

            simplified_transaction["timestamp"] = transaction["timestamp"]
            simplified_transaction["amount"] = transaction["amount"]
            simplified_transaction["amount_usd"] = transaction["amount_usd"]
            outcome.append(simplified_transaction)

        return outcome