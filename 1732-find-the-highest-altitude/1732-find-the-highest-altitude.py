class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        altitude_gain = 0
        for point in gain:
            altitude_gain += point
            if highest_altitude < altitude_gain:
                highest_altitude = altitude_gain
        return highest_altitude
        