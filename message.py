import requests


class Message:

    content = ''
    send_status = False


    # generates message content from template
    def generate(self, response_dict):
        amount_usd = self.__separate_thousands(response_dict['amount_usd'])
        emoji = u"\U0001F6A8"       # emoji :rotating_light: unicode
        self.content = f"""{emoji} {response_dict['amount']} {response_dict['symbol'].upper()} ({amount_usd} USD) transferred from {response_dict['from']} to {response_dict['to']}."""

    # sends content to specified chat as a bot
    def send(self, bot_token, chatID):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + self.content
        response = requests.get(send_text)
        self.__check_send_status(response)


    def __check_send_status(self, response):
        response_json = response.json()
        send_status = response_json.get("ok", False)        # saves response send status to send_status, if it doesn't exist saves as default False
        try:
            if send_status:
                print(f"Message {self.content} sent successfully")
            else:
                raise MessageSendingError

        except MessageSendingError:
            print("Sending message failed.")
            print(f"Error code: {response_json['error_code']} description: {response_json['description']}")


    def __separate_thousands(self, numb_to_separate):
        outcome = '{:20,.2f}'.format(numb_to_separate)
        outcome = outcome.replace(" ", "")      # bugfix
        return outcome


class MessageSendingError(Exception):
    """Message couldn't be sent"""
    pass
