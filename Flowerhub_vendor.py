import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import db

# VENDOR WINDOWS

class VendorMainScreen(Screen):
    pass

class ViewInventory(Screen):
    def display_available_flowers(self):
        available_flowers = db.get_available_flowers()
        self.ids.available_flowers_label.text = "Available Flowers:\n"
        for flower in available_flowers:
            self.ids.available_flowers_label.text += (
                f"ID: {flower['id']}, Name: {flower['name']}, Quantity: {flower['quantity']}\n"
            )

    def display_total_flowers(self):
        total_flowers = db.get_total_flowers()
        self.ids.total_flowers_label.text = f"Total Flowers: {total_flowers}"

class CarriageInwards(Screen):
    def add_flower(self):
        name = self.ids.add_flower_name.text.capitalize()
        quantity = int(self.ids.add_flower_quantity.text)
        price = float(self.ids.add_flower_price.text)
        db.add_flower(name, quantity, price)
        self.ids.add_flower_name.text = ""
        self.ids.add_flower_quantity.text = ""
        self.ids.add_flower_price.text = ""

class CarriageOutwards(Screen):
    def delete_sold_flower(self):
        flower_id = int(self.ids.sold_flower_id.text)
        quantity_sold = int(self.ids.sold_flower_quantity.text)
        db.delete_sold_flower(flower_id, quantity_sold)
        self.ids.sold_flower_id.text = ""
        self.ids.sold_flower_quantity.text = ""

class Reject(Screen):
    def delete_spoilt_flower(self):
        flower_id = int(self.ids.spoilt_flower_id.text)
        quantity_spoilt = int(self.ids.spoilt_flower_quantity.text)
        db.delete_spoilt_flower(flower_id, quantity_spoilt)
        self.ids.spoilt_flower_id.text = ""
        self.ids.spoilt_flower_quantity.text = ""

class Transactions(Screen):
    def add_transaction(self):
        custname = self.ids.custname.text.capitalize()
        custid = self.ids.custid.text
        county = self.ids.county.text.capitalize()
        town = self.ids.town.text.capitalize()
        ftype = self.ids.ftype.text.capitalize()
        nflowers = self.ids.nflowers.text
        price = self.ids.price.text
        db.add_transaction(custname, custid, county, town, ftype, nflowers, price)
        self.ids.custname.text = ''
        self.ids.custid.text = ''
        self.ids.county.text = ''
        self.ids.town.text = ''
        self.ids.ftype.text = ''
        self.ids.nflowers.text = ''
        self.ids.price.text = ''

class ViewTransaction(Screen):
    def display_available_transaction(self):
        available_transactions = db.get_available_transaction()
        self.ids.available_transactions_label.text = "Available Transactions:\n"
        for transaction in available_transactions:
            self.ids.available_transactions_label.text += (
                f"ID: {transaction['id']}, Name: {transaction['custname']}, "
                f"Flowertype: {transaction['ftype']}, No.flowers: {transaction['nflowers']}, "
                f"Price: {transaction['price']}, Date: {transaction['custid']}\n"
            )

class About(Screen):
    pass



class FlowerHubApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(VendorMainScreen(name='Main'))
        sm.add_widget(ViewInventory(name='Inventory'))
        sm.add_widget(CarriageInwards(name='Inwards'))
        sm.add_widget(CarriageOutwards(name='Outwards'))
        sm.add_widget(Reject(name='Spoilt'))
        sm.add_widget(Transactions(name='Transact'))
        sm.add_widget(ViewTransaction(name='Transactions'))
        sm.add_widget(About(name='Info'))
        self.title = "RUACH FLOWERHUB INVENTORY AND VENDING SYSTEM-VENDOR"
        return sm

if __name__ == '__main__':
    FlowerHubApp().run()
