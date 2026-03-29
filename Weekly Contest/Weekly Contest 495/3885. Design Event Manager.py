"""
3885. Design Event Manager - Medium


You are given an initial list of events, where each event has a unique eventId and a priority.

Implement the EventManager class:

 - EventManager(int[][] events) Initializes the manager with the given events, where events[i] = [eventIdi, priority​​​​​​​i].

 - void updatePriority(int eventId, int newPriority) Updates the priority of the active event with id eventId to newPriority.

 - int pollHighest() Removes and returns the eventId of the active event with the highest priority. If multiple active events have the same priority, return the smallest eventId among them. If there are no active events, return -1.

An event is called active if it has not been removed by pollHighest().



Example 1:

Input:
["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]
[[[[5, 7], [2, 7], [9, 4]]], [], [9, 7], [], []]

Output:
[null, 2, null, 5, 9]

Explanation

EventManager eventManager = new EventManager([[5,7], [2,7], [9,4]]); // Initializes the manager with three events
eventManager.pollHighest(); // both events 5 and 2 have priority 7, so return the smaller id 2
eventManager.updatePriority(9, 7); // event 9 now has priority 7
eventManager.pollHighest(); // remaining highest priority events are 5 and 9, return 5
eventManager.pollHighest(); // return 9


Example 2:

Input:
["EventManager", "pollHighest", "pollHighest", "pollHighest"]
[[[[4, 1], [7, 2]]], [], [], []]

Output:
[null, 7, 4, -1]

Explanation

EventManager eventManager = new EventManager([[4,1], [7,2]]); // Initializes the manager with two events
eventManager.pollHighest(); // return 7
eventManager.pollHighest(); // return 4
eventManager.pollHighest(); // no events remain, return -1



Constraints:

1 <= events.length <= 10^5
events[i] = [eventId, priority]
1 <= eventId <= 10^9
1 <= priority <= 10^9
All the values of eventId in events are unique.
1 <= newPriority <= 10^9
For every call to updatePriority, eventId refers to an active event.
At most 105 calls in total will be made to updatePriority and pollHighest.
"""

from heapq import heapify, heappop, heappush


class EventManager:

    def __init__(self, events: list[list[int]]):
        self.events = [(-p, x) for x, p in events]
        self.priority = {x: p for x, p in events}
        heapify(self.events)

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.priority[eventId] = newPriority
        heappush(self.events, (-newPriority, eventId))

    def pollHighest(self) -> int:
        while self.events:
            p, i = heappop(self.events)
            if -p == self.priority[i]:
                self.priority[i] = 0
                return i
        return -1


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()


def test(calls, prams):
    event_manager = None
    res = []

    for call, param in zip(calls, prams):
        if call == "EventManager":
            event_manager = EventManager(param[0])
            res.append(None)
        elif call == "updatePriority":
            event_manager.updatePriority(param[0], param[1])
            res.append(None)
        elif call == "pollHighest":
            res.append(event_manager.pollHighest())

    return res


if __name__ == "__main__":
    # Example 1
    calls = ["EventManager", "updatePriority", "updatePriority", "pollHighest", "pollHighest"]
    prams = [[[[5, 7], [2, 7], [9, 4]]], [9, 7], [2, 6], [], []]

    print(test(calls, prams))  # [None, None, None, 5, 9]

    # Example 2
    calls = ["EventManager", "pollHighest", "pollHighest", "pollHighest"]
    prams = [[[[4, 1], [7, 2]]], [], [], []]

    print(test(calls, prams))  # [None, 7, 4, -1]
