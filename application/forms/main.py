from application.models.mongoDB.get import *
from application.forms.register import primary_goal_choices, activity_level_choices

from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField,
    DecimalField, DateField, SelectField,
    SubmitField)
from wtforms.validators import (
    ValidationError, DataRequired,
    Length, EqualTo, NumberRange, Regexp
)

data_required_msg = "Required"

class LoginForm(FlaskForm):       
    username = StringField(
        label = "Username:",
        validators = [
            DataRequired("Username required")
        ])
    password = PasswordField(
        label = "Password:",
        validators = [
            DataRequired("Password required")
        ])

    submit = SubmitField(label = "Login")

class UpdateUsernameForm(FlaskForm):
    #validate username by finding matching name exists in the database
    def validate_username(form, username_to_check):
        if find_username(username_to_check.data):
            raise ValidationError("Username already exists, please try another username")
    
    username = StringField(
        label = "Username:",
        validators = [
            DataRequired(data_required_msg),
            Length(min = 2, max = 30, message = "Username must be between %(min)d and %(max)d characters"),
            Regexp(r"^[a-zA-Z0-9]+$", message = "Username should not include special letter or space")
        ])
    
    submit_username = SubmitField(label = "Update")

class UpdatePasswordForm(FlaskForm):
    password = PasswordField(
        label = "New Password:",
        validators = [
            DataRequired(data_required_msg),
            Length(min = 8, message = "Password must be %(min)d or more characters")
        ])
    re_password = PasswordField(
        label = "Confirm Password:",
        validators = [
            DataRequired(data_required_msg),
            EqualTo("password", message = "Passwords do not match")
        ])
    
    submit_password = SubmitField(label = "Update")

class UpdateCurrentForm(FlaskForm):
    current_weight = DecimalField(
        label = "Curret Weight:",
        places = 2,
        validators = [
            DataRequired(f"{data_required_msg}, Height must be numeric"),
            NumberRange(min = 20, max=150, message="Weight must be in the range of %(min)d and %(max)d")
        ])
    current_height = DecimalField(
        label = "Curret Height:",
        places = 2,
        validators = [
            DataRequired(f"{data_required_msg}, Height must be numeric"),
            NumberRange(min = 100, max = 250, message = "Height must be in the range of %(min)d and %(max)d")
        ])

    submit_current = SubmitField(label = "Update")

class UpdateGoalForm(FlaskForm):
    primary_goal = SelectField(
        label = "Primary goal:",
        choices = list(primary_goal_choices.keys()),
        validators = [
            DataRequired(data_required_msg)   
        ])
    
    activity_level = SelectField(
        label = "Activity level:",
        choices = list(activity_level_choices.keys()),
        validators = [
            DataRequired(data_required_msg)   
        ])
    
    submit_goal = SubmitField(label = "Update")

class UpdateTargetForm(FlaskForm):
    def validate_target_date(form, date_to_check):
        current_date = date.today()
        target_date = date_to_check.data
        if (target_date - current_date).days <= 0:
            raise ValidationError("Target date can only be future date")
    
    target_weight = DecimalField(
        label = "Target Weight:",
        places = 2,
        validators = [
            DataRequired(data_required_msg),
            NumberRange(min = 20, max = 150, message = "Weight must be in the range of %(min)d and %(max)d")
        ])
    target_date = DateField(
        label = "Target Date:",
        validators = [
             DataRequired(data_required_msg)
        ])
    
    submit_target = SubmitField(label = "Update")
