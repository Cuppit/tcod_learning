class Impossible(Exception):
    """Exception reaised when an action is impossible to be performed.
    
    The reason is given as the exception message.
    """

class QuitWithoutSaving(SystemExit):
    """Can be raised to exit the game without automatically saving."""
    
    