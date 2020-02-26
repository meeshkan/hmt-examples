import requests


class OPBankClient:
    API_URL = 'https://sandbox.apis.op-palvelut.fi/'
    API_KEY = 'ZoStul8nNuwq1SYCzSrLcO1wAj4Tyf7x'
    API_TOKEN = '6c18c234b1b18b1d97c7043e2e41135c293d0da9'

    def get_accounts(self):
        accounts = requests.get(self.API_URL + '/accounts/v3/accounts',
                                headers={'x-api-key': self.API_KEY,
                                         'authorization': "Bearer {}".format(self.API_TOKEN)}).json()['accounts']
        return {account['identifier']: account for account in accounts}

    def init_payment(self, payer_iban, receiver_iban, amount):
        body = {
            "amount": amount,
            "subject": "Client Test",
            "currency": "EUR",
            "payerIban": payer_iban,
            "valueDate": "2020-01-27T22:59:34Z",
            "receiverBic": "string",
            "receiverIban": receiver_iban,
            "receiverName": "string"
        }
        url = self.API_URL + '/v1/payments/initiate'
        response = requests.post(url, headers={'x-api-key': self.API_KEY, 'x-authorization': self.API_TOKEN}, json=body)
        return response.json()

    def confirm_payment(self, payment_id):
        body = {
            'paymentId': payment_id
        }
        url = self.API_URL + '/v1/payments/confirm'
        response = requests.post(url, headers={'x-api-key': self.API_KEY, 'x-authorization': self.API_TOKEN}, json=body)
        return response.json()
