class Twitter:

    def __init__(self):
        # All indexed by a user id lol???
        self.users = collections.defaultdict(list)
        self.user_following = collections.defaultdict(list)
        self.tweets = collections.defaultdict(list)
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # post a tweet
        self.tweets[userId].append((self.clock, tweetId))
        self.clock -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # 10 most recent tweets - most likely a prio q.
        # we assign an array to each user and then heapify it as needed
        following = self.user_following[userId] # whom the user is following
        arr = []
        heap = []

        heap.extend(self.tweets[userId])
 
        # for each user followed, we want to parse their tweets and add them
        # to a big heap
        for user_followed in following: # 1 is currently querying 2
            # so it should be user tweets of themselves and then following
            heap.extend(self.tweets[user_followed])
       
        heapq.heapify(heap)
        print(heap)
        # go through all the followers and get the ones of the least prio
        new_count = 0
        while heap and new_count < 10:
            arr.append(heapq.heappop(heap)[1])
            new_count += 1
        return arr

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId in self.user_following[followerId]:
            return
        self.user_following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.user_following[followerId]:
            return
        self.user_following[followerId].remove(followeeId)
