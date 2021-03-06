from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

import app.data.basicData as bD
from app.classes.Server import Server
from app.GUI.updateGUI.serverList import UpdateServerList

import os

Builder.load_file(f"{os.getcwd()}/GUI/Design/kv/addServer.kv")


class PopupContent(BoxLayout):
    def add_server(self):
        name = self.ids.server_name.text
        ip = self.ids.server_address.text
        port = self.ids.server_port.text

        def clear_inputs():
            self.ids.server_name.text = ""
            self.ids.server_address.text = ""
            self.ids.server_port.text = ""

        if name == "" or ip == "" or port == "":
            clear_inputs()
            self.ids.server_name.focus = True
            return

        AddServerHandler(name, ip, port)

        bD.AddServerPopup.dismiss()  # Close the popup


class AddServerPopup(Popup):
    pass


class CreateAddServerPopup:
    def __init__(self):
        self.popup = AddServerPopup()
        bD.AddServerPopup = self.popup
        self.popup.open()


class AddServerHandler:
    def __init__(self, server_name, server_ip, server_port):
        self.server_name = server_name
        self.server_ip = server_ip
        self.server_port = server_port

        self.server = Server(self.server_name, self.server_ip, self.server_port)

        self.add_server()
        UpdateServerList()

    def add_server(self):
        server_list = bD.server_list
        server_list.append(self.server)
        bD.server_list = server_list

