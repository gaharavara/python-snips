import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

people_data = [("Akshay", 88, "Actor"),("Luffy", 18, "Pirate"), ("Zoro", 21, "Swordsman")]

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="List View")
        self.set_border_width(10)
        box = Gtk.Box()
        self.add(box)

        # ListStore
        # Convert data to ListStore (lists that tree view can display)
        people_liststore = Gtk.ListStore(str, int, str)
        # Add items to the model/ populate the model (liststore)
        for item in people_data:
            people_liststore.append(list(item))

        # TreeView is the item that is displayed
        treeview = Gtk.TreeView(model=people_liststore)

        # How to draw the data, using only one type of cell_renderer, since
        # here we are only dealing with text
        cell_renderer = Gtk.CellRendererText()

        for i, col_title in enumerate(["Name", "Age", "Profession"]):

            # Create columns, here taking text as column number
            column = Gtk.TreeViewColumn(col_title, cell_renderer, text=i)

            # Add the column to treeview
            treeview.append_column(column)

        # Add treeview to main layout
        box.pack_start(treeview, True, True, 0)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

