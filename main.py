import time
from api import WhaleAlertAPI, time_step
from processing import JsonHandler
from message import Message
from login_data import bot_token, target_id, api_key
from session import PidFile


# TODO add emoji to start-stop notification
def main():
    api = WhaleAlertAPI(api_key)
    last_cursor = None
    while True:
        print("____________________________________________\n")
        response = api.make_request()
        json_handler = JsonHandler(response)

        # checks if api.make_request returned any value
        if response:
            api.check_status_code(response)
            data = json_handler.get_data()

            if not data:
                print('There is no new transactions.')

            else:
                print("New transactions detected, sending message...")
                message = Message()
                for transaction in data:
                    message_content = message.generate(transaction)
                    message.send(message_content, bot_token, target_id)

        else:
            pass

        # time_step is defined in api.py.
        # It's required to do it this way in order to sync time.sleep and WhaleAlertApi.__get_time()
        time.sleep(time_step)


if __name__ == '__main__':
    pid_file = PidFile('main.pid')
    try:
        pid_file.create()
        start_message = Message()
        start_message_content = "Script is now online, looking for new transactions..."
        start_message.send(start_message_content, bot_token, target_id)
        main()

    # This exception is raised when script is closed with ctrl+C
    except KeyboardInterrupt:
        print("Script has been terminated...")

    # this will be raised in any other case
#    except Exception as ex:
#        print("Unknown error has occurred: ", ex)       # prints out error message

    finally:
        end_message = Message()
        end_message_content = "Script is currently offline, there will be no alerts until - back online notification"
        end_message.send(end_message_content, bot_token, target_id)
        print("Script has ended")
        pid_file.delete()

