class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        prev=0
        for i in range(len(gain)):
            next_alt = gain[i] + prev
            print(next_alt)
            max_altitude = max(max_altitude, next_alt)
            prev= next_alt
        return max_altitude

        