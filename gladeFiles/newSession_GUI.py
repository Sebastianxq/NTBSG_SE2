import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        #Creates application bar name
       	Gtk.Window.__init__(self, title="New Session")
        self.set_border_width(300)

        #hbox = Gtk.Box(spacing=6)
        #self.add(hbox)
        
        #text input for Project Name
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.entry.set_text("Project Name")
        vbox.pack_start(self.entry, True, True, 0)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

        #Session Name label
        vbox_SessionName = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_SessionName.set_homogeneous(False)
        hbox.pack_start(vbox_SessionName, True, True, 0)
        label = Gtk.Label("Session Name")
        vbox_SessionName.pack_start(label, True, True, 0)


        #Description label
        vbox_description = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_description.set_homogeneous(False)
        hbox.pack_start(vbox_description, True, True, 0)
        label = Gtk.Label("Description")
        vbox_description.pack_start(label, True, True, 0)

        #Guidance Label (create a new session)
        vbox_guidance= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_guidance.set_homogeneous(False)
        hbox.pack_start(vbox_guidance, True, True, 0)
        label = Gtk.Label("Create a new session")
        vbox_guidance.pack_start(label, True, True, 0)

        #Click me Button
        button = Gtk.Button.new_with_label("Create")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        #close button
        button = Gtk.Button.new_with_mnemonic("_Cancel")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

        #open button
        #button = Gtk.Button.new_with_mnemonic("_Open")
        #button.connect("clicked", self.on_open_clicked)
        #hbox.pack_start(button, True, True, 0)

    #event handler for Click me button click
    def on_click_me_clicked(self, button):
        print("\"Click me\" button was clicked")

    #event handler for Open button click
    def on_open_clicked(self, button):
        print("\"Open\" button was clicked")

    #event handler for On button click
    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()


#exits program and wipes data or sumn
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
