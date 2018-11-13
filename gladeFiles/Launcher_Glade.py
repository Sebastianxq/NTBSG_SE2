import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("Launcher_GUI.glade")

window = builder.get_object("window1")
window.show_all()

builder1 = Gtk.Builder()
builder1.add_from_file("newSession_GUI.glade")

window = builder.get_object("window2")
window.show_all()

Gtk.main()
