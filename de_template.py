import csv
import re

def detemplate(response, patterns):
	for pattern in patterns:
		prev = response
		if pattern in [":", "\<li\>", "\</li\>","\<b\>", "\</b\>", "\<br\>", "\</br\>", "\<ul\>", "\</ul\>", "\<em\>", "\</em\>", "[ ]+"]:

			response = re.sub(pattern, ' ', response)
		else:
			response = re.sub(pattern, '', response)

		response = re.sub("[ ]+", ' ', response)
		response = response.replace(' .', '.')
		response = response.replace(' ,', ',')
		response = response.replace(' :', ':')
		response = response.replace(' ?', '?')
		response = response.replace(' !', '!')
		response = response.replace(' ;', ';')

		# if prev != response:
			# print('------------------------')
			# print(prev)
			# print('--->', pattern)
			# print(response, end='\n\n')

	special_cases = ["There are no instances in the data that meet this description.",
					 'There are no instances that meet this description!']
	for x in special_cases:
		if response in x or x in response:
			response = 'NONE'

	response = response.replace('diabetespedigreefunction', 'diabetes pedigree function')
	response = response.replace('skinthickness', 'skin thickness')
	response = response.replace('bloodpressure', 'blood pressure')
	response = response.replace('..', '.')
	if response.startswith(", "):
		response = response[2:]

	if response.startswith(" , "):
		response = response[3:]

	response = response.strip()

	return 'Information: '+response

if __name__ == '__main__':
	
	strings_to_remove = [
					 # general
					 "\<b\>", "\</b\>",
					 "\<br\>", "\</br\>",
					 "\<li\>", "\</li\>",
					 "\<ul\>", "\</ul\>",
					 "\<em\>", "\</em\>",
					 "&#129502",

					 # change
					 "The instance with [a-z ]+ (\d+(\.\d+)?) is predicted [a-z]+ to have diabetes. For instances where [a-z ]+ (\d+(\.\d+)?), the original prediction is ",
					 "Here are some options to change the prediction of this instance",
					 "First, if you",
					 "Furthermore, if you ",
					 "Further, if you ",
					 # "the model will predict likely to have diabetes.",
					 # "the model will predict unlikely to have diabetes.",
					 "If you want some more options, just ask ",

					 # pred likelihood
					 "Over (\d+(\.\d+)?) cases where [a-z ]+ (\d+(\.\d+)?) in the data, the model predicts:",
					 "Over (\d+(\.\d+)?) cases where [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?) in the data, the model predicts",
					 "Over (\d+(\.\d+)?) cases where [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?) in the data, the model predicts",
					 "Over (\d+(\.\d+)?) cases in the data, the model predicts:",
					 "The model predicts the instance with id equal to (\d+(\.\d+)?) as:",

					 # show data
					 "For the data with [a-z ]+ (\d+(\.\d+)?), the instance id's are:",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?), the instance id's are:",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?), the instance id's are:",
					 "For the data with [a-z ]+ (\d+(\.\d+)?)",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?)",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?)",
					 "Which one do you want to see?",
					 "For the data with id equal to (\d+(\.\d+)?), the features are",
					 "For all the instances in the data,",
					 "I've truncated this instance to be concise. Let me know if you want to see the rest of it.",

					 # score
					 "The model scores ",
					 "accuracy on the data",

					 # what if
					 "For the data with [a-z]+ is increased by (\d+(\.\d+)?), the model predicts:",
					 "For the data with [a-z]+ is decreased by (\d+(\.\d+)?), the model predicts:",

					 # predict
					 "The instance with [a-z ]+ (\d+(\.\d+)?) is predicted",
					 "The instance [a-z ]+ (\d+(\.\d+)?) is predicted",
					 "For the data with [a-z ]+ (\d+(\.\d+)?),",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?)",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?)",

					 # label
					 "For the data with [a-z ]+ (\d+(\.\d+)?), the label is ",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?), the label is ",
					 "For the data with [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?), the label is ",
					 "For the data with [a-z ]+ (\d+(\.\d+)?), the labels are ",
					 "is labeled",

					 # importance
					 "For the model's predictions",
					 "Here, rank 1 is the most important feature (out of 8 features). ",
					 "Compared to other instances where [a-z ]+ (\d+(\.\d+)?)",
					 "Compared to other instances where [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?)",
					 "Compared to other instances where [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?)",
					 "Compared to other instances in the data,",
					 "the importance of the features have the following ranking, where 1 is the most important feature:",
					 "the top (\d+(\.\d+)?) most important features are as follows, where 1 is the most important feature:",

					 # explain
					 "For instances with [a-z ]+ (\d+(\.\d+)?) predicted",
					 "For instances with [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?) predicted",
					 "For instances with [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?) predicted",
					 "is the [a-z]*most important feature and has a",
					 "influence on the predictions",
					 "I can provide a more comprehensive overview of how important different features in the data are for the model's predictions, just ask for more description",

					 # define
					 "Definition for feature name",
					 "The feature named [a-z]+ is defined as: ",

					 # count_data_points
					 "Let me know if you want to see their ids.",

					 # interaction
					 "For the model's predictions on instances instances where ",
					 "For the model's predictions on the data,",
					 "most significant feature interaction effects are as follows, ",
					 "where higher values correspond to greater interactions.",

					 # lastly
					 ":",
					 "[ ]+"
					 " , ",
					 "to have ",
					 "probability",
					 "There are ",
					 "is predicted"
					 "where [a-z ]+ (\d+(\.\d+)?).",
					 "the model predicts",
					 "the model will predict ",
					 "The instance with [a-z ]+ (\d+(\.\d+)?)",
					 "The instance with [a-z ]+ (\d+(\.\d+)?) or [a-z ]+ (\d+(\.\d+)?)",
					 "The instance with [a-z ]+ (\d+(\.\d+)?) and [a-z ]+ (\d+(\.\d+)?)",
					 "For instances where [a-z ]+ (\d+(\.\d+)?), the original prediction is",
					 "has a ",
					 "effect",
					 

	]

	
	filename = 'answered_questions_responses.csv'

	cleaned_responses = []
	with open(filename) as f:
		data = csv.reader(f)
		for line in data:
			# print('------------------------')
			cleaned_responses.append(detemplate(line[0], strings_to_remove))

	print(*cleaned_responses, sep='\n')


	