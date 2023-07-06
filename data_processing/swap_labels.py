import os

dct = {
    0: "Aluminium foil",
    1: "Battery",
    2: "Blister pack",
    3: "Blister pack",
    4: "Bottle",
    5: "Bottle",
    6: "Bottle",
    7: "Bottle cap",
    8: "Bottle cap",
    9: "Broken glass",
    10: "Can",
    11: "Can",
    12: "Can",
    13: "Carton",
    14: "Carton",
    15: "Carton",
    16: "Carton",
    17: "Carton",
    18: "Carton",
    19: "Carton",
    20: "Cup",
    21: "Cup",
    22: "Cup",
    23: "Cup",
    24: "Cup",
    25: "Food waste",
    26: "Glass jar",
    27: "Lid",
    28: "Lid",
    29: "Other plastic",
    30: "Paper",
    31: "Paper",
    32: "Paper",
    33: "Paper",
    34: "Paper bag",
    35: "Paper bag",
    36: "Plastic bag & wrapper",
    37: "Plastic bag & wrapper",
    38: "Plastic bag & wrapper",
    39: "Plastic bag & wrapper",
    40: "Plastic bag & wrapper",
    41: "Plastic bag & wrapper",
    42: "Plastic bag & wrapper",
    43: "Plastic container",
    44: "Plastic container",
    45: "Plastic container",
    46: "Plastic container",
    47: "Plastic container",
    48: "Plastic glooves",
    49: "Plastic utensils",
    50: "Pop tab",
    51: "Rope & strings",
    52: "Scrap metal",
    53: "Shoe",
    54: "Squeezable tube",
    55: "Straw",
    56: "Straw",
    57: "Styrofoam piece",
    58: "Unlabeled litter",
    59: "Cigarette",
}
output = {
    "Aluminium foil" : 0,
    "Battery": 2,
    "Blister pack": 0,
    "Bottle": 3,
    "Bottle cap": 0,
    "Broken glass": 3,
    "Can": 0,
    "Carton": 1,
    "Cup": 5,
    "Food waste": 4,
    "Glass jar": 3,
    "Lid": 5,
    "Other plastic": 0,
    "Paper": 1,
    "Paper bag": 1,
    "Plastic bag & wrapper": 0,
    "Plastic container": 0,
    "Plastic glooves": 0,
    "Plastic utensils": 0,
    "Pop tab": 0,
    "Rope & strings": 5,
    "Scrap metal": 0,
    "Shoe": 5,
    "Squeezable tube": 0,
    "Straw": 4,
    "Styrofoam piece": 0,
    "Unlabeled litter": 5,
    "Cigarette": 5,    
}

def swap_labels_in_file(path, filename):
    new_lines = []
    with open(path+filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(" ")
            old_class = int(data[0])
            tmp = dct[old_class]
            new_class = output[tmp]
            new_line = str(new_class)
            data[0] = new_line
            new_lines.append(data)

    with open(path+filename, "w") as f:
        for line in new_lines:
            cnt = 0
            for l in line:
                if cnt < 4:
                    f.write(str(l) + " ")
                else:
                    f.write(str(l))
                cnt += 1

def swap_labels():
    all_filenames = os.listdir("output/labels")
    for filename in all_filenames:
        swap_labels_in_file("output/labels/", filename)
    
if __name__ == "__main__":
    swap_labels()