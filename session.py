import os
from pathlib import Path
import os


class PidFile:

    def __init__(self, pid_file):
        self.pid = str(os.getpid())
        tmp_folder = Path("tmp/")
        self.pid_file = tmp_folder / "main.pid"

    def create(self):
        with open(self.pid_file, 'w') as f:
            print(f)
            f.write(self.pid)

    def delete(self):
        os.unlink(self.pid_file)

    def check_if_exists(self):
        return os.path.isfile(self.pid_file)
