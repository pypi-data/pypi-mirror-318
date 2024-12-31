from importlib.metadata import version
from .vis_axes import (
    despine, naked, get_list_ticks, get_list_ticklabels, set_min_lims_to_0,
    equal_xy_lims, equal_lims_two_axs, equal_lims_n_axs, 
    remove_xticklabels, remove_yticklabels, remove_both_ticklabels,
    add_panel_label
)
from .vis_text import (
    set_fontsize, two_digit_sci_not, readable_p, readable_p_exact,
    readable_p_significance_statement
)
__version__ = version("missmat")
__author__= 'Thijs van der Plas'
__description__ = 'Simple functions to complement matplotlib'
__all__ = ['vis_axes', 'vis_text']
