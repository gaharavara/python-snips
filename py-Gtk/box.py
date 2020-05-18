import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="A poll")
        # Box is like an invisible container where you can hook any type of
        # Gtk widget
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        self.tuna_button = Gtk.Button(label="I love tuna")
        self.tuna_button.connect("clicked", self.button_clicked)
        self.box.pack_start(self.tuna_button, True, True, 0)

        self.pizza_button = Gtk.Button(label="I love pizza")
        self.pizza_button.connect("clicked", self.button_clicked)
        self.box.pack_start(self.pizza_button, True, True, 0)

    def button_clicked(self, widget):
        # We could simply use get_label method too!
        print("You said ", widget.get_properties("label"))

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

