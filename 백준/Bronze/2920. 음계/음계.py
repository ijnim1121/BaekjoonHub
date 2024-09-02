melody = list(map(int, input().split()))

def distinction(melody):
    if sorted(melody) == melody:
        print("ascending")
    elif sorted(melody, reverse=True) == melody:
        print("descending")
    else:
        print("mixed")

distinction(melody)