import time
from api import WhaleAlertAPI
from processing import Json
from message import Message
from login_data import bot_token, target_id, api_key


def main():
    api = WhaleAlertAPI(api_key)

    while True:
        print("____________________________________________\n")
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

        else:
            pass

        time.sleep(30)




if __name__ == '__main__':
    try:
        start_message = Message()
        start_message.content = "Script is now online, looking for new transactions..."
        start_message.send(bot_token, target_id)
        main()

    except KeyboardInterrupt:
        print("Script has been terminated...")

    except:
        print("Unknown Error has occurred")

    finally:
        end_message = Message()
        end_message.content = "Script is currently offline, there will be no alerts until - back online notification"
        end_message.send(bot_token, target_id)
        print("Script has ended")
