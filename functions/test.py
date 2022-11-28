glb_name = "sally"
def change_name():
    global glb_name
    glb_name = "sammy"

change_name()
print(glb_name)
