import requests

def test_requests():
    response = requests.get("https://raw.githubusercontent.com/AnkushSharma2698/CMPUT404Lab1/main/req.py")
    print(response.text)

if __name__ == "__main__":
    test_requests()