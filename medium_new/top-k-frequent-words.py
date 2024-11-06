class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # https://leetcode.com/problems/top-k-frequent-words/
        # time complexity O(n + klogn) space O(n)

        # Create an harshtable with words and its frequency
        from collections import defaultdict
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        
        # Use heap to pop the k largest (most frequent words)
        import heapq
        count_word = []
        for word, count in freq.items():
            count_word.append((-count, word))
        heapq.heapify(count_word)

        ans = [] 
        for i in range(k):
            count, word = heapq.heappop(count_word)
            ans.append(word)
        
        return ans