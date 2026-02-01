"""
3829. Design Ride Sharing System - Medium


A ride sharing system manages ride requests from riders and availability from drivers. Riders request rides, and drivers become available over time. The system should match riders and drivers in the order they arrive.

Implement the RideSharingSystem class:

 - ideSharingSystem() Initializes the system.

 - oid addRider(int riderId) Adds a new rider with the given riderId.

 - oid addDriver(int driverId) Adds a new driver with the given driverId.

 - nt[] matchDriverWithRider() Matches the earliest available driver with the earliest waiting rider and removes both of them from the system. Returns an integer array of size 2 where result = [driverId, riderId] if a match is made. If no match is available, returns [-1, -1].

 - oid cancelRider(int riderId) Cancels the ride request of the rider with the given riderId if the rider exists and has not yet been matched.



Example 1:

Input:
["RideSharingSystem", "addRider", "addDriver", "addRider", "matchDriverWithRider", "addDriver", "cancelRider", "matchDriverWithRider", "matchDriverWithRider"]
[[], [3], [2], [1], [], [5], [3], [], []]

Output:
[None, None, None, None, [2, 3], None, None, [5, 1], [-1, -1]]

Explanation

RideSharingSystem rideSharingSystem = new RideSharingSystem(); // Initializes the system
rideSharingSystem.addRider(3); // rider 3 joins the queue
rideSharingSystem.addDriver(2); // driver 2 joins the queue
rideSharingSystem.addRider(1); // rider 1 joins the queue
rideSharingSystem.matchDriverWithRider(); // returns [2, 3]
rideSharingSystem.addDriver(5); // driver 5 becomes available
rideSharingSystem.cancelRider(3); // rider 3 is already matched, cancel has no effect
rideSharingSystem.matchDriverWithRider(); // returns [5, 1]
rideSharingSystem.matchDriverWithRider(); // returns [-1, -1]


Example 2:

Input:
["RideSharingSystem", "addRider", "addDriver", "addDriver", "matchDriverWithRider", "addRider", "cancelRider", "matchDriverWithRider"]
[[], [8], [8], [6], [], [2], [2], []]

Output:
[None, None, None, None, [8, 8], None, None, [-1, -1]]

Explanation

RideSharingSystem rideSharingSystem = new RideSharingSystem(); // Initializes the system
rideSharingSystem.addRider(8); // rider 8 joins the queue
rideSharingSystem.addDriver(8); // driver 8 joins the queue
rideSharingSystem.addDriver(6); // driver 6 joins the queue
rideSharingSystem.matchDriverWithRider(); // returns [8, 8]
rideSharingSystem.addRider(2); // rider 2 joins the queue
rideSharingSystem.cancelRider(2); // rider 2 cancels
rideSharingSystem.matchDriverWithRider(); // returns [-1, -1]



Constraints:

1 <= riderId, driverId <= 1000
Each riderId is unique among riders and is added at most once.
Each driverId is unique among drivers and is added at most once.
At most 1000 calls will be made in total to addRider, addDriver, matchDriverWithRider, and cancelRider.
"""

from typing import List
from collections import deque


class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.rider_st = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.rider_st.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] not in self.rider_st:
            self.riders.popleft()
        
        if not self.riders or not self.drivers:
            return [-1, -1]

        rider = self.riders.popleft()
        driver = self.drivers.popleft()
        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rider_st:
            self.rider_st.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)


def test(calls, prams):
    ride_sharing_system = None
    res = []

    for call, param in zip(calls, prams):
        if call == "RideSharingSystem":
            ride_sharing_system = RideSharingSystem()
            res.append(None)
        elif call == "addRider":
            ride_sharing_system.addRider(param[0])
            res.append(None)
        elif call == "addDriver":
            ride_sharing_system.addDriver(param[0])
            res.append(None)
        elif call == "matchDriverWithRider":
            res.append(ride_sharing_system.matchDriverWithRider())
        elif call == "cancelRider":
            ride_sharing_system.cancelRider(param[0])
            res.append(None)

    return res


if __name__ == "__main__":
    # Example 1
    calls_1 = ["RideSharingSystem", "addRider", "addDriver", "addRider", "matchDriverWithRider", "addDriver", "cancelRider", "matchDriverWithRider", "matchDriverWithRider"]
    prams_1 = [[], [3], [2], [1], [], [5], [3], [], []]

    print(test(calls_1, prams_1))  # [None, None, None, None, [2, 3], None, None, [5, 1], [-1, -1]]

    # Example 2
    calls_2 = ["RideSharingSystem", "addRider", "addDriver", "addDriver", "matchDriverWithRider", "addRider", "cancelRider", "matchDriverWithRider"]
    prams_2 = [[], [8], [8], [6], [], [2], [2], []]

    print(test(calls_2, prams_2))  # [None, None, [8, 8], None, None, [-1, -1]]

