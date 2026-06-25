from application.logics.calculation import *
from application.models.mongoDB.get import *

import bcrypt

#class used to through error message
class CustomErrorMessage(Exception):
    pass

#if user goal would lead to underweight or overweight => throw error
def validate_primary_goal(bmi, primary_goal):
    if primary_goal == "lose" and (bmi - 2) < 19:
        raise CustomErrorMessage("Your goal would lead to underweight")
    if primary_goal == "gain" and (bmi + 2) >= 24.9:
         raise CustomErrorMessage("Your goal would lead to obesity")

#if user has set goal but setting target weight that does not suit the goal set => throw error
def validate_target_weight(current_weight, target_weight, primary_goal):
    if primary_goal == "lose" and current_weight < target_weight:
        raise CustomErrorMessage("You will gain weight instead!")
    elif primary_goal == "gain" and current_weight > target_weight:
        raise CustomErrorMessage("You will lose weight instead!")
    elif current_weight == target_weight:
        raise CustomErrorMessage("You will maintain weight instead!")

#if the target weight leads to underewight or overweight => throw error
def validate_target_bmi(target_weight, current_height):
    target_bmi = calculate_bmi(target_weight, current_height)

    if target_bmi <= 19:
        raise CustomErrorMessage("Your target weight would lead to underweight")
    elif target_bmi >= 30:
        raise CustomErrorMessage("Your target weight would lead to obesity")

#if the target require more changes than 20% of TDEE => throw error
def validate_target(adc, daily_calories):
    acceptable_range = daily_calories/5

    if acceptable_range < adc:
        raise CustomErrorMessage("Current target would cause damage to your health")

#if same as old password => throw error
def validate_new_password(username, new_password):
    old_password_hashed = get_password(username)
    new_password_hashed = bcrypt.hashpw(new_password.encode("utf-8"), old_password_hashed)

    if old_password_hashed == new_password_hashed:
        raise CustomErrorMessage("New password is same as the old password, Please use other password")

#if new weight has more than 5kg difference than the old weight => throw error
def validate_new_current_weight(old_current_weight, new_current_weight):
    if abs(old_current_weight - new_current_weight) > 10:
        raise CustomErrorMessage("Plesae enter valid weight for your new current weight")
        
#if new height has more than 5cm difference than the old height => throw error
def validate_new_current_height(old_current_height, new_current_height):
    if abs(old_current_height - new_current_height) > 5:
        raise CustomErrorMessage("Plesae enter valid height for your new current height")
    
