total_score = 0
total_score_b = 0
with open("input.txt") as strategy_guide:
    for opponents_move, response in (map(ord, line.split()) for line in strategy_guide):
        symbol_score = response - ord("X") + 1
        outcome_score = (response - opponents_move + 2) % 3 * 3
        total_score += symbol_score + outcome_score

        symbol_score_b = ((opponents_move - ord("A")) + (response - ord("Y"))) % 3 + 1
        outcome_score_b = (response - ord("X")) * 3 
        total_score_b += symbol_score_b + outcome_score_b
print(total_score)
print(total_score_b)
