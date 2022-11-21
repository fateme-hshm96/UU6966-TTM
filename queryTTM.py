import requests
import time


def query_TTM(userInput):
	userName = "user"
	PARAMS = {'userInput':userInput, 'userName':userName}
	  
	# sending get request and saving the response as response object
	# r = requests.get(url = URL, params = PARAMS)
	r = requests.post(url=URL, json=PARAMS)

	# return (r.text)
	return (r.text).split('<>')[0]


if __name__ == '__main__':
	# URL = "http://129.82.45.126:4455/"
	URL = "http://129.82.45.126:4455/get_response"

	q_file = 'questions.txt'
	with open(q_file) as f:
		data = f.readlines()

	for userInput in data:
		print('Question:', userInput)
		# print()
		response = query_TTM(userInput)
		print('Response:', response)
		print('###')
		time.sleep(10)

