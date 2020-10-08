class LanguageConverter:

    """URL converter for languages (ru/en)"""

    regex = r"ru|en"

    def to_url(self, value):
        return str(value)

    def to_python(self, value):
        return str(value)

