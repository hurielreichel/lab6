class Shape:

    def __init__(self, strokeWidth, strokeColour, fillColour):

        self.strokeWidth = float(strokeWidth)
        self.strokeColour = str(strokeColour)
        self.fillColour = str(fillColour)
           
    def get(self):

        return(self.strokeWidth, self.strokeColour, self.fillColour)

    def set(self, strokeWidth, strokeColour, fillColour):

        self.strokeWidth = strokeWidth

        self.strokeColour = strokeColour

        self.fillColour = fillColour

        return(self)
  
