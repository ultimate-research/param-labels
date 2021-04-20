#!/usr/bin/env python3

def assert_is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        assert key(el) >= key(lst[i]) # i is the index of the previous element

def test_hashes():
    from binascii import crc32

    with open("ParamLabels.csv") as f:
        csv = [line.rstrip('\n').split(',', 1) for line in f.readlines() if not line.isspace()]

    assert_is_sorted(csv, key=lambda i: i[1])
    alreadyFoundHashes = set()
    for line in csv:
        hashString = line[0]
        hash = int(hashString, 16)
        assert len(hashString) >= 12
        # Only the lower 32 bits are the hash (blame arthur), ensure the crc is legit
        # length - uppermost 8  bits
        # crc32  - lowermost 32 bits
        assert len(line[1]) == (hash >> 32)
        assert crc32(line[1].encode('utf-8')) == (hash & 0xFFFFFFFF)
        assert not hash in alreadyFoundHashes
        alreadyFoundHashes.add(hash)

def main():
    from binascii import crc32

    with open("ParamLabels.csv", mode="r", encoding="utf-8") as f:
        csv = [line.rstrip('\n').split(',', 1) for line in f.readlines() if not line.isspace()]

    try:
        assert_is_sorted(csv, key=lambda i: i[1])
    except AssertionError:
        print("ParamLabels.csv is not sorted, run remove_duplicates.py to fix")
    alreadyFoundHashes = set()
    for i, line in enumerate(csv):
        hashString = line[0]
        hash = int(hashString, 16)
        hashUtf8 = line[1].encode('utf-8')
        if not len(hashString) >= 12:
            print(f"'{hashString}', line {i+1} is not properly padded to 12 chars.")
        if not len(hashUtf8) == (hash >> 32):
            print(f"'{hashString}', line {i+1} specified string length mismatch.")
        # Only the lower 32 bits are the hash (blame arthur), ensure the crc is legit
        if not crc32(hashUtf8) == (hash & 0xFFFFFFFF):
            print(f"'{hashString}', line {i+1} crc32 mismatch.")
        if hash in alreadyFoundHashes:
            print(f"'{hashString}', line {i+1} hash duplicate.")
        alreadyFoundHashes.add(hash)

# Note: Intended use is with pytest, this is
#       merely for printing out incorrect hashes
if __name__ == '__main__':
    main()
