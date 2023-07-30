import requests


class HTTP:
    # this will not use self, herein better to define as staticmethod
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
