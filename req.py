import requests

def test_requests():
    print(requests.__version__)
    response = requests.get("http://google.com")
    print(response.status_code)

if __name__ == "__main__":
    test_requests()