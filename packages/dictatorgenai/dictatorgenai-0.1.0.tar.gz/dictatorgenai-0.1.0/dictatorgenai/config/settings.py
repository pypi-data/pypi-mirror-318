class DictatorSettings():
    """
    Centralized configuration settings for the Dictator Framework.
    """
    language: str = "en"  # Default language for responses
    confidence_threshold: float = 0.7  # Confidence threshold for general selection
    logging_level: str = "INFO"  # Default logging level

    @classmethod
    def set_language(cls, language: str):
        """
        Change the default language for the framework.
        """
        cls.language = language

    @classmethod
    def get_language(cls):
        """
        Retrieve the current default language.
        """
        return cls.language
