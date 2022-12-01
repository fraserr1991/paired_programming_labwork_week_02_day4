def get_latest_score(scores):
    return scores[-1]

def personal_best(scores):
    #return max(scores)
    scores.sort()
    return scores[-1]


# def personal_top_three(scores):
#     high_scores = []
#     scores.sort()
#     high_scores.append(scores[-1])
#     high_scores.append(scores[-2])
#     high_scores.append(scores[-3])
#     return high_scores

def personal_top_three(scores):
    
    scores.sort(reverse = True)
    return scores[:3]

def highest_to_lowest(scores):
    scores.sort(reverse = True)
    return scores


