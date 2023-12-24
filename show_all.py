import os
import pdoc
import pathlib

# explicitly import submodules that are not in __all__
import top_level_reimports, top_level_reimports._internal

# if __all__ is defined in the package, add additional submodules to be documented to __all__
top_level_reimports.__all__ = top_level_reimports.__all__ + ["_internal"]

# custom template to show methods starting with _
pdoc.render.configure(template_directory=pathlib.Path("/home/thorsten/src/pdoc/custom"))

pdoc.pdoc(
    "top_level_reimports",
    output_directory=pathlib.Path("/home/thorsten/src/pdoc/test_html"),
)
