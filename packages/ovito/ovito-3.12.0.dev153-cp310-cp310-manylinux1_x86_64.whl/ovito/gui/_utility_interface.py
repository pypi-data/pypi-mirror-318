from __future__ import annotations
import ovito
import traits.api

class UtilityInterface(traits.api.HasTraits):
    """
    Base: :py:class:`traits.has_traits.HasTraits`

    Base class for utility applets running in the command panel of OVITO Pro.
    """

# Inject class into public module:
ovito.gui.UtilityInterface = UtilityInterface
