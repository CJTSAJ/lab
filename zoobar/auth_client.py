from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def login(username, password):
    ## Fill in code here.

    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as connect:
        ret =  connect.call('get_cred', username=username, password=password)
        return ret


def register(username, password):
    ## Fill in code here.
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as connect:
        ret = connect.call('create_cred', username=username, password=password)
        return ret

def check_token(username, token):
    ## Fill in code here.
    host = readconf.read_conf().lookup_host('auth')
    with rpclib.client_connect(host) as connect:
        ret = connect.call('check_token', username=username, token=token)
        return ret
