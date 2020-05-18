import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="grid layout")
        # Create a Grid widget
        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="button1")
        button2 = Gtk.Button(label="button2")
        button3 = Gtk.Button(label="button3")
        button4 = Gtk.Button(label="button4")
        button5 = Gtk.Button(label="button5")

        # No argument places the button by default at top left position
        grid.add(button1)
        # Attach the button to a given position
        # arguments are widget to attach, column, row, column_span, row_span
        grid.attach(button2, 1, 0, 2, 1)
        # Here we need to provide another widget to take as reference when attaching
        # A positional argument declaring in which direction should be the reference
        # taken, width and height
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach(button4, 1, 1, 2, 1)
        grid.attach(button5, 2, 0, 2, 1)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
