import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("newSession_GUI.glade")

window = builder.get_object("window1") 
window.show_all()

Gtk.main()
