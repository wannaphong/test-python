import glob
import os
import pathlib

print("check all students")


def list_students(path_store="../students"):
    students = list(glob.glob(os.path.join(path_store,"*")))
    return students