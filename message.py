import requests


class Message:

    # generates message content from template
    def generate(self, response_dict):
        amount_usd = self.__separate_thousands(response_dict['amount_usd'])
        emoji = u"\U0001F6A8"       # emoji :rotating_light: unicode
        content = f"{emoji} {response_dict['amount']} {response_dict['symbol'].upper()} ({amount_usd} USD) transferred from {response_dict['from']} to {response_dict['to']}."
        return content
    
    # sends content to specified chat as a bot
    def send(self, message_content, bot_token, chatID):
        send_text = ('https://api.telegram.org/bot' + bot_token +
                     '/sendMessage?chat_id=' + chatID +
                     '&parse_mode=Markdown&text=' + message_content)

        response = requests.get(send_text)
        self.__check_send_status(response)

    @staticmethod
    def __check_send_status(response):
        response_json = response.json()

        # saves response send status to send_status, if it doesn't exist saves as default False
        send_status = response_json.get("ok", False)
        try:
            if send_status:
                print(f"Message sent successfully")
            else:
                raise MessageSendingError

        except MessageSendingError:
            print("Sending message failed.")
            print(f"Error code: {response_json['error_code']} description: {response_json['description']}")

    @staticmethod
    def __separate_thousands(numb_to_separate):
        outcome = '{:20,.2f}'.format(numb_to_separate)
        outcome = outcome.replace(" ", "")      # deletes all spaces
        return outcome


class MessageSendingError(Exception):
    """Message couldn't be sent"""
    pass
