class Json:

    def __init__(self, api_response):
        #self.json_file = api_response.json()
        self.json_file = {
  "result": "success",
  "cursor": "2bc7efa-2bc7efa-5c66c095",
  "count": 4,
  "transactions": [
    {
      "blockchain": "ethereum",
      "symbol": "eth",
      "transaction_type": "transfer",
      "hash": "f11c10e44880f0b282fbc40390cd4f50a4d6e6662cc6a3847d57032c79c7e256",
      "from": {
        "address": "3bcf29647e479473dd18dff467a066fcb5a597a0",
        "owner_type": "Unknown"
      },
      "to": {
        "address": "5e032243d507c743b061ef021e2ec7fcc6d3ab89",
        "owner": "bittrex",
        "owner_type": "Exchange"
      },
      "timestamp": 1550237833,
      "amount": 144.24371,
      "amount_usd": 17721.047,
      "transaction_count": 1
    },
    {
      "blockchain": "ethereum",
      "symbol": "eth",
      "transaction_type": "transfer",
      "hash": "76210c5c2cda39b4b2f4685e5e57c342ad7e3b577ba71184792cf76706ec5345",
      "from": {
        "address": "a1ba7454a59ed71c39de58448ca8ff9048e2d0ef",
        "owner_type": "unknown"
      },
      "to": {
        "address": "1423e4e89f9d5913f2fa4f5ecf60a3e2775e4152",
        "owner": "bitfinex",
        "owner_type": "exchange"
      },
      "timestamp": 1550237833,
      "amount": 90.40528,
      "amount_usd": 11106.731,
      "transaction_count": 1
    }
  ]
}
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