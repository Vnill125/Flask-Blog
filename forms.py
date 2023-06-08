


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired(), Length(min=3, max=20)])
