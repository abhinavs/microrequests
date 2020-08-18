
import microrequests

HTTPBIN_BASE        = "http://httpbin.org"
HTTPBIN_BASE_HTTPS  = "https://httpbin.org"
TEST_API            = "https://api.ipify.org"
EXAMPLE_API         = "http://www.example.com/api"
PAYLOAD             = {'key1': 'value1', 'key2': 'value2'}

def test_requests():
    mr = microrequests.init()
    response = mr.get(HTTPBIN_BASE + "/get")
    assert response.status_code == 200
    assert response.json()

    response = mr.post(HTTPBIN_BASE + "/post", data=PAYLOAD)
    assert response.status_code == 200
    assert response.json()

def test_https():
    mr = microrequests.init()
    response = mr.get(HTTPBIN_BASE_HTTPS + "/get")
    assert response.status_code == 200
    assert response.json()

    response = mr.post(HTTPBIN_BASE_HTTPS + "/post", data=PAYLOAD)
    assert response.status_code == 200
    assert response.json()

def test_session():
    pass

def test_session_connection():
    mr = microrequests.init()

    conn1 = mr.get_adapter(TEST_API).get_connection(TEST_API)
    conn2 = mr.get_adapter(TEST_API).get_connection(TEST_API)
    assert conn1 == conn2
    conn3 = mr.get_adapter(EXAMPLE_API).get_connection(EXAMPLE_API)
    assert conn2 != conn3


