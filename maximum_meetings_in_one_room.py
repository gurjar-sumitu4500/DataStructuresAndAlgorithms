class Solution:    
    def maximumMeetings(self, n, start, end):
        meetingIntervals = []
        for i in range(n):
            meetingIntervals.append([start[i], end[i]])
        meetingIntervals.sort(key=lambda x: x[1])
        lastMeeting = -1
        noOfMeetings = 0
        for i in meetingIntervals:
            if lastMeeting < i[0]:
                lastMeeting = i[1]
                noOfMeetings += 1
        return noOfMeetings
