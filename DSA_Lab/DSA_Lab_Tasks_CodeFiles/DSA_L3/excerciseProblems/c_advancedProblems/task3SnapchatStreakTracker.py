class StreakTracker:
    def __init__(self):
        self.streaks = {}

    def add_streak(self, user, streak_count):
        if user in self.streaks:
            self.streaks[user].append(streak_count)
        else:
            self.streaks[user] = [streak_count]

    def highest_streak(self):
        max_streak_user = None
        max_streak = 0
        for user, streak_list in self.streaks.items():
            highest = max(streak_list)
            if highest > max_streak:
                max_streak = highest
                max_streak_user = user
        return max_streak_user, max_streak


# Example usage
streak_tracker = StreakTracker()
streak_tracker.add_streak("User1", 5)
streak_tracker.add_streak("User1", 7)
streak_tracker.add_streak("User2", 8)
streak_tracker.add_streak("User2", 6)

user, streak = streak_tracker.highest_streak()
print(f"User with highest streak: {user} with a streak of {streak} days.")
