import copy

from meeshkan.serve.mock.callbacks import callback


@callback('sandbox.apis.op-palvelut.fi', 'post', '/v1/payments/initiate', format='json')
def initiate(request_body, response_body, storage):
    """
    This callback function is called on a request to the `/v1/payments/initiate` endpoint.
    It stores a request body into internal storage to modify accounts after confirmation.
    :param request_body: a request body
    :param response_body: a mocked response body
    :param storage: the internal storage
    :return: a response body without modifications
    """
    storage[response_body['paymentId']] = request_body
    return response_body


@callback('sandbox.apis.op-palvelut.fi', 'post', '/v1/payments/confirm', format='json')
def confirm(request_body, response_body, storage):
    """
    This callback function is called on a request to the `/v1/payments/confirm` endpoint.
    It stores differences between initial balances of accounts and actual balances after payments are completed.
    :param request_body: a request body
    :param response_body: a mocked response body
    :param storage: the internal storage
    :return: a response body without modifications
    """
    payment_info = storage[response_body['paymentId']]
    storage[payment_info['receiverIban']] = storage.get(payment_info['receiverIban'], 0) + payment_info['amount']
    storage[payment_info['payerIban']] = storage.get(payment_info['payerIban'], 0) - payment_info['amount']
    return response_body


@callback('sandbox.apis.op-palvelut.fi', 'get', '/accounts/v3/accounts', format='json')
def accounts(request_body, response_body, storage):
    """
    This callback function is called on a request to the `/accounts/v3/accounts` endpoint.
    It modifies mocked balances of accounts according to previously confirmed payments.
    :param request_body: a request body
    :param response_body: a mocked response body
    :param storage: the internal storage
    :return: a response body with modified accounts
    """
    response_body_new = copy.deepcopy(response_body)
    for account in response_body_new['accounts']:
        account['balance'] += storage.get(account['identifier'], 0)
    return response_body_new
