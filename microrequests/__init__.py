import requests
from requests.packages.urllib3.util import Retry

__version__ = "0.1.2"

def __session__(max_retries, pool_connections, pool_maxsize):
    session = requests.Session()

    adapter = requests.adapters.HTTPAdapter(
            max_retries=Retry(total=max_retries, status_forcelist=[500, 502]),
            pool_connections=pool_connections,
            pool_maxsize=pool_maxsize)

    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session

def init(max_retries=1, pool_connections=100, pool_maxsize=50):
    return __session__(max_retries, pool_connections, pool_maxsize)
