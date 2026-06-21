from functools import reduce


scores = [

    78,

    90,

    65,

    88,

    95

]


# map()

bonus_scores = list(

    map(

        lambda score: score + 5,

        scores

    )

)


# filter()

high_scores = list(

    filter(

        lambda score: score >= 80,

        scores

    )

)


# reduce()

total_score = reduce(

    lambda x, y: x + y,

    scores

)


print("Original Scores :", scores)

print("Bonus Scores :", bonus_scores)

print("High Scores :", high_scores)

print("Total Score :", total_score)