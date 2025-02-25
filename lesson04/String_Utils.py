class StringUtils:
      
    @staticmethod
    def to_uppercase(text: str) -> str:
    
        if text is None:
            return None
        return text.upper()

    @staticmethod
    def to_lowercase(text: str) -> str:
        if text is None:
            return None
        return text.lower()

    @staticmethod
    def capitalize(text: str) -> str:
       
        if text is None:
            return None
        return text.capitalize()

    @staticmethod
    def reverse(text: str) -> str:
       
        if text is None:
            return None
        return text[::-1]