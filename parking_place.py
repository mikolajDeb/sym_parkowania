#Metodda falling edge z ktorej zerzygnowalem

from const import screen_height
import pygame, math

def find_place(intersection_points: list, Car):
    #pewne stale

    vector_right = pygame.math.Vector2(1, 0)
    vector_down = pygame.math.Vector2(0, 1)

    

    upper_points = []
    lower_points = []

    upper_reeding_angles = []
    lower_reeding_angles = []

    lower_edges_found = []
    upper_edges_found = []

    if len(intersection_points) == 0:

        return []
    
    else:
        

        #upper_reeding_angles = []
        #lower_reeding_angles = []

        #lower_edges_found = []
        #upper_edges_found = []
        #rozpakowanie chmury punktow na gore i dol
        

        distance_list = []

        for point in intersection_points:
            if point.y >= screen_height/2:
                lower_points.append(point)
                rel_vec = point - Car.lidar.lidar_pos
                current_angle = rel_vec.angle_to(vector_right)
                lower_reeding_angles.append(current_angle)
            else:
                upper_points.append(point)
                rel_vec = point - Car.lidar.lidar_pos
                current_angle = rel_vec.angle_to(vector_right)
                upper_reeding_angles.append(current_angle)

        lower_zip = zip(lower_reeding_angles, lower_points)
        upper_zip = zip(upper_reeding_angles, upper_points)

        lower_sorted = sorted(lower_zip)
        upper_sorted = sorted(upper_zip)

        # posortowane wzgledem kata od osi poziomej skierowanej w prawo

        if len(lower_sorted) > 0:
            sorted_lower_angles, sorted_lower_points = zip(*lower_sorted)
        else:
            sorted_lower_angles, sorted_lower_points = [], []

        if len(upper_sorted) > 0:
            sorted_upper_angles, sorted_upper_points = zip(*upper_sorted)
        else:
            sorted_upper_angles, sorted_upper_points = [], []
            
        

        


        #logika szukania miejsca          
        sensivity_margin = 1.5
        depth_thresh = 125
        gap_thresh = 50
        for p in range(1, len(sorted_lower_points)):
            #distance = sorted_lower_points[p-1] - sorted_lower_points[p]
            #dis_jump = distance.length()
            #distance_list.append(dis)

            dis_jump = sorted_lower_points[p].distance_to(sorted_lower_points[p-1])

            dist_to_sensor_curr = Car.lidar.lidar_pos.distance_to(sorted_lower_points[p])
            dist_to_sensor_prev = Car.lidar.lidar_pos.distance_to(sorted_lower_points[p-1]) 

            depth_jump = abs(dist_to_sensor_curr - dist_to_sensor_prev)
            #obliczenie dynamicznego progu 

            curr_pos = Car.lidar.lidar_pos
            dis_to_object = curr_pos.distance_to(sorted_lower_points[p - 1])

            Dyn_thersh = sensivity_margin * (dis_to_object * math.sin(math.radians(1)))

            if dis_jump > Dyn_thersh and depth_jump > depth_thresh:
                obstacle_edge = pygame.math.Vector2(sorted_lower_points[p].x,sorted_lower_points[p].y)
                lower_edges_found.append(obstacle_edge)
            else:
                avg_x = (sorted_lower_points[p-1].x + sorted_lower_points[p].x) / 2
                avg_y = (sorted_lower_points[p-1].y + sorted_lower_points[p].y) / 2
                continue


        for p in range(1, len(sorted_upper_points)):
            distance = sorted_upper_points[p-1] - sorted_upper_points[p]
            dis = distance.length()
            distance_list.append(dis)
            #obliczenie dynamicznego progu 

            curr_pos = Car.lidar.lidar_pos
            dis_to_object = curr_pos.distance_to(sorted_upper_points[p - 1])

            Dyn_thersh = sensivity_margin * (dis_to_object * math.sin(math.radians(Car.lidar.angle_between_rays)))

            if dis <= Dyn_thersh:
                continue
            else:
                avg_x = (sorted_upper_points[p-1].x + sorted_upper_points[p].x) / 2
                avg_y = (sorted_upper_points[p-1].y + sorted_upper_points[p].y) / 2
                obstacle_edge = pygame.math.Vector2(sorted_upper_points[p].x,sorted_upper_points[p].y)
                upper_edges_found.append(obstacle_edge)

    edges_found = upper_edges_found + lower_edges_found


    return edges_found

def parking_space_render(edges_found):
    
    for edge in edges_found:
        pygame.draw.circle(pygame.display.get_surface(), "green", (edge.x, edge.y), 10)

    
    pass


    
