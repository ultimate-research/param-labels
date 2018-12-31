def assert_is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        assert key(el) >= key(lst[i]) # i is the index of the previous element

def test_hashes():
    from binascii import crc32

    with open("ParamLabels.csv") as f:
        csv = [line.rstrip('\n').split(',') for line in f.readlines() if not line.isspace()]

    assert_is_sorted(csv, key=lambda i: i[1])
    for line in csv:
        hashString = line[0]
        assert len(hashString) >= 12
        # Only the lower 32 bits are the hash (blame arthur), ensure the crc is legit
        assert crc32(line[1].encode('utf-8')) == (int(line[0], 16) & 0xFFFFFFFF)
