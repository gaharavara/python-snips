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

        # Create a ListStore
        list_store = Gtk.ListStore(str, int, str)
        # Populate the ListStore
        for item in people_data:
            list_store.append(list(item))

        # View to display the model
        tree_view = Gtk.TreeView(model=list_store)
        # Add columns to the tree view
        for i, col_val in enumerate(["Name", "Age", "Profession"]):
            # Create a cell renderer, here only text type needed
            cell_renderer = Gtk.CellRendererText()

            # Create TreeViewColumn
            column = Gtk.TreeViewColumn(col_val, cell_renderer, text=i)
            column.set_sort_column_id(i)

            # After 3 iterations we will have all the three columns
            # Name Age Profession, each rendered of type Text 
            tree_view.append_column(column)

        # row-activated
        tree_view.connect("row-activated", self.row_activated)

        # get_selection returns Gtk.TreeSelection
        selection = tree_view.get_selection()
        selection.connect("changed", self.selection_changed)

        # Add the tree_view to our layout box, to display
        box.pack_start(tree_view, True, True, 0)

    def row_activated(self,*args):
        print("Row Activated")

    def selection_changed(self, selection):
        print("selection changed")
        model, row = selection.get_selected()
        if row is not None:
            print("Name", model[row][0])
            print("Age", model[row][1])
            print("Profession", model[row][1])

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

