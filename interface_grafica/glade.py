import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def fechar(self, *args):
        Gtk.main_quit()

    def btn_clique(self, button):
        print("ok")

builder = Gtk.Builder()
builder.add_from_file("alo.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
