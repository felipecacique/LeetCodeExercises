class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # https://leetcode.com/problems/meeting-rooms-iii/
        # time O(mlogm+n)
        import heapq
        meetings = sorted(meetings, reverse=True)
        waitings = deque()
        availableRooms = [i for i in range(n)]
        heapq.heapify(availableRooms)
        happening = []
        time = 0
        count = {}
        maxMeetings = 0
        roomMaxMeeting = 0

        while meetings or waitings:
            # print(time, meetings, waitings, happening, availableRooms, count)
            # Get the meeting and add it to the waiting queue
            while meetings and time == meetings[-1][0]:
                waitings.append(meetings.pop())

            # Check if a meeting has already finished
            while happening and time >= happening[0][0]:
                meetingEnd, availableRoom, meetingStart = heapq.heappop(happening) # meeting has finished, so clear the room
                heapq.heappush(availableRooms, availableRoom) # since the room is empty, we put it back to the availableRooms

            # Get the available room with smallest index
            while waitings and availableRooms:
                meeting = waitings.popleft()
                availableRoom = heapq.heappop(availableRooms) # get the available room
                meetingStart = time if meeting[0] <= time else meeting[0]
                meetingEnd = meetingStart + (meeting[1] - meeting[0])
                heapq.heappush(happening, (meetingEnd, availableRoom, meetingStart)) # the meeting i is happening in the availableRoom

                # Saving the number of meeting per room and save the room with more meetings
                count[availableRoom] = count.get(availableRoom, 0) + 1
                if (count[availableRoom] > maxMeetings) or (count[availableRoom] == maxMeetings and availableRoom < roomMaxMeeting):
                    maxMeetings, roomMaxMeeting = count[availableRoom], availableRoom

            time += 1

            # We dont need to go over all possible minutes.We can skip to the time that matters, in which would trigger and event
            if meetings and happening: time = min(happening[0][0],meetings[-1][0])
            elif happening: time = happening[0][0]
            elif meetings: time = meetings[-1][0]

        return roomMaxMeeting
