import requests


class Message:

    content = ''

    def generate(self, response_dict):
        amount_usd = self.__separate_thousands(response_dict['amount_usd'])
        self.content = f"""{response_dict['amount']} {response_dict['symbol'].upper()} ({amount_usd} USD) transferred from {response_dict['from']} to {response_dict['to']}."""

    def send(self, bot_token, chatID):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + self.content
        requests.get(send_text)

    def __separate_thousands(self, numb_to_separate):
        outcome = '{:20,.2f}'.format(numb_to_separate)
        outcome = outcome.replace(" ", "")
        return outcome
