
import math

def get_memory_steps(n):

    layer_max_values = []
    layer_size = []

    # populate layer max values
    current_value = -1
    while current_value <= math.sqrt(n):
        current_value = current_value + 2
        layer_size.append(current_value)
        layer_max_values.append(current_value * current_value)

    layer = 0
    for value in layer_max_values:
        if value < n:
            layer = layer + 1

    layer_mid_points = [math.ceil(layer_max_values[layer] - layer_size[layer] / 2) - (layer_size[layer] - 1) * x for x
                        in range(0, 4)]

    distance_to_face_mid_point = [abs(n - mid_point) for mid_point in layer_mid_points]

    return min(distance_to_face_mid_point) + layer


if __name__ == "__main__":

    n = 265149

    #n = 26

    print(get_memory_steps(n))
