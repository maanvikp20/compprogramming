# 6 kyu - Ho Ho Ho with Functions

def ho(ho_func=None):
    return "Ho" + (" " + ho_func if ho_func else "!")

print(ho(ho(ho(ho()))))
    