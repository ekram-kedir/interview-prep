class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        even = "bdfh"
        odd = "aceg"
        
        if coordinates[0] in odd and int(coordinates[1]) % 2 != 0:
            return False
        if coordinates[0] in even and int(coordinates[1]) % 2 == 0:
            return False
        return True