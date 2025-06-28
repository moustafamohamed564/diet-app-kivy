from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button

class DietApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.add_widget(Label(text="الاسم"))
        self.name_input = TextInput()
        self.add_widget(self.name_input)

        self.add_widget(Label(text="العمر"))
        self.age_input = TextInput(input_filter='int')
        self.add_widget(self.age_input)

        self.add_widget(Label(text="الوزن (كجم)"))
        self.weight_input = TextInput(input_filter='float')
        self.add_widget(self.weight_input)

        self.add_widget(Label(text="الطول (سم)"))
        self.height_input = TextInput(input_filter='float')
        self.add_widget(self.height_input)

        self.add_widget(Label(text="الجنس"))
        self.gender_spinner = Spinner(text='ذكر', values=['ذكر', 'أنثى'])
        self.add_widget(self.gender_spinner)

        self.add_widget(Label(text="النشاط اليومي"))
        self.activity_spinner = Spinner(text='متوسط', values=['خامل', 'متوسط', 'نشيط'])
        self.add_widget(self.activity_spinner)

        self.add_widget(Label(text="الهدف"))
        self.goal_spinner = Spinner(text='خسارة', values=['خسارة', 'تضخيم', 'حفاظ'])
        self.add_widget(self.goal_spinner)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

        self.calc_button = Button(text="احسب النظام")
        self.calc_button.bind(on_press=self.calculate)
        self.add_widget(self.calc_button)

    def calculate(self, instance):
        weight = float(self.weight_input.text)
        height = float(self.height_input.text)
        age = int(self.age_input.text)
        gender = self.gender_spinner.text
        activity = self.activity_spinner.text
        goal = self.goal_spinner.text

        # BMR
        bmr = 10 * weight + 6.25 * height - 5 * age + (5 if gender == "ذكر" else -161)

        # TDEE
        activity_factors = {"خامل": 1.2, "متوسط": 1.55, "نشيط": 1.725}
        tdee = bmr * activity_factors[activity]

        # Adjust for goal
        if goal == "خسارة":
            tdee -= 500
        elif goal == "تضخيم":
            tdee += 300

        protein = round((tdee * 0.3) / 4)
        carbs = round((tdee * 0.45) / 4)
        fats = round((tdee * 0.25) / 9)

        self.result_label.text = f"""السعرات اليومية: {int(tdee)} سعرة
بروتين: {protein} جم | كارب: {carbs} جم | دهون: {fats} جم
"""

class DietAppMain(App):
    def build(self):
        return DietApp()

if __name__ == '__main__':
    DietAppMain().run()
