import os
import pecan
from pecan import rest

class GetHandlerController(rest.RestController):
        @pecan.expose('json')
        def get(self):
            return os.uname()

