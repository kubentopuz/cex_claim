import requests
import threading
import time
def claim_farm(auth, device_id):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '369',
        'Content-Type': 'application/json',
        'Referer': 'https://cexp.cex.io/',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        'authData': auth,
        'data': None,
        'devAuthData': device_id,
    }

    response = requests.post('https://cexp.cex.io/api/claimFarm', headers=headers, json=json_data)
    print(response.text)

def start_farm(auth, device_id):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Length': '369',
        'Content-Type': 'application/json',
        'Referer': 'https://cexp.cex.io/',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        'authData': auth,
        'data': None,
        'devAuthData': device_id,
    }

    response = requests.post('https://cexp.cex.io/api/startFarm', headers=headers, json=json_data)
    print(response.text)

def process_data(auth, device_id):
    try:
        claim_farm(auth, device_id)
        time.sleep(15)
        start_farm(auth, device_id)
    except Exception as e:
        print(f"Error processing data for device {device_id}: {e}")

with open('datacex.txt', 'r') as file:
            for line in file:
                auth, device_id = line.strip().split('|')
                threading.Thread(target=process_data, args=(auth, device_id)).start()
            time.sleep(5)
