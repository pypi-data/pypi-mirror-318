from __future__ import annotations
from typing import Union
from ..pipeline import Pipeline
from ..vis import Viewport
import ovito
import ovito.nonpublic

# Implementation of the ovito.gui.create_qwidget() function:
def create_qwidget(contents: Union[Pipeline, Viewport, None] = None, parent: "PySide6.QtWidgets.QWidget | None" = None, *, show_orientation_indicator: bool = True, show_title: bool = False):
    """
    Creates an interactive visual widget displaying the three-dimensional scene as seen through a virtual :py:class:`~ovito.vis.Viewport`.
    The method creates an interactive window accepting mouse inputs from the user similar to the viewport windows
    of the OVITO desktop application. You can use this method to develop custom user interfaces based on the Qt cross-platform framework
    that integrate OVITO's functionality and display the output of a data pipeline.

    :param contents: The :py:class:`~ovito.pipeline.Pipeline` or :py:class:`~ovito.vis.Viewport` object to be displayed by the window.
    :param parent: An optional Qt widget serving as container for the new viewport widget.
    :return: `PySide6.QtWidgets.QWidget <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html>`__

    The Qt widget returned by this method is linked to the :py:class:`!Viewport` instance.
    Any changes your Python script subsequently makes to the non-visual :py:class:`!Viewport` instance,
    for example setting :py:attr:`~ovito.vis.Viewport.camera_pos` or :py:attr:`~ovito.vis.Viewport.camera_dir`, will automatically be reflected by the
    visual widget. Vice versa will interactions of the user with the viewport widget
    automatically lead to changes of the corresponding fields of the :py:class:`!Viewport` instance.

    OVITO automatically creates a QApplication object if necessary, which can be accessed via the :py:meth:`!QApplication.instance()` static method.

    The following short example program demonstrates the use of the :py:meth:`!show_qt_widget` method. Please see the
    `Qt for Python <https://doc.qt.io/qtforpython-6/>`__ documentation for more information on how to create graphical
    user interfaces using the Qt framework.

    .. seealso:: :ref:`example_trajectory_viewer`

    .. literalinclude:: ../example_snippets/viewport_create_widget.py
        :lines: 17-

    """
    from ovito.qt_compat import shiboken, QtWidgets

    # Determine what to display in the viewport window.
    if contents is None:
        # Create an ad-hoc viewport showing the global scene.
        viewport = Viewport()
    elif isinstance(contents, Pipeline):
        # Create a new scene containing just the given pipeline and an ad-hoc viewport.
        scene = ovito.nonpublic.Scene()
        scene.children.append(ovito.nonpublic.SceneNode(pipeline=contents))
        viewport = Viewport(scene=scene)
    elif isinstance(contents, Viewport):
        viewport = contents
    else:
        raise ValueError("Invalid contents argument. Expected a Pipeline, Viewport, or None.")

    # Get memory address of parent widget.
    if parent is None:
        parent_ptr = 0
    elif isinstance(parent, QtWidgets.QWidget):
        parent_ptr = shiboken.getCppPointer(parent)[0]
    else:
        raise ValueError("Invalid parent argument. Expected a QWidget instance or None.")

    # Initialize main event loop, which is needed for displaying a widget with the Qt framework.
    ovito.init_qt_app(support_gui=True)

    # Create viewport window widget.
    vpwin = ovito.nonpublic.OpenGLViewportWindow(viewport, parent_ptr)
    vpwin.show_title = show_title
    vpwin.show_orientation_indicator = show_orientation_indicator

    # Return a QWidget to the caller.
    return shiboken.wrapInstance(vpwin._widget, QtWidgets.QWidget)

# Inject function into public module:
ovito.gui.create_qwidget = create_qwidget
