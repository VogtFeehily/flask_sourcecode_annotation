# -*- coding: utf8 -*-

from werkzeug.local import LocalStack, LocalProxy

# context locals
ctx = LocalStack()

request = LocalProxy(lambda: ctx.top.request)
request_test = lambda: ctx.top.request
