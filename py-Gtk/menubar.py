import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

people_data = [("Akshay", 88, "Actor"),("Luffy", 18, "Pirate"), ("Zoro", 21, "Swordsman")]

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Menu Bar")
        self.set_border_width(10)
        box = Gtk.Box()
        self.add(box)

        # MenuBar
        menu_bar = Gtk.MenuBar()

        # Menu
        menu = Gtk.Menu()

        # The first MenuItem itself is taken as the menu label here
        menu_label = Gtk.MenuItem("File")
        menu_label.set_submenu(menu)

        menu_item_open = Gtk.MenuItem("Open")
        menu_item_new = Gtk.MenuItem("New")
        menu_item_save = Gtk.MenuItem("Save")

        menu.append(menu_item_open)
        menu.append(menu_item_new)
        menu.append(menu_item_save)

        menu_bar.append(menu_label)

        box.pack_start(menu_bar, True, True, 0)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

