import random

def schedule_matches(num_teams):

    teams = [f"Team {i+1}" for i in range(num_teams)]
    random.shuffle(teams)
    matches = []
    for i in range(0, len(teams)-1, 2):
        matches.append((teams[i], teams[i+1]))
    if len(teams)%2 != 0:
        matches.append((teams[-1], "Bye"))
    return matches

num_teams = 10
match_schedule = schedule_matches(num_teams)
print("Tournament Matches")
for match in match_schedule:
    print(f"{match[0]} vs {match[1]}")
