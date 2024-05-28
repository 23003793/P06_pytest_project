from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
        
    def test_subtract(self):
        #arrange 
        a=10
        b=5
        cal=Calculator()

        #act
        result=cal.add(a,b)

        #assert
        expected = 5
        assert result == expected

    def test_multiply(self):
        #arrange
        a=4
        b=2
        cal=Calculator()

        #act
        result=cal.multiply(a,b)

        #assert
        expected = 8
        assert result == expected
        
    def test_divide(self):
        a=10
        b=5
        cal=Calculator()
        result=cal.divide(a,b)

        expected=2
        assert result == expected





