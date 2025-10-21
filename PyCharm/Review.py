def summarize_book_ratings(library, book_title):
    min_val = 6
    max_val = 0
    avg = 0
    ratings = []
    for lib, info in library.items():
        if book_title in info:
            value = sum(info[book_title])/len(info[book_title])
            if min(info[book_title]) < min_val:
                min_val = min(info[book_title])
            if max(info[book_title]) > max_val:
                max_val = max(info[book_title])
            ratings.append(value)
    return min_val, max_val, round(sum(ratings)/len(ratings), 1)
ratings_data = {
    "UF Library": {"Dune": [5,4,5], "1984": [4,4]},
    "City Library": {"Dune": [3,4], "Brave New World": [5]},
    "Public Archive": {"Dune": [2,5,4], "1984": [3,4]}
}
print(summarize_book_ratings(ratings_data, "Dune"))



def classify_student_scores(scores):
    if scores == {}:
        return {}
    name, score = scores.popitem()
    rest = classify_student_scores(scores)
    if score >= 90:
        rest[name] = "Excellent"
    elif 89 >= score >= 75:
        rest[name] = "Good"
    else:
        rest[name] = "Needs Improvement"
    return rest
scores = {"Alice": 95, "Bob": 82, "Charlie": 70, "Diana": 88}
print(classify_student_scores(scores))

