import json
import requests
import sys
import string

key = "YANDEX_API_KEY"

def main():
	text = " ".join(sys.argv[1:])
	headers = {
		"Host": "translate.yandex.net",
		"Accept": "*/*",
		"Content-Length": str(len(text)),
		"Content-Type": "application/x-www-form-urlencoded"
	}
	try:
		response = requests.get(u"https://translate.yandex.net/api/v1.5/tr.json/translate?key={0}&text={1}&lang=en-ru".format(key, text))
		if response.json()["code"] == 200:
			for token in response.json()["text"]:
				print(token)
		elif response.json()["code"] == 401:
			print(response.json()["message"])
	except requests.ConnectionError:
		print("No connection")

if __name__ == "__main__":
	main()	
