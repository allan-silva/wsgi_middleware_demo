import sys
import time
import requests


if __name__ == "__main__":
    delay = int(sys.argv[1])
    tid = sys.argv[2]
    time.sleep(delay)
    for i in range(0, 1000):
        resp = requests.get(f"http://127.0.0.1:5000/update/6/firefox/77.0.1?id={tid}-{i}")
        if not resp.ok:
            print(f"ERROR: {idt}-{i}")
