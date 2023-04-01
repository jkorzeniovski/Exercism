expected_bake_time = 40

def bake_time_remaining(elapsed_bake_time):
    return expected_bake_time - elapsed_bake_time

def preparation_time_in_mins(number_of_layers):
    return number_of_layers * 2

def elapsed_time_in_mins(number_of_layers, elapsed_bake_time):
    return preparation_time_in_mins(number_of_layers) + elapsed_bake_time


print(expected_bake_time)
print(bake_time_remaining(15))
print(preparation_time_in_mins(5))
print(elapsed_time_in_mins(5, 20))