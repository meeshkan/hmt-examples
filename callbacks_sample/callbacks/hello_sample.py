from hmt.serve.mock.callbacks import callback


@callback('api.com', 'get', '/hello', format='plain')
def hello_callback(query, response_body, storage):
    name = query.get('name')
    name = 'my friend' if name is None else name[0]
    return 'Hello, {}'.format(name)
