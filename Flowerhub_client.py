import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import db


class CustomerMainScreen(Screen):
    pass

class MakeOrder(Screen):
    def makingorder(self):
        import smtplib
        fname = str(self.ids.fname.text.capitalize())
        sname = str(self.ids.sname.text.capitalize())
        email = str(self.ids.email.text.lower())
        creside = str(self.ids.creside.text.capitalize())
        treside = str(self.ids.treside.text.capitalize())
        ftype = str(self.ids.ftype.text.capitalize())
        nflowers = str(self.ids.nflowers.text)
        to = 'To: johnkarish073@gmail.com'
        tomail = 'johnkarish073@gmail.com'
        fromwho = 'From: ' + email
        emailbody = str(
            to + ' ' + fromwho + ' ' + fname + ' ' + sname + ' ' +
            creside + ' ' + treside + ' ' + ftype + ' ' + nflowers
        )
        server = smtplib.SMTP('localhost')
        server.sendmail(email, tomail, emailbody)
        server.quit()

class About(Screen):
    pass

class FlowerHubApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CustomerMainScreen(name='Main2'))
        sm.add_widget(MakeOrder(name='Order'))
        sm.add_widget(About(name='Info'))
        self.title = "RUACH FLOWERHUB INVENTORY AND VENDING SYSTEM-CLIENT"
        return sm

if __name__ == '__main__':
    FlowerHubApp().run()