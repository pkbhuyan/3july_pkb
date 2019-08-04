global_var1, global_var2 = "godfather", "godmother"


def relation():
    print(f"{global_var1} is called within relation", end='\n')
    local_var = "Grandson"
    print(f"{local_var} is called inside relation", end='\n')
    return


relation()

# print(f"{local_var} is called outside relation") # calling variable
# local to function gives error as not defined.
print(f"{global_var1} can be called anywhere")
