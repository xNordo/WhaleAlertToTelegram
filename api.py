import requests
import time
import math
from exceptions import *
from login_data import api_key


class WhaleAlertAPI:

    api_key = api_key

    # Makes requests and returns api response
    def make_request(self):
        start_time = self.__get_time()
        try:
            link = self.__create_request_link(self.api_key, start_time)
            r = requests.get(link)
            return r

        except:
            print("Couldn't send request to API.")

    # Creates request URL to api with given API key and start time in UNIX timestamp
    def __create_request_link(self,api_key, start_time):
        link = f"https://api.whale-alert.io/v1/transactions?api_key={api_key}&min_value=500000&start={start_time}&cursor=2bc7e46-2bc7e46-5c66c0a7"
        return link

    # Returns current time -10 secounds in UNIX timestamp
    def __get_time(self):
        current = time.time()
        outcome = math.floor(current)
        outcome = outcome - 10
        return outcome

    @staticmethod
    def check_status_code(api_response):
        try:
            status = api_response.status_code
            if status == 200:
                print("200	Ok -- The request was successful.")
            elif status == 400:
                raise BadRequest
            elif status == 401:
                raise Unauthorized
            elif status == 403:
                raise Forbidden
            elif status == 404:
                raise NotFound
            elif status == 405:
                raise MethodNotAllowed
            elif status == 406:
                raise NotAcceptable
            elif status == 429:
                raise TooManyRequests
            elif status == 500:
                raise InternalServerError
            elif status == 503:
                raise ServiceUnavilable


        except BadRequest:
            print("Bad Request -- Your request was not valid.")

        except Unauthorized:
            print("Unauthorized -- No valid API key was provided")

        except Forbidden:
            print("Forbidden -- Access to this resource is restricted for the given caller.")

        except NotFound:
            print("Not Found -- The requested resource does not exist.")

        except MethodNotAllowed:
            print("Method Not Allowed -- An invalid method was used to access a resource.")

        except NotAcceptable:
            print("Not Acceptable -- An unsupported format was requested.")

        except TooManyRequests:
            print("Too Many Requests -- You have exceeded the allowed number of calls per minute. Lower call frequency or upgrade your plan for a higher rate limit.")

        except InternalServerError:
            print("Internal Server Error -- There was a problem with the API host server. Try again later.")

        except ServiceUnavilable:
            print("Service Unavailable -- API is temporarily offline for maintenance. Try again later.")

        except:
            print("Something went terribly wrong")
            exit()



