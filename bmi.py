def calculate_bmi(height, weight):
    print("Height= " +str(height))
    print("Weight=" +str(weight))

    bmi = weight/(height * height)
    print("BMI= " +str(bmi))

    if bmi > 25:
        ret_val = "Over weight", -1
      

    elif bmi >= 18.5 and bmi <= 25:
        ret_val = "Normal Weight", 0
  

    elif bmi < 18.5:
        ret_val = "Under Weight", 1

    return ret_val

def main():
    bmi_val = calculate_bmi(weight=57,height=1.73)  
    print(bmi_val) 

if __name__  == '__main__':
    main()