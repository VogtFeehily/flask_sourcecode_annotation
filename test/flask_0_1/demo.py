# -*- coding: utf8 -*-

from test.flask_0_1.demo import ctx
from test.flask_0_1.demo import request, request_test


class Request:
    pass


class Context:
    def __init__(self):
        self.request = Request()


def create_app():
    ctx.push(Context())


if __name__ == '__main__':

    create_app()
    request.a = [3, [3, 4]]
    print(request.a)
    request.a.append(666)
    request.a[1].append(666)
    print(request.a)

    print('-=-=-=-=-=-=-')
    request_test.a = [3, [3, 4]]
    print(request_test.a)
    request_test.a.append(666)
    request_test.a[1].append(666)
    print(request_test.a)
