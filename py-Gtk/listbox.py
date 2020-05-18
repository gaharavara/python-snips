import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Listbox go")
        # To make it look clean
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        # We don't want the items of our listbox to be selectable
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)
        
        # CheckBox
        row1 = Gtk.ListBoxRow()
        # We use a box for every ListBoxRow to get additional styling choice
        box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        label1 = Gtk.Label("Do you like gtk")
        checkbox = Gtk.CheckButton()
        box1.pack_start(label1, True, True, 0)
        box1.pack_start(checkbox, True, True, 0)
        row1.add(box1)
        listbox.add(row1)
        
        # Switch
        row2 = Gtk.ListBoxRow()
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row2.add(box2)
        label2 = Gtk.Label("Turn On The Heat")
        switch = Gtk.Switch()
        box2.pack_start(label2, True, True, 0)
        box2.pack_start(switch, True, True, 0)
        listbox.add(row2)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()


