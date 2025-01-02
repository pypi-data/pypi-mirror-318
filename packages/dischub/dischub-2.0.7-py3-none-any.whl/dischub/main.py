import requests
class Dischub:
    def __init__(self):
        self.api_url = "https://dischub.co.zw/api/orders/create/" 
    def create_payment(self, data):
        try:
            response = requests.post(self.api_url, json=data)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            return response  # Assuming the response is in JSON format
        except requests.exceptions.ConnectionError:
            return {'status': 'error', 'message': 'connection failed. unable to reach the server.'}
        except requests.exceptions.Timeout:
            return {'status': 'error', 'message': 'request timed out.'}
        except requests.exceptions.RequestException as e:
            # Catch other exceptions like HTTP errors or invalid URLs
            return {'status': 'error', 'message': f'an error occurred: server not responding'}