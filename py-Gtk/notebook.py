import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Notebook")
        self.set_border_width(10)

        # Notebook
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Page
        page1 = Gtk.Box()
        page1.add(Gtk.Label("This is the content of page 1"))
        self.notebook.append_page(page1, Gtk.Label("page 1"))

        # Page with icon as tab label
        page2 = Gtk.Box()
        page2.add(Gtk.Label("Duh, already on page 2 !"))
        tab_label = Gtk.Image.new_from_icon_name("gnome-dev-cdrom-audio", Gtk.IconSize.MENU)
        self.notebook.append_page(page2, tab_label)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
