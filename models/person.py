from decimal import Decimal

class Person:
    """
    This class represents people
    """

    def __init__(self,name,userId,latitude,longitude):
    
        """
        Constructor

        Args:
        name(string): persons name
        userId(int): persons id
        latitude(Decimal): persons latitude coordinate
        longitude(Decimal): persons longitude coordinate
        """
        try:
            self.name=name
            self.userId=userId
            self.latitude=Decimal(latitude)
            self.longitude=Decimal(longitude)

        except:
            raise Exception("Incorrect input format")