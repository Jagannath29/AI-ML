def multiple_two_number(num):
    if num == 0:
        return(ValueError)
    
    else:
        return num % 2 ==0
    
def test_numbers():
    assert multiple_two_number(2) is True