# If..else
"""
destination= input("Which Airlines have you booked ?")

if destination=="ethiopia":
    print("transit point: Addis Ababa")
else:
    print("Transit point is unknown to me")
"""

# if..elif....else
"""
destination= input("Which Airlines have you booked ?")

if destination=="ethiopia":
    print("transit point: Addis Ababa")
elif destination=='emirates':
    print("transit point: Dubai")
elif destination=='qatar':
    print("transit point: Doha")
else:
    print("Transit point is unknown to me")
"""
# Nested if...

airlines= input("Which Airlines have you booked ?")
place= input("Which Place you are going")

final_dest = lambda p: print(f"final destination:{p}")
wrong_dest= lambda w: print("NO such destination through this airlines")

if airlines=="ethiopia":
    if place=="Addis Ababa":
        final_dest(place)
    elif place == 'Dubai':
        wrong_dest()
    else:
        print("transit point: Addis ababa")
        final_dest(place)

elif airlines == 'emirates':
    if place == 'Addis Ababa':
        wrong_dest()
    elif place == 'Dubai':
        final_dest(place)
    else:
        print("Transit point: Dubai")
        final_dest(place)
else:
   print("No info for this airlines")

