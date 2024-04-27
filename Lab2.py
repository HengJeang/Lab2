print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu():
    print("Enter some numbers separated by commas (e.g., 5, 67, 32)")

def get_user_input():
    print("Enter numbers:")
    numbers= input()
    numbers = [float(x) for x in numbers.split(",")]
    return numbers

def calc_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    print("Average =", average)
    return average

def find_min_max(numbers):
    max_temp = max(numbers)
    min_temp = min(numbers)
    print("Maximum:", max_temp)
    print("Minimum:", min_temp)
    return max_temp, min_temp

def sort_temperature(numbers):
    sorted_temp = sorted(numbers)
    print("Sorted temperatures:", sorted_temp)
    return sorted_temp

def calc_median_temperature(numbers): 
    sorted_temperatures = sorted(numbers)
    length = len(sorted_temperatures)

    if length % 2 == 0:
        median_temperature = (sorted_temperatures[length//2 - 1] + sorted_temperatures[length//2]) / 2
    else:
        median_temperature = sorted_temperatures[length//2]

    print("Median temperature:", str(median_temperature))
    return median_temperature

def main():
    display_main_menu()
    numbers = get_user_input()
    calc_average(numbers)
    find_min_max(numbers)
    sorted_temperature = sort_temperature(numbers)
    calc_median_temperature(sorted_temperature)

if __name__ == "__main__":
    main()







    
    