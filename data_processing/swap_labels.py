import os

new_dct = {
    0: 0, #"Aluminium foil",
    1: 2, #"Battery",
    2: 0, #"Blister pack",
    3: 0, #"Blister pack",
    4: 0, #"plastic Bottle",
    5: 0, #"plastic Bottle", ?? is this glass bottle or plastic bottle finally
    6: 3, #"glass Bottle",
    7: 0, #"metal Bottle cap",
    8: 0, #"plastic Bottle cap",
    9: 3, #"Broken glass",
    10: 0, #"Can",
    11: 0,
    12: 0,
    13: 1,
    14: 1,
    15: 1,
    16: 1,
    17: 1,
    18: 1,
    19: 1,
    20: 1,
    21: 0,
    22: 0,
    23: 3,
    24: 0,
    25: 4,
    26: 3,
    27: 0,
    28: 0,
    29: 0,
    30: 1,
    31: 1,
    32: 1,
    33: 1,
    34: 1,
    35: 1,
    36: 0,
    37: 0,
    38: 0,
    39: 0,
    40: 0,
    41: 0,
    42: 0,
    43: 0,
    44: 0,
    45: 0,
    46: 0,
    47: 0,
    48: 0,
    49: 0,
    50: 0,
    51: 5,
    52: 0,
    53: 5,
    54: 0,
    55: 0,
    56: 1,
    57: 1,
    58: 5,
    59: 5,
}

dct_xxxx = {
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
output_xxx = {
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
            #tmp = dct[old_class]
            new_class = new_dct[old_class]
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