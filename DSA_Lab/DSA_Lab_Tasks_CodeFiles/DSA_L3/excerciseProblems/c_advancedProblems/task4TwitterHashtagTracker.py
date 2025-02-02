class HashtagTracker:
    def __init__(self):
        self.hashtags = {}

    def add_tweet(self, tweet):
        words = tweet.split()
        for word in words:
            if word.startswith("#"):
                self.hashtags[word] = self.hashtags.get(word, 0) + 1

    def top_hashtags(self, top_n=3):
        sorted_hashtags = sorted(self.hashtags.items(), key=lambda x: x[1], reverse=True)
        return sorted_hashtags[:top_n]


# Example usage
hashtag_tracker = HashtagTracker()
hashtag_tracker.add_tweet("I love #Python programming")
hashtag_tracker.add_tweet("Learning #Python with fun")
hashtag_tracker.add_tweet("Hello #Java and #Python fans")

top_hashtags = hashtag_tracker.top_hashtags()
for tag, count in top_hashtags:
    print(f"{tag}: {count} times")
