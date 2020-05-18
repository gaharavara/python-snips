import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Best approach is to use OOP to develop such application
class MainWindow(Gtk.Window):
    def __init__(self):
        # Call the constructor Gtk.Window and pass an argument to initialize
        # the title of newly created window
        Gtk.Window.__init__(self, title="A window title")
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)

    def button_clicked(self, widget):
        print("You clicked")

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
