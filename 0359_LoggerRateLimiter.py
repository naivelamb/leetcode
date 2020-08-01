"""
https://leetcode.com/problems/logger-rate-limiter/
"""
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ref = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.ref:
            if timestamp - self.ref[message] >= 10:
                self.ref[message] = timestamp
                return True
            else:
                return False
        else:
            self.ref[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
