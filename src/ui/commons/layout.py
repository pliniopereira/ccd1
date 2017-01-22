from PyQt5 import QtWidgets

# Function that create a HBox Layout


def set_hbox(*args, stretch=None, stretch2=None):
    hbox = QtWidgets.QHBoxLayout()

    if stretch2 is not None:
        hbox.addStretch(stretch2)

    for widget in args:
        hbox.addWidget(widget)

    if stretch is not None:
        hbox.addStretch(stretch)

    return hbox


def set_wvbox(*args, stretch=None):
    vbox = QtWidgets.QVBoxLayout()
    for widget in args:
        vbox.addWidget(widget)

    if stretch is not None:
        vbox.addStretch(stretch)
    return vbox


def set_lvbox(*args):
    vbox = QtWidgets.QVBoxLayout()
    for layout in args:
        vbox.addLayout(layout)

    return vbox


def add_all_to_vbox(vbox, *args):
    for h in args:
        vbox.addWidget(h)

    return vbox


def add_widget_to_vbox(vbox, *args):
    for h in args:
        vbox.addLayout(h)

    return vbox