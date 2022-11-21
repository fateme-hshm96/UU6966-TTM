import random


def fill(template, ids, FFF, CCC, VVV):
    temp_FFF = FFF.copy()

    if 'XXX' in template:
        id_ = str(random.choice(ids))
        template = template.replace('XXX', id_)

    for f in ['1', '2', '3']:
        if 'FFF' + f in template:
            feature1 = random.choice(temp_FFF)
            temp_FFF.remove(feature1)
            template = template.replace('FFF' + f, feature1)

            if 'VVV' + f in template:
                start = VVV[feature1][0]
                end = VVV[feature1][1]
                if isinstance(end, int):
                    value1 = str(random.randint(start, end))
                else:
                    value1 = str(round(random.uniform(start, end), 3))
                template = template.replace('VVV' + f, value1)

            if 'CCC' + f in template:
                ageCCC = ['older than', 'younger than', 'set to', 'equal to', 'over', 'below']
                if feature1 != 'age':
                    compare1 = random.choice(CCC)
                else:
                    compare1 = random.choice(ageCCC)
                template = template.replace('CCC' + f, compare1)

    if 'XXX' in template or 'FFF' in template or 'VVV' in template or 'CCC' in template:
        return 'ERROR'

    return template


if __name__ == '__main__':

    valid_ids = [51, 27, 144, 617, 522, 535, 389, 399, 81, 80, 450, 124, 137, 291, 293, 432, 651, 741, 397, 392, 665,
                 627, 303, 229, 197, 624, 411, 621, 211, 85, 266, 710, 324, 442, 269, 121, 45, 103, 78, 447, 356, 101,
                 376, 709, 407, 597, 472, 767, 623, 728, 600, 412, 679, 163, 534, 547, 201, 102, 661, 235, 31, 466, 465,
                 112, 177, 528, 237, 619, 613, 97, 694, 610, 377, 127, 461, 224, 136, 301, 469, 515, 105, 454, 109, 673,
                 68, 572, 145, 385, 313, 106, 216, 644, 751, 448, 416, 134, 247, 700, 232, 758, 230, 251, 157, 595, 467,
                 239, 142, 108, 607, 347, 288, 632, 73, 150, 457, 451, 688, 391, 452, 599, 271, 585, 210, 40, 738, 653,
                 70, 577, 640, 395, 79, 49, 731, 514, 342, 55, 378, 579, 86, 65, 10, 123, 270, 693, 648, 748, 443, 487,
                 552, 400, 387, 351, 523, 41, 48, 358, 388, 439, 314, 294, 214, 730, 542, 756, 590, 159, 215, 180, 568,
                 16, 355, 716, 58, 477, 170, 323, 206, 186, 194, 518, 563, 284, 744, 238, 155, 329, 492, 464, 357, 739,
                 28, 39, 91, 175, 596, 126, 453, 4, 549, 459, 327, 5, 264, 743, 386, 64, 14, 759, 576, 468, 478, 107,
                 304, 548, 336, 505, 319, 715, 529, 306, 431, 737, 30, 578, 243, 539, 657, 116, 339, 111, 209, 115, 143,
                 766, 630, 37, 537, 506, 95, 689, 283, 702, 417, 236, 592, 53, 246, 668, 151, 536, 424, 188, 132, 406,
                 602, 427, 185, 546, 43, 646, 330, 404, 690, 390, 61, 263, 192, 558, 723, 67, 362, 429, 498, 338, 594,
                 509, 131, 745, 130, 499, 114, 628, 129, 667, 393, 204, 272, 8, 636, 691, 557, 93, 322, 634, 250, 147,
                 57, 614, 46, 199, 350, 233, 195, 359, 532, 169, 296, 317]

    FFF = ["glucose", "bmi", "age", "diabetes pedigree function", "blood pressure", "pregnancies", "skin thickness",
           "insulin"]  # features

    CCC = ["of", "set to", "over", "below", "greater than", "lower than", "equal to", "no larger than",
           "higher than"]  # comparison

    VVV = {"glucose": [10, 200], "bmi": [10, 68], "age": [20, 100], "diabetes pedigree function": [0.084, 2.5],
           "blood pressure": [20, 123],
           "pregnancies": [1, 17], "skin thickness": [10, 99], "insulin": [50, 680]}

    question_templates = {"prediction":
                          ["what's the label for id XXX",
                           "what's the prediction for id XXX",
                           "please tell me what the model predicts instances with VVV1 FFF1 or VVV2 FFF2 or VVV3 FFF3?",
                           "please tell me what the model predicts instances with VVV1 FFF1 and VVV2 FFF2",
                           "please tell me what the model predicts instances with VVV1 FFF1 or VVV2 FFF2?",
                           "show prediction of id XXX"],
                          "prediction_likelihood":
                          ["what's the probability of likely to have diabetes?",
                           "how likely is id XXX to have diabetes?",
                           "what is the chance that the data point with id XXX is likely to have diabetes",
                           "what is the chance that id XXX is likely to have diabetes",
                           "what is the probability that id XXX is predicted as likely to have diabetes by the model?",
                           "return the probability that instance XXX is predicted in the "
                           "unlikely-to-have-diabetes class",
                           "for those with FFF1 CCC1 VVV1, what are the likelihoods of unlikely to have diabetes?",
                           "for those with FFF1 CCC1 VVV1 and FFF2 CCC2 VVV2, what are the likelihoods of unlikely "
                           "to have diabetes?",
                           "for those with FFF1 CCC1 VVV1 or FFF2 CCC2 VVV2, what are the likelihoods of unlikely "
                           "to have diabetes?",
                           "for those with FFF1 CCC1 VVV1 and FFF2 CCC2 VVV2 and FFF3 CCC3 VVV3, what are the "
                           "likelihoods of unlikely to have diabetes?",
                           "for those with FFF1 CCC1 VVV1 or FFF2 CCC2 VVV2 or FFF3 CCC3 VVV3, what are the "
                           "likelihoods of unlikely to have diabetes?",
                           "for data points with FFF1 CCC1 VVV1, what is the chance of unlikely to have diabetes?",
                           "for data points with FFF1 CCC1 VVV1 and FFF2 CCC2 VVV2, what is the chance of unlikely "
                           "to have diabetes?",
                           "for data points with FFF1 CCC1 VVV1 or FFF2 CCC2 VVV2, what is the chance of unlikely "
                           "to have diabetes?",
                           "for data points with FFF1 CCC1 VVV1 and FFF2 CCC2 VVV2 and FFF3 CCC3 VVV3, what is "
                           "the chance of unlikely to have diabetes?",
                           "for data points with FFF1 CCC1 VVV1 or FFF2 CCC2 VVV2 or FFF3 CCC3 VVV3, what is "
                           "the chance of unlikely to have diabetes?",
                           "please tell me what is the probability that the model predicts instances with VVV1 FFF1 "
                           "or VVV2 FFF2 or VVV3 FFF3 to have diabetes.",
                           "please tell me what is the probability that the model predicts instances with VVV1 FFF1 "
                           "or VVV2 FFF2 to have diabetes.",
                           "please tell me what is the probability that the model predicts instances with VVV1 FFF1 "
                           "and VVV2 FFF2 to have diabetes."],
                          "label":
                          ["what are the labels for everything with FFF1 CCC1 VVV1",
                           "what is the label for id XXX?",
                           "what's the gold label for FFF1 CCC1 VVV1 and FFF2 CCC2 VVV2"],
                          "show_data":
                          ["show me some instances where FFF1 is CCC1 VVV1",
                           "for XXX please show me the values of the features.",
                           "can you display the instance with id XXX",
                           "return the data where FFF1 CCC1 VVV1 and FFF2 CCC2 VVV2 people",
                           "show me some data where FFF1 is VVV1 but FFF2 is not less than VVV2",
                           "show me some data where FFF1 is VVV1 but FFF2 is over VVV2",
                           "can you display the instance with id XXX",
                           "show XXX"],
                          "feature_importance":
                          ["could you please indicate when the FFF1 feature is important?",
                           "most important feature?",
                           "third most important feature?",
                           "second most important feature?",
                           "Tell me the second most important feature for men",
                           "Tell me the second most important feature for wommen",
                           "Tell me the third most important feature for men",
                           "Tell me the third most important feature for wommen",
                           "what is the 4th most important feature?",
                           "if people with FFF1 not CCC1 VVV1 were to have FFF2 decreased by VVV2, what would the "
                           "top 5 most important features be?",
                           "if people with FFF1 not CCC1 VVV1 were to have FFF2 increased by VVV2, what would the "
                           "top 5 most important features be?",
                           "5 most important features for FFF1 CCC1 VVV1", ],
                          "change_prediction":
                          ["what does an instance with id XXX need to do to change the prediction?",
                           "could you please tell me the predictions for id XXX and what you have to do to flip "
                           "the prediction?",
                           "show me how to change the prediction for the instance with id XXX",
                           "how would you flip the prediction for id XXX",
                           "what does instance with id XXX need to do to change the prediction?",
                           "how would you flip the prediction for id XXX",
                           "flip the classification for sample XXX?"],
                          "explain":
                          ["explain id XXX",
                           "what does my model predict for data XXX? next, once you've completed this, could you tell "
                           "me why the model predicts it (i.e., what's it rationale)?",
                           "why is id XXX predicted likely to have diabetes",
                           "tell me why is id XXX predicted likely to have diabetes",
                           "explain my model's prediction for data XXX and then follow up with the rationale for "
                           "the prediction!"],
                          'what_if':
                          ["what if we took VVV1 points away from FFF1 for id XXX what would happen to the "
                           "probability of the predictions?",
                           "what if we set FFF1 to VVV1 for id XXX what would happen to the probability of "
                           "the predictions?",
                           "what would happen to the predictions for instances with FFF1 CCC1 VVV1 if you were "
                           "to change FFF2 to VVV2?",
                           "what would happen to the class probabilities if we increased FFF1 by VVV1?",
                           "what would happen to the class probabilities if we decreased FFF1 by VVV1?",
                           "tell me what the model would predict if you decreased FFF1 by VVV1 on all the data",
                           "tell me what the model would predict if you increased FFF1 by VVV1 on all the data",
                           "What would the predictions be if you set the FFF1 to VVV1 on the entire dataset?",
                           "what are the model’s predictions on FFF1 CCC1 VVV1 and what would it be if you "
                           "decreased FFF2 by VVV2?",
                           "what are the model’s predictions on FFF1 CCC1 VVV1 and what would it be if you "
                           "increased FFF2 by VVV2?",
                           "what would the prediction for id XXX be if you change the FFF1 to VVV1?",
                           "what would happen to the distribution of model predictions if people with "
                           "FFF1 CCC1 VVV1 had FFF2 CCC2 VVV2 and FFF3 CCC3 VVV3?",
                           "what are the model’s predictions on FFF1 CCC1 VVV1 and what would it be if you "
                           "decreased FFF2 by VVV2?",
                           "what are the model’s predictions on FFF1 CCC1 VVV1 and what would it be if you "
                           "increased FFF2 by VVV2?",
                           "if we set FFF1 of sample XXX to VVV1 what would the class probabilities be?"]
                          }

    filled_questions = []
    for k in question_templates.keys():
        if k in ['change_prediction', 'explain', 'what_if']:
            x = 200
        else:
            x = 100
        for i in range(0, x):
            temp = random.choice(question_templates[k])
            q = fill(temp, valid_ids, FFF, CCC, VVV)
            filled_questions.append(q)

    random.shuffle(filled_questions)
    random.shuffle(filled_questions)
    random.shuffle(filled_questions)
    print(*filled_questions, sep='\n')
