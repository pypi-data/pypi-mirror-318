# smarttitletool/__init__.py

class SmartTitleTool:
    def __init__(self, *exclusions):
        self.exclusions = self._normalize_exclusions(exclusions)

    @staticmethod
    def _normalize_exclusions(exclusions):
        normalized = []
        for exclusion in exclusions:
            if isinstance(exclusion, str):
                normalized.extend(exclusion.lower().split())
            elif isinstance(exclusion, list):
                normalized.extend(word.lower() for word in exclusion)
        return normalized

    def to_smart_title_case(self, text):
        words = text.split()
        formatted_words = [
            word.capitalize() if word.lower() not in self.exclusions or i == 0 else word.lower()
            for i, word in enumerate(words)
        ]
        return " ".join(formatted_words)

