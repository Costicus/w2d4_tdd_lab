def latest_score(scores):
    return scores[-1]

def personal_best(scores):
    print("Highest Score is: ", max(scores))
    return max(scores)

def personal_top_three(scores):
    sorted_list = sorted(scores)
    return sorted_list[-1:-4:-1]

# def personal_top_three(scores):
#     sorted_list = highest_to_lowest(scores)
#     count = 3
#     if len(scores) < 3

def ordered_highest_to_lowest(scores):
    scores.sort(reverse = True)
    return scores
