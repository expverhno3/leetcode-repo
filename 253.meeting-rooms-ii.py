class Solution:
    def minMeetingRooms(self, intervals):
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]

        starts.sort()
        ends.sort()

        rooms = 0
        end_ptr = 0

        for start in starts:
            if start < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1

        return rooms
