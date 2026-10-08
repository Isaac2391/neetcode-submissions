class Twitter:

    def __init__(self):

        self.count = 0 
        self.tweetMap = defaultdict(list) 
        self.followMap = defaultdict(set)

        # use default dict so you dont have to initialise new lists/sets 
        # every time you want to add collections ( lists, sets) as values
        # to a dict entry 
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # minus 1 because we're using a minheap

    def getNewsFeed(self, userId: int) -> List[int]:

        result = []
        minheap = [] 

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap,[count, tweetId, followeeId, index - 1])

            heapq.heapify(minheap)

        while minheap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            result.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
