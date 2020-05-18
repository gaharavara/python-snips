import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Sign In")
        self.set_border_width(10)
        self.set_size_request(200, 100)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(box)

        # Entry
        self.username = Gtk.Entry()
        self.username.set_text("Username")
        box.pack_start(self.username, True, True, 0)

        self.password = Gtk.Entry()
        self.password.set_text("Password")
        self.password.set_visibility(False)
        box.pack_start(self.password, True, True, 0)

        # Sign In
        button = Gtk.Button(label="Sign In")
        button.connect("clicked", self.signin)
        box.pack_start(button, True, True, 0)

    def signin(self, widget):
        print(self.username.get_text())
        print(self.password.get_text())

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

