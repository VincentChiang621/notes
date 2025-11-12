class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)   # userID -> set() of following
        self.userPosts = defaultdict(list) # userID -> [[time, tID]] of tweets
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPosts[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # make a combined list of tweets based on userID and its follows (self.follows)
        tweets = self.userPosts[userId].copy()
        for user in self.follows[userId]:
            tweets += self.userPosts[user]

        heapq.heapify(tweets)
        i = 10
        res = []
        while i > 0 and len(tweets) > 0:
            i -= 1
            time, tweetId = heapq.heappop(tweets)
            res.append(tweetId)

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

