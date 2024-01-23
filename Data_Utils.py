import math

def calculate_expected_score(rating_a, rating_b):
    """
    Calculate the expected score of player A against player B.
    """
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

def update_elo_rating(rating_a, rating_b, score_a, k=32):
    """
    Update the Elo rating of two players based on the match outcome.
    
    Parameters:
    - rating_a: Elo rating of player A
    - rating_b: Elo rating of player B
    - score_a: Result of the match for player A (1 for win, 0.5 for draw, 0 for loss)
    - k: Weight of the match (default is 32)
    
    Returns:
    - Updated Elo ratings for players A and B
    """
    expected_score_a = calculate_expected_score(rating_a, rating_b)
    rating_a_new = rating_a + k * (score_a - expected_score_a)
    rating_b_new = rating_b + k * ((1 - score_a) - (1 - expected_score_a))
    
    return rating_a_new, rating_b_new