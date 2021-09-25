#!/usr/bin/python
import os, sys
import park

class Parkinglotcheck(object):
    def __init__(self):
        self.parking_lot = park.Park()

    def check_file(self, input_file):
        if not os.path.exists(input_file):
            print("Given f %s does not exist" % input_file)

        f = open(input_file)
        try:
            while True:
                l = next(f)
                if l.endswith('\n'): l = l[:-1]
                if l == '': continue
                self.process_command(l)
        except StopIteration:
            f.close()
        except Exception as ex:
            print("Error occured while processing f %s" % ex)

    def process_input(self):
        try:
            while True:
                input_in = input("Enter the command: ")
                self.process_command(input_in)
        except (KeyboardInterrupt, sys.exit()):
            return
        except Exception as ex:
            print("Error occured while processing the input %s" % ex)


    def process_command(self, input_in):
        input_to = input_in.split()
        command = input_to[0]
        params = input_to[1:]
        if hasattr(self.parking_lot, command):
            command_function = getattr(self.parking_lot, command)
            command_function(*params)
        else:
            print("Got wrong command.")


if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 1:
        command = Parkinglotcheck()
        command.process_input()
    elif len(arg) == 2:
        command = Parkinglotcheck()
        command.check_file(arg[1])
    else:
        print("Wrong number of arguments.\n" \
         "Usage:\n" \
         "./parkinglot.py <filename> OR \n" \
         "./parkinglot.py")

