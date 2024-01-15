from math import sin, asin, acos, degrees, sqrt, radians

ANGLE_C = 90  # Angle C will always be considered 90 degrees
triangle_types = ["SAS", "AAS", "ASA", "SSS", "SAA"]
cannot_solve = ["ASS", "AAA", "SSA"]
possible_side_combos = ["AB", "AC", "BC"]
possible_angle_combos = ["ac", "bc", "ab"]


# Runs the main program
def run():
    triangle_type = determine_type()
    match triangle_type:
        case "SSS":
            side_a, side_b, side_c, angle_a, angle_b = get_info(triangle_type)
            print(
                f"Side A is {side_a}, side B is {side_b}, Side C is {side_c}, angle a is {angle_a}, angle b is {angle_b}"
                f", angle c is {ANGLE_C}")
        case "SAS":
            side_a, side_b, side_c, angle_a, angle_b = get_info(triangle_type)
            print(
                f"Side A is {side_a}, side B is {side_b}, Side C is {side_c}, angle a is {angle_a}, angle b is {angle_b}"
                f", angle c is {ANGLE_C}")
        case "AAS":
            side_a, side_b, side_c, angle_a, angle_b = get_info(triangle_type)
            print(
                f"Side A is {side_a}, side B is {side_b}, Side C is {side_c}, angle a is {angle_a}, angle b is {angle_b}"
                f", angle c is {ANGLE_C}")
        case "ASA":
            side_a, side_b, side_c, angle_a, angle_b = get_info(triangle_type)
            print(
                f"Side A is {side_a}, side B is {side_b}, Side C is {side_c}, angle a is {angle_a}, angle b is {angle_b}"
                f", angle c is {ANGLE_C}")


# Determines the type of triangle and whether it is solvable by my program
def determine_type():
    while True:
        config = input("What type of triangle(SAS, AAS/SAA, ASA, SSS) do you have: ")
        config = config.upper()
        if config in cannot_solve:
            print("Not solvable")
            continue
        if config not in triangle_types:
            print("Input not valid")
            continue
        if config == "AAS" or config == "SAA":
            config = "AAS"
        return config


# Figures out what kind angles and sides are known of the inputted triangle type and returns the missing pieces
def get_info(triangle_type):
    match triangle_type:
        case "SSS":
            while True:
                side_a, side_b, side_c, angle_a, angle_b = info_SSS()
                if not check_triangle_valid(side_a, side_b, side_c):
                    print("Invalid Triangle: Impossible Side Lengths")
                    continue
                return side_a, side_b, side_c, angle_a, angle_b
        case "SAS":
            while True:
                known_sides = input("What sides(AB, AC, BC) are known: ")
                known_sides = known_sides.upper()
                if not known_sides in possible_side_combos:
                    print("Not Side Possible Combo")
                    continue
                match known_sides:
                    case "AB":
                        side_a, side_b, side_c, angle_a, angle_b = info_SAS("AB")
                        return side_a, side_b, side_c, angle_a, angle_b
                    case "AC":
                        side_a, side_b, side_c, angle_a, angle_b = info_SAS("AC")
                        return side_a, side_b, side_c, angle_a, angle_b
                    case "BC":
                        side_a, side_b, side_c, angle_a, angle_b = info_SAS("BC")
                        return side_a, side_b, side_c, angle_a, angle_b
        case "AAS":
            while True:
                known_angles = input("What angles(ac, bc, ab) are known: ")
                if not known_angles.lower() in possible_angle_combos:
                    print("Not Possible Angle Combo")
                    continue
                match known_angles:
                    case "ac":
                        side_a, side_b, side_c, angle_a, angle_b = info_AAS("ac")
                        return side_a, side_b, side_c, angle_a, angle_b
                    case "bc":
                        side_a, side_b, side_c, angle_a, angle_b = info_AAS("bc")
                        return side_a, side_b, side_c, angle_a, angle_b
                    case "ab":
                        side_a, side_b, side_c, angle_a, angle_b = info_AAS("ab")
                        return side_a, side_b, side_c, angle_a, angle_b
        case "ASA":
            while True:
                known_angles = input("What angles(ac, bc, ab) are known: ")
                if not known_angles.lower() in possible_angle_combos:
                    print("Not Possible Angle Combo")
                    continue
                match known_angles:
                    case "ac":
                        side_a, side_b, side_c, angle_a, angle_b = info_ASA("ac")
                        return side_a, side_b, side_c, angle_a, angle_b
                    case "bc":
                        side_a, side_b, side_c, angle_a, angle_b = info_ASA("bc")
                        return side_a, side_b, side_c, angle_a, angle_b
                    case "ab":
                        side_a, side_b, side_c, angle_a, angle_b = info_ASA("ab")
                        return side_a, side_b, side_c, angle_a, angle_b


# Uses the pythagorean theorem to find one of the missing sides
def pythagorean_theorem(side_1, side_2, hypotenuse_known):
    if not hypotenuse_known:
        return round(sqrt(((side_1 ** 2) + (side_2 ** 2))), 2)
    return round(sqrt(((side_2 ** 2) - (side_1 ** 2))), 2)


# Uses arcsin to find the angles in an AAS triangles
def SAS(side_a, side_b, side_c):
    angle_a = asin((side_a / side_c))
    angle_b = asin(side_b / side_c)
    angle_a, angle_b = degrees(angle_a), degrees(angle_b)
    return round(angle_a, 2), round(angle_b, 2)


# Uses sin and the pythagorean theorem to find the sides in an AAS triangles
def AAS(side_1, angle_1, side_c_known):
    if side_c_known:
        return_side_1 = (side_1 * (sin(radians(angle_1))))
        return_side_2 = sqrt(((side_1 ** 2) - (return_side_1 ** 2)))
    else:
        return_side_1 = (side_1 / (sin(radians(angle_1))))
        return_side_2 = sqrt(((return_side_1 ** 2) - (side_1 ** 2)))
    return round(return_side_2, 2), round(return_side_1, 2)


# Uses sin to find the angles and sides in an ASA triangles
def ASA(angle_1, side_1, hypotenuse_known):
    if hypotenuse_known:
        return_valued = side_1 * sin(radians(angle_1))
    else:
        return_valued = (side_1 / (sin(radians(angle_1))))
    return round(return_valued, 2)


# Uses the law of cosines to find the angles in an SSS triangles
def SSS(side_a, side_b, side_c):
    angle_b = acos(((side_a ** 2) + (side_c ** 2) - (side_b ** 2)) / (2 * side_c * side_a))
    angle_a = acos(((side_b ** 2) + (side_c ** 2) - (side_a ** 2)) / (2 * side_b * side_c))
    angle_a, angle_b = degrees(angle_a), degrees(angle_b)
    return round(angle_a, 2), round(angle_b, 2)


# Determines the missing angle in a triangle by using the sum of triangle angles formula
def sum_of_angles(angle_1, angle_2):
    angle_3 = 180 - (angle_1 + angle_2)
    return round(angle_3, 2)


# Checks if triangle is possible by checking the side lengths
def check_triangle_valid(side_1, side_2, side_3):
    if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
        return True
    return False


# Gets the side lengths of the SSS triangle
def info_SSS():
    while True:
        side_a = input("Side A length: ")
        side_b = input("Side B length: ")
        side_c = input("Side C length: ")
        side_a, side_b, side_c = float(side_a), float(side_b), float(side_c)
        if not check_triangle_valid(side_a, side_b, side_c):
            print("Invalid Triangle: Impossible Side Lengths")
            continue
        angle_a, angle_b = SSS(side_a, side_b, side_c)
        return side_a, side_b, side_c, angle_a, angle_b


# Gets the side lengths and angles of the SAS triangle
def info_SAS(known_sides):
    match known_sides:
        case "AB":
            side_a = input("Input side A: ")
            side_b = input("Input side B: ")
            side_a, side_b = float(side_a), float(side_b)
            side_c = pythagorean_theorem(side_a, side_b, False)
            angle_a, angle_b = SAS(side_a, side_b, side_c)
            return side_a, side_b, side_c, angle_a, angle_b
        case "BC":
            side_b = input("Input side B: ")
            side_c = input("Input side C: ")
            angle_a = input("Input angle a: ")
            side_b, side_c = float(side_b), float(side_c)
            side_a = pythagorean_theorem(side_b, side_c, True)
            angle_a, angle_b = SAS(side_a, side_b, side_c)
            return side_a, side_b, side_c, angle_a, angle_b
        case "AC":
            side_a = input("Input side A: ")
            side_c = input("Input side C: ")
            angle_b = input("Input angle b: ")
            side_a, side_c = float(side_a), float(side_c)
            side_b = pythagorean_theorem(side_a, side_c, True)
            angle_a, angle_b = SAS(side_a, side_b, side_c)
            return side_a, side_b, side_c, angle_a, angle_b


# Gets the side lengths and angles of the AAS triangle
def info_AAS(known_angles):
    match known_angles:
        case "ac":
            angle_a = input("What is angle a: ")
            angle_a = float(angle_a)
            while True:
                known_side = input("Which side is known: ")
                if known_side.upper() == "C":
                    side_c = input("What is the length of side C: ")
                    side_c = float(side_c)
                    side_b, side_a = AAS(side_c, angle_a, True)
                elif known_side.upper() == "A":
                    side_a = input("What is the length of side A: ")
                    side_a = float(side_a)
                    side_c, side_b = AAS(side_a, angle_a, False)
                else:
                    print("Not Possible Known Side")
                    continue
                angle_b = sum_of_angles(angle_a, ANGLE_C)
                return side_a, side_b, side_c, angle_a, angle_b
        case "bc":
            angle_b = input("What is angle b: ")
            angle_b = float(angle_b)
            while True:
                known_side = input("Which side is known: ")
                if known_side.upper() == "C":
                    side_c = input("What is the length of side C: ")
                    side_c = float(side_c)
                    side_a, side_b = AAS(side_c, angle_b, True)
                elif known_side.upper() == "B":
                    side_b = input("What is the length of side B: ")
                    side_b = float(side_b)
                    side_a, side_c = AAS(side_b, angle_b, False)
                else:
                    print("Not Possible Known Side")
                    continue
                angle_a = sum_of_angles(angle_b, ANGLE_C)
                return side_a, side_b, side_c, angle_a, angle_b
        case "ab":
            known_angle = input("What angle is known: ")
            if known_angle.upper() == 'B':
                angle_b = input("What is angle b: ")
                angle_b = float(angle_b)
                angle_a = sum_of_angles(angle_b, ANGLE_C)
                while True:
                    known_side = input("Which side is known: ")
                    if known_side.upper() == "A":
                        side_a = input("What is the length of side A: ")
                        side_a = float(side_a)
                        side_b, side_c = AAS(side_a, angle_a, False)
                    elif known_side.upper() == "B":
                        side_b = input("What is the length of side B: ")
                        side_b = float(side_b)
                        side_a, side_c = AAS(side_b, angle_b, False)
                    else:
                        print("Not Possible Known Side")
                        continue
                    return side_a, side_b, side_c, angle_a, angle_b
            else:
                angle_a = input("What is angle a: ")
                angle_a = float(angle_a)
                angle_b = sum_of_angles(angle_a, ANGLE_C)
                while True:
                    known_side = input("Which side is known: ")
                    if known_side.upper() == "A":
                        side_a = input("What is the length of side A: ")
                        side_a = float(side_a)
                        side_b, side_c = AAS(side_a, angle_a, False)
                    elif known_side.upper() == "B":
                        side_b = input("What is the length of side B: ")
                        side_b = float(side_b)
                        side_a, side_c = AAS(side_b, angle_b, False)
                    else:
                        print("Not Possible Known Side")
                        continue
                    angle_a = sum_of_angles(angle_b, ANGLE_C)
                    return side_a, side_b, side_c, angle_a, angle_b


# Gets the side lengths and angles of the ASA triangle
def info_ASA(known_angles):
    match known_angles:
        case "ab":
            angle_a = input("Input angle a: ")
            angle_b = input("Input angle b: ")
            side_c = input("Input side C: ")
            angle_a, angle_b, side_c = float(angle_a), float(angle_b), float(side_c)
            side_a = ASA(angle_a, side_c, True)
            side_b = pythagorean_theorem(side_a, side_c, True)
            return side_a, side_b, side_c, angle_a, angle_b
        case "bc":
            angle_b = input("Input angle b: ")
            side_a = input("Input side A: ")
            angle_b, side_a = float(angle_b), float(side_a)
            angle_a = sum_of_angles(angle_b, ANGLE_C)
            side_c = ASA(angle_a, side_a, False)
            side_b = pythagorean_theorem(side_a, side_c, True)
            return side_a, side_b, side_c, angle_a, angle_b
        case "ac":
            angle_a = input("Input angle a: ")
            side_b = input("Input side B: ")
            angle_a, side_b = float(angle_a), float(side_b)
            angle_b = sum_of_angles(angle_a, ANGLE_C)
            side_c = ASA(angle_b, side_b, False)
            side_a = pythagorean_theorem(side_b, side_c, True)
            return side_a, side_b, side_c, angle_a, angle_b


# Runs the program
if __name__ == '__main__':
    run()
