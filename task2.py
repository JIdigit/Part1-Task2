ef square_number(num):
    x=num
    x=x*num
    return x
def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")

test_square_number()