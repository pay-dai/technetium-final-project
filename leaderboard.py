# Jason Ayala
# The function creates a leadeboard based off completed rounds
# and score
def build_leaderboard(rounds):
    """Build a ranked leaderboard from completed rounds including total score.
    Higher total score ranks first. if scores are tied, player with fewer rounds
    ranks higher.If both score and rounds are tied, whoever appears first in the input
    ranks higher
    
    Args:
        rounds (list): a list of dictionaries, one per completed round
    
    Returns:
        list: A ranked list of player dictionaries which contains "username",
            "total_score", "rounds_played", and "rank"
    """
    
    player_stats = {}
    
    for round_result in rounds:
        username = round_result["username"]
        score = round_result["score"]
        
        if username not in player_stats:
            player_stats[username] = {
                "username": username,
                "total_score": 0,
                "rounds_played": 0
            }
        
        player_stats[username]["total_score"] += score
        player_stats[username]["rounds_played"] += 1
    
    leaderboard = sorted(player_stats.values(), key=lambda player:
        player["rounds_played"])
    
    leaderboard = sorted(leaderboard, key=lambda player: player["total_score"],
                         reverse=True)
    
    rank = 1
    for player in leaderboard:
        player["rank"] = rank
        rank += 1
    return leaderboard