_score = 0


def reset_score():
    global _score
    _score = 0


def add_to_score(to_add):
    global _score
    _score += to_add

def get_score():
    return _score
