import pygame

def colision_detection(moving_car, static_upper_car: list, static_lower_car: list):
    

    all_parked_veh = static_upper_car + static_lower_car

    for parked_car in all_parked_veh:
        colision = col_between_2(moving_car, parked_car)
        if colision == True:
            return True
    return False
    

def SAT_projection(axis, corners):
    min_value = float('inf')
    max_value = float('-inf')

    for i in range(0    , len(corners)):
        proj = axis.dot(corners[i])
        if proj < min_value:
            min_value = proj
        if proj > max_value:
            max_value = proj

    return min_value, max_value

def get_axes(car):
    axes = []
    
    corners = car["rogi"]

    lenghwise_axis = corners[1] - corners[2]
    widthwise_axis = corners[1] - corners[0]

    SAT_axis_length = lenghwise_axis.normalize()
    SAT_axis_width = widthwise_axis.normalize()

    axes.append(SAT_axis_length)
    axes.append(SAT_axis_width)
    
    return axes

def col_between_2(car_a, car_b):

    SAT_axes_A = get_axes(car_a)
    SAT_axes_B = get_axes(car_b)

    SAT_axes = SAT_axes_A + SAT_axes_B 

    rogi_A = car_a["rogi"]
    rogi_B = car_b["rogi"]

    for axis in SAT_axes:
        min_a, max_a = SAT_projection(axis, rogi_A)
        min_b, max_b = SAT_projection(axis, rogi_B)

        if max_a < min_b or max_b < min_a:
            return False
    return True


#def get_line_eqation(p_1, p_2):
    
    # Wzor ogolny prostej: Ax + By + C = 0

    #A = p_2.y - p_1.y
    #B = p_2.x - p_1.x
    #C = -(A * p_1.x) - (B * p_1.y)

    #return A, B, C