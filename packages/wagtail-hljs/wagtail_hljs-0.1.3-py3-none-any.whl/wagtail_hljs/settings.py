from django.conf import settings

HLJS_PREFIX = "//cdnjs.cloudflare.com/ajax/libs/highlight.js"
HLJS_VERSION = "11.9.0"


def get_language_choices():
    """
    Default list of language choices, if not overridden by Django.
    """
    DEFAULT_LANGUAGES = (
        ("bash", "Bash/Shell"),
        ("css", "CSS"),
        ("diff", "diff"),
        ("html", "HTML"),
        ("javascript", "Javascript"),
        ("json", "JSON"),
        ("python", "Python"),
        ("scss", "SCSS"),
        ("yaml", "YAML"),
    )

    return getattr(settings, "WAGTAIL_HLJS_LANGUAGES", DEFAULT_LANGUAGES)


def get_theme():
    """
    Returns a default theme, if not in the proejct's settings. Default theme is 'coy'.
    """

    return getattr(settings, "WAGTAIL_HLJS_THEME", "base16/darcula")


# def get_copy_to_clipboard():
#     """
#     Returns the copy to clipboard setting.
#     """
#
#     return getattr(settings, "WAGTAIL_CODE_BLOCK_COPY_TO_CLIPBOARD", True)
