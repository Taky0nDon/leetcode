class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the longest sequence of unique characters.
        When s is an empty string, return 0
        Two pointers
            - index 0 (L)
            - index 1 (R)
        Capture substring starting at L and ending at index R - 1.
        Problem with this approach: could miss longest substring if it includes part of the
        previous substring.
        Instead, slide the window one char at a time until it is only unique chars again, then
        resume expanding rightward. Use a hashmap to keep track of character counts.
        Can use a hash set to determine whether characters are repeated. (O1 look ups)
        When R == len(s), it's over.
        """
        l = 0
        r = 0
        sublength = len(s)
        maxlength = 0
        char_counts = defaultdict(int)
        while r < len(s):
            char_counts[s[r]] += 1
            while char_counts[s[r]] > 1:
                char_counts[s[l]] -= 1
                l += 1
            sublength = r - l + 1
            maxlength = max(sublength, maxlength)
            r += 1
        return maxlength
