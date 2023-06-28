class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #initializing
        sell=0
        hold=-math.inf
        prev=0
        #running loop
        for x in prices:
            cache=sell
            sell=max(sell, hold+x)
            hold=max(hold,prev-x)

            prev = cache
        #returning the value
        return sell
