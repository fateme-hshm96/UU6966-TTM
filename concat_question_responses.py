import pandas as pd
import random


def read_file(file_name):
	df = pd.read_csv(file_name)
	data = df['data'].tolist()
	return data

if __name__ == '__main__':
	question_file = 'Questions.csv'
	TTM_file = 'TTM_response.csv' 
	T5_file = 'T5_response.csv'

	questions = read_file(question_file)
	TTM_res = read_file(TTM_file)
	T5_res = read_file(T5_file)

	# print(len(questions), len(TTM_res), len(T5_res))

	results = []
	sequesce = []
	for idx, q in enumerate(questions):
		x = random.randint(0, 1)

		query = '<b>Question:</b> '+q+'\n'+'<br><br>'
		
		query += '<b>Response 1:</b> '
		
		if x == 1:
			query += (TTM_res[idx] + '\n'+'<br><br>')
			query += '<b>Response 2:</b> '
			query += (T5_res[idx] + '\n'+'<br><br>')
			sequesce.append(('TTM', 'T5'))
		else:
			query += (T5_res[idx] + '\n'+'<br><br>')
			query += '<b>Response 2:</b> '
			query += (TTM_res[idx] + '\n'+'<br><br>')
			sequesce.append(('T5', 'TTM'))

		results.append(query)

	df = pd.DataFrame(results, columns=['text1'])
	df.to_csv("annotation_samples.csv",index=False)

	# save the output to a file :)
	print(*sequesce, sep='\n')
	