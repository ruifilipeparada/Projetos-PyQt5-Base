## 1. CLASS Calculator - desenvolvimento de lógica ## 

class Calculator:

    def __init__(self):
        self.current = ""
        self.operator = None
        self.previous = None

    def set_number(self, digit): 
        if digit == ",":
            digit = "."
        self.current += digit
        return self.current 
    
    def toggle_sign(self):
        if self.current:
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
        return self.current

    def percent(self):
        if self.current != "":
            try:
                value = float(self.current) / 100
                self.current = str(value)
                return self.current
            except:
                return self.current

    def backspace(self):
        if self.current:
            self.current = self.current[:-1]
            return self.current

    def set_operator(self, op):
        if self.current != "":
            if self.previous is None: 
                self.previous = float(self.current)
            else:
                self.calculate()
            self.current = ""
        self.operator = op 

    def calculate(self):
        if self.current != "" and self.operator is not None:
            try:
                value = float(self.current)
                if self.operator == "+":
                    self.previous += value
                elif self.operator == "-":
                    self.previous -= value
                elif self.operator == "*":
                    self.previous *= value
                elif self.operator == "/":
                    if value == 0:
                        return "Erro"
                    self.previous /= value
            except:
                return "Erro"
            
            self.current = ""
            self.operator = None 
            return str(self.previous)
        
    def clear(self):
        self.current = ""
        self.previous = None
        self.operator = None
        return ""
