class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        print("--- BEGIN ---")
        # # pick up first item
        # self.swap_item()
        # print(f"helf item: {self._item}, positon: {self._position}")

        # # turn on light
        # self.set_light_on()
        # # while light is on ....

        # # keep moving right until you can't
        # while self.can_move_right():
        #     self.move_right()
            
        #     # if held is GREATER than in front, swap
        #     if self.compare_item() == 1:
        #         self.set_light_on
        #         self.swap_item()

        # # END of list, can't move right anymore
        # print("END of list")
        # print(f"helf item: {self._item}, positon: {self._position}")

        # # move all the way to the left until you can't
        # while self.can_move_left():
        #     self.move_left()

        # # START of list, can't move left anymore
        # print("START of list")
        # print(f"helf item: {self._item}, positon: {self._position}")

        # # Held item should be smallest item in list, so put back at postition 0
        # self.swap_item()
        # print(f"helf item: {self._item}, positon: {self._position}")

        # -------

        # if self.can_move_right:
        #     self.move_right
        #     # pick up item to right of postition 0, to start all over from next index
        #     self.swap_item

        # start
        # pick up first item
        # self.swap_item()
        # print(f"helf item: {self._item}, positon: {self._position}")

        # turn on light
        self.set_light_on()
        print("light ON")
        
        while self.light_is_on():
            print("Start Loop")

            print("RIGHT!")
            self.swap_item()

            self.set_light_off()
            print("light OFF")
            
            # keep going right until you can't
            while self.can_move_right():
                self.move_right()
                    
                # if held is GREATER than in front, swap
                if self.compare_item() == 0 or self.compare_item() == -1:
                    self.swap_item()
                    # print(f"helf item: {self._item}, positon: {self._position}")
                else:
                    self.set_light_on()
                    print("light ON")
        
            print("LEFT")
            self.swap_item()
            # print(f"helf item: {self._item}, positon: {self._position}")

            # keep going left until you cant'
            while self.can_move_left():
                self.move_left()
                # print(f"helf item: {self._item}, positon: {self._position}")

                if self.compare_item() is None or self.compare_item() > 0:
                    self.swap_item()
                    # print(f"helf item: {self._item}, positon: {self._position}")

        print("End Loop")
        
        # while self.light_is_on:
            # # keep going right until you can't
            # self.swap_item()
            # self.set_light_off()

            # while self.can_move_right():
            #     self.move_right()
                
            #     # if held is GREATER than in front, swap
            #     if self.compare_item() <= 0:
            #         self.swap_item()
            #     else:
            #         self.set_light_on()

            # self.swap_item()
            # # keep going left
            # while self.can_move_left():
            #     self.move_left()

            #     if self.compare_item() is None or self.compare_item() > 0:
            #         self.swap_item()

        # # move all the way to the left until you can't
        # while self.can_move_left():
        #     self.move_left()

        # #  keep doing until light is off
        # while self.light_is_on():
            
        #     self.set_light_off()

        #     # until you get to end, we have lowest as our held temp
        #     while self.can_move_right():
        #         self.move_right() # i += 0
        #         self.set_light_off()

        #         # go right, swap, then go back
        #         if self.can_move_right():
        #             self.move_right()
        #             self.swap_item()
        #             self.move_left()

        #         # if held (old next) is LESS than front
        #         if self.compare_item() == -1:
        #             self.swap_item()
        #             self.move_right()
        #             self.swap_item()
        #             self.set_light_on()


        # ------ Put first back
        # # END of list, can't move right anymore
        # print("END of list")
        # print(f"helf item: {self._item}, positon: {self._position}")

        # # move all the way to the left until you can't
        # while self.can_move_left():
        #     self.move_left()

        # # START of list, can't move left anymore
        # print("START of list")
        # print(f"helf item: {self._item}, positon: {self._position}")

        # # Held item should be smallest item in list, so put back at postition 0
        # self.swap_item()
        # print(f"helf item: {self._item}, positon: {self._position}")

        print("--- END ---")
        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    l = [2, 1, 3, 4, 5]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)