class Point:
    def __init__(self, x, y) -> None:
        import math
        self.x = x
        self.y = y
        self.r = self.distance_from_center()
        self.theta = math.atan2(y, x)
        self.theta_degrees = math.degrees(self.theta)
    def __str__(self) -> str:
        return f"The point is ({self.x},{self.y})"
    
    def polar(self):
        return (self.r, self.theta_degrees)
    
    def distance_from_center(self):
        import math
        a = self.x * self.x
        b = self.y * self.y
        return math.sqrt(a+b)
     
    def distance_to(self, other_point):
        from math import hypot
        return hypot(self.x - other_point.x, self.y - other_point.y)

    #def line_between(self, other_point):

class Line(Point):
    def __init__(self, x, y, slope) -> None:
        super().__init__(x, y)
        self.slope = slope
        self.y_intercept = self.intercept()
    
    def intercept(self):
        return self.y - self.slope*self.x

    def __str__(self) -> str:
        if self.y_intercept > 0:
            return f"The line is y = {self.slope}x + {self.y_intercept}"
        elif self.y_intercept < 0:
            return f"The line is y = {self.slope}x - {-self.y_intercept}"
        else:
            return f"The line is y = {self.slope}x"