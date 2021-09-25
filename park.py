import slot_details, car_details

#This class contains details about parking slots as well as operation performed on parking are present here
class Park(object): 
    def __init__(self):
        self.slots = {}

    # This method will create parking lot if not present already with given number of slots.
    # Input: num_slots, Type-Integer 
    def Create_parking_lot(self, num_slots):
        num_slots = int(num_slots)
        if len(self.slots) > 0:
            print("Parking Lot has already been created")
            return
        if num_slots > 0:
            for i in range(1, num_slots+1):
                temp_slot = slot_details.Slot(slot_no=i, available=True)
                self.slots[i] = temp_slot
            print("Created parking of %s slots" % num_slots)
        else:
            print("Number of slots is wrong.")
        return
        
    #Method to find nearest available slot in parking
    def nearest_slot(self):
        # the available slots = slots
        slots = [i for i in list(self.slots.values()) if i.available]
        if not slots:
            return None
        return sorted(slots, key=lambda i: i.slot_no)[0]
        
    # Method to park a coming car in nearest available parking slot. If not present it will throw message.
    # Input: reg_no, age - Type is String
    def Park(self, reg_no, driver_age, age):  
        if not self.main_check():
            return
        #the exact available slot is check slot
        check_slot = self.nearest_slot()
        if check_slot:
            # Create car object and save in the available slot
            check_slot.car = car_details.Car.create(reg_no, age)
            check_slot.available = False
            print("Car with vehicle registration number ",reg_no," has been parked at slot number ",check_slot.slot_no)
        else:
            print("Sorry, parking lot is full.")

    # Method to empty a parking slot while car is leaving.
    #Input: slot_no ,Type-Integer
    def Leave(self, slot):
        slot = int(slot)
        if not self.main_check():
            return

        if slot in self.slots:
            p = self.slots[slot]
            if not p.available and p.car:
                p.car = None
                p.available = True
                print("Slot number",  slot," vacated, the car with vehicle registration number left the space, the driver of the car was of age ")
                # in the input file details were not provided
                # the car with vehicle registration number",car.reg_no, left the space, the driver of the car was of age ",car.age)
            else:
                print("There is no car is present at slot number %s" % slot)
        else:
            print("Sorry..! Slot number does not exist in parking lot.")

    # To show current status of parking
    def Status(self): 
        if not self.main_check():
            return
        print("Slot No\tRegistration No\tAge")
        for i in list(self.slots.values()):
            if not i.available and i.car:
                print("%s\t%s\t%s" % (i.slot_no, i.car.reg_no, i.car.age))

    def main_check(self):
        if len(self.slots) == 0:
            print("Parking Lot not created")
            return False
        return True

    # Function to find registration numbers of car with given age in parking
    # Input: age ,Type-String
    def Vehicle_registration_number_for_driver_of_age(self, age):
        if not self.main_check():
            return
        reg_nos = ''
        for p in list(self.slots.values()):
            if not p.available and p.car and \
                p.car.age == age:
                reg_nos += '%s ' % p.car.reg_no
        if reg_nos:
            print(reg_nos[:-1])
        else:
            print("NULL ") #Empty Space
          
    #Function to find slot numbers for cars with given age in parking.
    #Input: age, Type-String
    def Slot_numbers_for_driver_of_age(self, age):
        if not self.main_check():
            return
        slot_nos = ''
        for p in list(self.slots.values()):
            if not p.available and p.car and \
                p.car.age == age:
                slot_nos += '%s ' % p.slot_no
        if slot_nos:
            print(slot_nos[:-1])
        else:
            print("Not found")

    #Method to find slot numbers in parking with given registration number.
    # Input: reg_no, Type - String
    def Slot_number_for_car_with_number(self, reg_no):
        if not self.main_check():
            return
        slot = ''
        for p in list(self.slots.values()):
            if not p.available and p.car and \
                p.car.reg_no == reg_no:
                slot = p.slot_no
                break
        if slot:
            print(slot)
        else:
            print("Not found")