import requests
class Dischub:
    def __init__(self):
        self.api_url = "http://dischub.co.zw/api/orders/create/"
    def create_payment(self, data):
        response = requests.post(self.api_url, json=data)
        return response
