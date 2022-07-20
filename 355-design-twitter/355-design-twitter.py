class Twitter:

    def __init__(self):
        self.tweet_stack = []
        self.following_dict = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_stack.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.tweet_stack) - 1, -1 , -1):
            if (self.following_dict.get(userId) is not None and self.tweet_stack[i][0] in self.following_dict[userId]) or self.tweet_stack[i][0] == userId:
                res.append(self.tweet_stack[i][1])
            if len(res) >= 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.following_dict.get(followerId) is None:
            self.following_dict[followerId] = []
        if followeeId not in self.following_dict[followerId]:
            self.following_dict[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following_dict.get(followerId) is not None:
            self.following_dict[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)