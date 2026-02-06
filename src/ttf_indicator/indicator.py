class Indicator:

    def indicate(self, ttf: float) -> str:
        """
        This function
        """
        if ttf < 5:
            return "red"
        elif ttf <= 15:
            return "yellow"
        else:
            return "green"