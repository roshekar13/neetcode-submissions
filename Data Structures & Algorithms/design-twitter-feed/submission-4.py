import heapq

class User(object):
    def __init__(self, uid):
        self.uid = uid
        self.following = {uid} # set
        self.tweets = [] # ordered list by default, we push tweets in chronolocal order and remove oldest

class Twitter:

    def __init__(self):
        self.users = {}
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create User class if new user posting
        if userId not in self.users: self.users[userId] = User(userId)

        # update User class with new tweet, pop earliest if >10
        curr_user = self.users[userId]
        curr_user.tweets.insert(0,(-self.timestamp,tweetId)) # pushing negative makes max heap, easier to getNewsFeed
        if len(curr_user.tweets) > 10: curr_user.tweets.pop()

        # update global timestamp
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # safety check: valid user
        if userId not in self.users: return []
        user = self.users[userId]
        followees = user.following

        # get top post from each user
        candidate_posts = [] # max-heap
        for idx in followees:
            if self.users[idx].tweets:
                timestamp, tweetId = self.users[idx].tweets[0]
                # (timestamp, userId, tweetId, nextIdx)
                # nextIdx to be used if we need more posts
                heapq.heappush(candidate_posts, (timestamp, idx, tweetId, 1))
        
        # populate feed, get most posts if needed
        feed = []
        while candidate_posts and len(feed) < 10:
            # add latest
            _, uid, tweetId, curr_idx = heapq.heappop(candidate_posts)
            feed.append(tweetId)
            
            # check if most recent user has more posts. If so, add to candidate heap
            if len(self.users[uid].tweets) > curr_idx:
                timestamp, tweetId = self.users[uid].tweets[curr_idx]
                heapq.heappush(candidate_posts, (timestamp, uid, tweetId, curr_idx+1))


        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        # add user to twitter has if new users
        if followerId not in self.users: self.users[followerId] = User(followerId)
        if followeeId not in self.users: self.users[followeeId] = User(followeeId)

        # safety check: double follow
        if followeeId in self.users[followerId].following: return

        # update following list
        self.users[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # safety check: unfollow called on unknown followee/follower
        if followeeId not in self.users or followerId not in self.users: return

        # safety check: follower doesnt currently follow followee
        curr_user = self.users[followerId]
        if followeeId not in curr_user.following: return

        # safety check: prevent self follow
        if followerId == followeeId: return

        # safety checks done- remove followee
        curr_user.following.remove(followeeId)






