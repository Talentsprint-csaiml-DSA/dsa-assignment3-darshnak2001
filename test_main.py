def test_huffman_coding():
    from main import huffman_coding
    print(huffman_coding('hello')) #It will print 1001111100
    assert huffman_coding('hello') == '1111100010' # It will return false

test_huffman_coding()