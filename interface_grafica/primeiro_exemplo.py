import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Janela(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Hello World")

        self.button = Gtk.Button(label = "Clique aqui")
        self.button.connect("clicked", self.btn_clique)
        self.add(self.button)

    def btn_clique(self, widget):
        print("Hello world")

win = Janela()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
