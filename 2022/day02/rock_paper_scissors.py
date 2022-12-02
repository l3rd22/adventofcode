total_score = 0
total_score_b = 0
with open("input.txt") as strategy_guide:
    for game_plan in (list(map(ord, line.split())) for line in strategy_guide):
        symbol_score = game_plan[1] - ord("X") + 1
        outcome_score = (game_plan[1] - game_plan[0] + 2) % 3 * 3
        total_score += symbol_score + outcome_score

        symbol_score_b = ((game_plan[0] - ord("A")) + (game_plan[1] - ord("Y"))) % 3 + 1
        outcome_score_b = (game_plan[1] - ord("X")) * 3 
        total_score_b += symbol_score_b + outcome_score_b
print(total_score)
print(total_score_b)
