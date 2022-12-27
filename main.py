import sys
import requests
def read_request_from_file(filename):
    return 'https://www.boredapi.com/api/activity?participants=1'

def handle_request(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print('starting dataseeker')
    print(sys.argv)

    filename = sys.argv[1]
    url = read_request_from_file(filename)
    response = handle_request(url)
    print(response)








