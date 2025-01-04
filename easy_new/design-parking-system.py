class ParkingSystem:
    # https://leetcode.com/problems/design-parking-system/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
    
    def __init__(self, big: int, medium: int, small: int):
        self.park = [0,0,0,0]
        self.park[1] = big
        self.park[2] = medium
        self.park[3] = small

    def addCar(self, carType: int) -> bool:
        if self.park[carType] > 0:
            self.park[carType] -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)