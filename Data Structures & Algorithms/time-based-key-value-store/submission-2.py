class TimeMap:

    def __init__(self):
        self.holder = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.holder:
            self.holder[key] = []
        self.holder[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # Get the list of [value, time] pairs for this key
        values = self.holder.get(key, [])
        low = 0
        res = ''
        high = len(values) - 1
        while low <= high:
            mid = (low + high) // 2
            if values[mid][1] <= timestamp:
                # This is a valid candidate! Record the value string.
                res = values[mid][0]
                # But there might be a larger timestamp that's still <= target
                # So look to the right
                low = mid + 1
            else:
            # This timestamp is too large, look to the left
                high = mid - 1
        return res
timeMap = TimeMap()
timeMap.set("alice", "happy", 1)  
timeMap.get("alice", 1)           
timeMap.get("alice", 2)           
timeMap.set("alice", "sad", 3)  
timeMap.get("alice", 3)                
