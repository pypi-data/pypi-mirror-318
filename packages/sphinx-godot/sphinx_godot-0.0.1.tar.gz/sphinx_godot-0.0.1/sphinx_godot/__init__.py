from .gdscript import GDScriptLexer
from .descriptions import generate_description
from sphinx import version_info as sphinx_version
from sphinx.locale import _
from sphinx.util.logging import getLogger
from sys import version_info as python_version
from pathlib import Path

__version__ = "0.0.1"
__version_full__ = __version__
__doc__ = Rf"""
sphinx_godot v{__version__}
copyright (c) 2025-present opsocket and contributors (GPLv3+)
"""

BASE_DIR = Path(__file__).resolve().parent

theme_templates_path = str(BASE_DIR / "templates")

logger = getLogger(__name__)


def get_context(app, pagename, templatename, context, doctree):
    # Add ``sphinx_version_info`` tuple for use in Jinja templates
    context["sphinx_version_info"] = sphinx_version
    if not app.config.html_logo:
        context["logo_url"] = "_static/godot/img/docs_logo.svg"

    if not app.config.html_favicon:
        context["favicon_url"] = "_static/favicon.ico"


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    if python_version[0] < 3:
        logger.error(
            "Python 2 is not supported with sphinx_rtd_theme, update to Python 3."
        )

    # hook theme templates path into app config
    if theme_templates_path not in app.config.templates_path:
        app.config.templates_path.append(theme_templates_path)

    # sphinx emits the permalink icon for headers, so choose one more in keeping with our theme
    app.config.html_permalinks_icon = "\uf0c1"

    # Register the theme that can be referenced without adding a theme path
    app.add_html_theme("godot", Path(__file__).resolve().parent)

    # Register the lexer for gdscript syntax highlighting
    app.add_lexer("gdscript", GDScriptLexer)

    # Add Sphinx message catalog for newer versions of Sphinx
    # See http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_message_catalog
    rtd_locale_path = Path(__file__).resolve().parent / "locale"
    app.add_message_catalog("sphinx", str(rtd_locale_path))

    app.add_css_file("godot/css/main.css")
    app.add_js_file("godot/js/main.js")

    # Extend the default context when rendering the templates.
    app.connect("html-page-context", get_context)
    app.connect("html-page-context", generate_description)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
