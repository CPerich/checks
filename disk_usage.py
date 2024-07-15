#!/usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absloute, min_percemt):
    """Returns True if there is enough free disk space, false otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gygabites
    gygabites_free = du.free / 2**30
    if percent_free < min_percent or gygabites_free < min_absloute
        return False
    return True

# Check for at leat 2 GB and 10% free
if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")
    sys.exit(1)
    
    print(Everythin: OK )
    sys.exit(0)
    