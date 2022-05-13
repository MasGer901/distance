from math import radians, cos, sin, asin, sqrt


def create_lo_la(coordinates):
    Lo1 = float(coordinates[0])
    La1 = float(coordinates[1])
    La2 = 55.898947
    Lo2= 37.632206
    return distance_1(La1, La2, Lo1, Lo2)


def distance_1(La1, La2, Lo1, Lo2):
    # The math module contains the function name "radians" which is used for converting the degrees value into radians.
    Lo1 = radians(Lo1)
    Lo2 = radians(Lo2)
    La1 = radians(La1)
    La2 = radians(La2)

    # Using the "Haversine formula"
    D_Lo = Lo2 - Lo1
    D_La = La2 - La1
    P = sin(D_La / 2) ** 2 + cos(La1) * cos(La2) * sin(D_Lo / 2) ** 2

    Q = 2 * asin(sqrt(P))

    # The radius of earth in kilometres.
    R_km = 6371
    distance = round(Q * R_km)
    # Then, we will calculate the result
    return distance

