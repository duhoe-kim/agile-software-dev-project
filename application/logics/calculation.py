from datetime import date, timedelta
import math

def calculate_bmi(weight, height):
    height_in_m = height / 100
    bmi = weight / (height_in_m * height_in_m)

    return round(bmi, 1)

def calculate_daily_calories(weight, height, age, gender, activity_level):
    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    if gender == "female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    #find Total Daily Energy Expenditure (TDEE)
    daily_calories = round((bmr * activity_level), 2)
    return daily_calories

#populate recommendation for user goal
def calculate_rec_primary_goal(bmi):
    if bmi < 18.5:
        return "gain weight"
    elif bmi >= 25:
        return "lose weight"
    else:
        return "maintain weight"

#calculate recommendation target weight and date using current bmi and TDEE
def calculate_rec_target(current_weight, current_height, bmi, primary_goal, daily_calories):
    if primary_goal == "lose":
        target_bmi = bmi - 2
    elif primary_goal == "gain":
        target_bmi = bmi + 2

    height_in_m = current_height / 100
    rec_target_weight = round((target_bmi * (height_in_m * height_in_m)), 0) 

    weight_difference = abs(rec_target_weight - current_weight)
    acceptable_range = daily_calories / 5
    
    number_of_days_req = math.ceil((weight_difference * 7000) / acceptable_range)
    rec_target_date = date.today() + timedelta(days = number_of_days_req)
    
    return rec_target_weight, rec_target_date

#calculate additional daily calories to reduce or gain
def calculate_adc(current_weight, target_weight, target_date):
    number_of_days = (target_date - date.today()).days
    weight_difference = abs(target_weight-current_weight)

    adc = (weight_difference * 7000) / number_of_days
    
    return adc

#calculate target calories based on additoinal daily calories to reduce or gain
#to reduce or gain is determined by user goal (primary goal)
def calculate_target_calories(adc, daily_calories, primary_goal):
    if primary_goal == "lose":
        target_calories = daily_calories + adc
    if primary_goal == "gain":
        target_calories = daily_calories - adc
    
    return target_calories
