import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject, GdkPixbuf

user_data = [("Akshay", 88, "Actor"),("Luffy", 18, "Pirate"), ("Zoro", 21, "Swordsman")]

class Item(GObject.GObject):
    text = str
    age = GObject.property(type = int)
    profession = GObject.property(type = str)
    pix_buf = GdkPixbuf.Pixbuf
    uri = object

    def __init__(self):
        GObject.GObject.__init__(self)
    def __repr__(self):
        print(text)

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Flow Box")
        self.set_border_width(10)

        flowbox = Gtk.FlowBox()
        self.add(flowbox)

        # Create Gio.ListStore
        liststore = Gio.ListStore()

        # Append Items to List Store
        for user in user_data:
            item = Item()
            item.text = user[0]
            item.age = user[1]
            item.profession = user[2]

            liststore.append(item)

        flowbox.bind_model(liststore, self.create_widget_func)
        flowbox.connect("child-activated", self.flowbox_child_activated)

    def create_widget_func(self, item):
        flowbox_child = Gtk.FlowBoxChild()

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        label1 = Gtk.Label(item.text)
        label2 = Gtk.Label(item.age)
        label3 = Gtk.Label(item.profession)

        box.pack_start(label1, True, True, 0)
        box.pack_start(label2, True, True, 0)
        box.pack_start(label3, True, True, 0)

        flowbox_child.add(box)

        return flowbox_child

    def flowbox_child_activated(self, flowbox, child):
        print("child activated")

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

