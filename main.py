from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("LoginPage.kv")

# class QuizPageApp(App):
#  def build(self):
#       return QuizManager()

# class QuizManager(ScreenManager):
# pass

# class Question1Screen(Screen):
# def answer_question(self, bool):
#         if bool:
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "error"
#
# class Question2Screen(Screen):
#     def answer_question(self, text):
#         if text.lower() == "deep in the heart of texas":
#             self.manager.current = "correct"
#         else:
#             self.ids.invalid_guess.text = "Incorrect! Try again."
#             self.ids.invalid_guess.color = "red"
# class CorrectScreen(Screen):
#     def next_question(self):
#         self.manager.current = "question2"
#
# class ErrorScreen(Screen):
#     pass
#
# QuizPageApp().run()


class LoginPageApp(App):
    def build(self):
        return LoginManager()


class LoginManager(ScreenManager):
    pass


class LoginScreen(Screen):
    def login(self, user, password):
        if user in users.keys() and password in users.values():
            self.manager.current = "landing"
        else:
            self.ids.userinput.text = "Invalid Login Information"
            self.ids.userinput.color = "red"


    def register(self):
        self.manager.current = 'register'


class RegisterScreen(Screen):
    def register(self, newuser, newpass, newpass2):
        newuser = str(newuser)
        newpass = str(newpass)
        newpass2 = str(newpass2)
        lowers = 'abcdefghijklmnopqrstuvwxyz'
        uppers = 'ABCDEFGHIJKLMNOPQRSTUV'
        nums = '123456789'
        spec = '!@#$%^&*_'
        num_check = False
        special_check = False
        lower_check = False
        upper_check = False
        for letter in newpass:
            if letter in lowers:
                lower_check = True
        for letter in newpass:
            if letter in uppers:
                upper_check = True
        for letter in newpass:
            if letter in nums:
                num_check = True
        for letter in newpass:
            if letter in spec:
                special_check = True
        print(newpass + newpass2)
        if newuser in users.keys():
            self.ids.problem.text = 'Username Already In System'
        elif newpass != newpass2:
            self.ids.problem.text = 'Password Does Not Match'
        elif len(newpass) < 8:
            self.ids.problem.text = 'Password Must Contain Minimum 8 Characters'
        elif not lower_check:
            self.ids.problem.text = 'Password Must Contain Minimum 1 Lowercase Letter'
        elif not upper_check:
            self.ids.problem.text = 'Password Must Contain Minimum 1 Uppercase Letter'
        elif not num_check:
            self.ids.problem.text = 'Password Must Contain Minimum 1 Number'
        elif not special_check:
            self.ids.problem.text = 'Password Must Contain Minimum 1 Special Character'
        if num_check == True and lower_check == True and upper_check == True and special_check == True and len(
                newpass) >= 8 and newpass == newpass2:
            self.ids.problem.color = 'green'
            self.ids.problem.text = 'Account Created'
            users[newuser] = newpass

    def gologin(self):
        self.manager.current = 'login'


class LandingPage(Screen):
    def logout(self):
        self.manager.current = 'login'


users = {}
LoginPageApp().run()
