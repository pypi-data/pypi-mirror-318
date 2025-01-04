class FlexibleTitle:
    def __init__(self, *exclusions):
        """
        Initializes the FlexibleTitle formatter with optional exclusions.

        Args:
            exclusions (str, list, or multiple strings): Words to exclude from capitalization.
        """
        self.exclusions = self._normalize_exclusions(exclusions)

    @staticmethod
    def _normalize_exclusions(exclusions):
        """
        Normalizes exclusions to ensure they are a list of lowercase words.

        Args:
            exclusions (tuple): A tuple of words, lists, or strings to normalize.

        Returns:
            list: A list of lowercase words.
        """
        normalized = []
        for exclusion in exclusions:
            if isinstance(exclusion, str):
                normalized.extend(exclusion.lower().split())  # Split string into words
            elif isinstance(exclusion, list):
                normalized.extend(word.lower() for word in exclusion)
        return normalized

    def to_flexible_title_case(self, text):
        """
        Converts the input text to flexible title case, excluding specified words from capitalization.

        Args:
            text (str): The input string to convert.

        Returns:
            str: The formatted string in flexible title case.
        """
        words = text.split()
        formatted_words = [
            word.capitalize() if word.lower() not in self.exclusions or i == 0 else word.lower()
            for i, word in enumerate(words)
        ]
        return " ".join(formatted_words)

