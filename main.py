import time
from api import WhaleAlertAPI
from processing import Json
from message import Message
from login_data import bot_token, target_id


if __name__ == '__main__':

    api = WhaleAlertAPI()

    while True:
        response = api.make_request()

        # checks if api.make_request returned any value
        if response:
            api.check_status_code(response)
            json = Json(response)
            data = json.get_data()

            if not data:
                print('There is no new transactions.')

            else:
                print("New transactions detected, sending message...")
                message = Message()
                for transaction in data:
                    message.generate(transaction)
                    message.send(bot_token, target_id)

            print("____________________________________________\n")

        else:
            pass

        time.sleep(10)

