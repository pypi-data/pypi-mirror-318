import os
from pathlib import Path
from streamlit.components.v1 import declare_component
from streamlit_elements import version


def booleanize(s):
    return s.lower() in ['true', '1', "y", "yes"]

if not booleanize(os.environ.get("DEBUG", "")) and version.__release__:
    ELEMENTS_FRONTEND = {"path": (Path(version.__file__).parent/"frontend/build").resolve()}
else:
    ELEMENTS_FRONTEND = {"url": "http://127.0.0.1:3001"}

render_component = declare_component("streamlit_elements", **ELEMENTS_FRONTEND)
