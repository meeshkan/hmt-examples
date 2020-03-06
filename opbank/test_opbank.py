import requests

from opbank.opbank_client import OPBankClient


def test_opbank():
    requests.delete("http://localhost:8888/admin/storage")

    client = OPBankClient()
    client.API_URL = 'http://localhost:8000/https://sandbox.apis.op-palvelut.fi/'

    payer_iban = 'FI3959986920207073'
    receiver_iban = 'FI2350009421535899'
    amount = 5

    accounts = client.get_accounts()
    print('Account list before payment: {}'.format(accounts))
    assert 2215.81 == accounts[payer_iban]['balance']
    assert 0 == accounts[receiver_iban]['balance']


    payment = client.init_payment(payer_iban, receiver_iban, amount)
    payment_id = payment['paymentId']
    print("Created payment {}".format(payment))

    accounts = client.get_accounts()
    print('Account list before confirmation: {}'.format(accounts))
    assert 2215.81 == accounts[payer_iban]['balance']
    assert 0 == accounts[receiver_iban]['balance']

    confirmation = client.confirm_payment(payment_id)

    accounts = client.get_accounts()
    print('Account list after confirmation: {}'.format(accounts))
    assert 2210.81 == accounts[payer_iban]['balance']
    assert 5 == accounts[receiver_iban]['balance']



