from opbank.opbank_client import OPBankClient

client = OPBankClient()
client.API_URL = 'http://localhost:8002/https://sandbox.apis.op-palvelut.fi/'

payer_iban = 'FI8359986950002741'
receiver_iban = 'FI4859986920215738'
amount = 5

accounts = client.get_accounts()
print('Account list before payment: {}'.format(accounts))

payment = client.init_payment(payer_iban, receiver_iban, amount)
payment_id = payment['paymentId']
print("Created payment {}".format(payment))
confirmation = client.confirm_payment(payment_id)

accounts = client.get_accounts()
print('Account list after payment confirmed: {}'.format(accounts))
