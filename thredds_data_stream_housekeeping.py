"""


"""

import os, time, sys
import os.path

MAX_FILE_AGE = int(os.getenv("MAX_FILE_AGE") or (24 * 60 * 60)) # In seconds
SLEEP_TIME = int(os.getenv("SLEEP_TIME") or (15 * 60)) # In seconds
PATH = os.getenv('DATA_DIR')
NOW = time.time()
exceptions = os.getenv("EXCEPTIONS").split(",") if os.getenv("EXCEPTIONS") else []

def main():
    files_to_check = [f for f in os.listdir(PATH) if f not in exceptions]
    print "Ignoring", exceptions
    for f in files_to_check:
        f = os.path.join(PATH, f)
        if os.stat(f).st_mtime < NOW - MAX_FILE_AGE:
            if os.path.isfile(f):
                file_to_remove = os.path.join(PATH, f)
                print "Removing", file_to_remove
                os.remove(file_to_remove)

    print "Done, sleeping for", SLEEP_TIME, "seconds"
    time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
