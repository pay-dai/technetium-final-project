# Joseph Sandberg
# Function manages the time limit per round
# Gives the player warnings at certain amounts of time remaining

import time

def round_timer(time_limit, warning_times, real_time=False):
    """
    Runs the time limit per round of the language guessing game.

    Args:
        time_limit (int): Total amount of time (seconds) allowed per round.
        warning_times (list): When a player should receive a warning based on the time remaining.
        real_time (bool): If the timer should wait one real second between each countdown.

    Returns:
        dict: Information such as if the timer expired, warnings that occurred, and how much time is left.

    Raises:
        ValueError: If the time limit is less than 1.
    """

    if time_limit < 1:
        raise ValueError("The time limit must be at least 1 second!")

    time_remaining = time_limit
    warnings_triggered = []

    while time_remaining > 0:

        if time_remaining in warning_times:
            warnings_triggered.append(time_remaining)
            print("Warning: You have", time_remaining, "seconds remaining")

        if real_time:
            time.sleep(1)

        time_remaining -= 1

    return {
        "expired": True,
        "warnings_triggered": warnings_triggered,
        "time_remaining": time_remaining
    }
result = round_timer(300, [60, 30, 10])

print(result)