CLIENT_ERRORS = (400, 402, 403, 404)
import requests
from requests.exceptions import HTTPError


def get_url_from_web(url):
    """
    Function -- get_url_from_web
        Give command from website
    Parameters: url, type: object
    ErrorRaised:
        -- HTTPError: handle the error if there is a problem from requesting online resources
        -- ConnectionError: handle the error if there is a connection problem
    Return resp, a object from download csv file from websites
    """
    try:
        resp = requests.get(url)
        resp_status = resp.raise_for_status()
        if resp_status in CLIENT_ERRORS:
            raise HTTPError(
                "Error happens in get_url_from_web(), client errors for url."
            )
    except ConnectionError as error_connection:
        print(type(error_connection), error_connection)

    return resp
