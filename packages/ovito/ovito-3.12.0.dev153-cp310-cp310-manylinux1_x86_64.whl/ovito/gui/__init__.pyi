"""This module defines functions for real-time interactive rendering using a graphical user interface (GUI):

    * :py:func:`create_qwidget` - Create a Qt widget displaying a virtual viewport
    * :py:func:`create_ipywidget` - Create an interactive widget for embedding in Jupyter notebooks
    * :py:func:`create_window` - Create an OVITO Pro window with a full graphical user interface

Furthermore, the module defines the :py:class:`UtilityInterface` abstract base class, which lets you
implement custom utility applets for the command panel of OVITO Pro."""
__all__ = ['create_window', 'create_qwidget', 'UtilityInterface', 'create_ipywidget']
from __future__ import annotations
from typing import Any, Union, Sequence, Optional, Generator, Type
import PySide6.QtWidgets
import ipywidgets
from dataclasses import dataclass

class UtilityInterface:
    """Base: :py:class:`traits.has_traits.HasTraits`

Base class for utility applets running in the command panel of OVITO Pro."""
    pass

@dataclass(kw_only=True)
class JupyterViewportWidget(ipywidgets.DOMWidget):
    antialiasing: bool = True
    picking: bool = False
    vr_scale: float = 0.0

    def refresh(self) -> None:
        ...