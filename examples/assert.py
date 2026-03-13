def assert_example():
    assert 1 + 1 == 2, "Math is broken!"
    assert "hello".upper() == "HELLO", "String manipulation failed!"
    assert len([1, 2, 3]) == 3, "List length is incorrect!"
    
    item = 2
    assert item in [1, 2, 3], "Item not found in list!"
    print("All assertions passed!")

assert_example()