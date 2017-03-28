import unittest


def hash_table_size(item, tablesize):
    """
    A hashing technique that involves 
    
    1. Converting the characters in a string to a list of ordinal values
    2. Get the sum of the list
    3. Get the remained by doing a modulo using tablesize

    item - string
    tablesize 
    """
    ordinal_list = [ord(i) for i in item]
    return sum(ordinal_list) % tablesize

def hash_fold(item, tablesize):
    """
    The folding method for constructing hash functions begins by dividing the item into equal-size 
    pieces (the last piece may not be of equal size). These pieces are then added together to give 
    the resulting hash value. For example, if our item was the phone number 436-555-4601, we would 
    take the digits and divide them into groups of 2 (43,65,55,46,01). After the addition, 
    43+65+55+46+0143+65+55+46+01, we get 210. If we assume our hash table has 11 slots, then we 
    need to perform the extra step of dividing by 11 and keeping the remainder. In this case 
    210 % 11210 % 11 is 1, so the phone number 436-555-4601 hashes to slot 1.

    item -  a number
    tablesize
    """
    # Split number into n chunks
    n = 2
    number = str(item)
    chunked_list = [number[i:i+n] for i in range(0, len(number), n)]

    # Convert the list items to numbers then get the sum
    sum = 0
    for c in chunked_list:
        sum += int(c)
    return sum % tablesize

def hash_mid_square(item, tablesize):
    """
    Another numerical technique for constructing a hash function is called the mid-square method. 
    We first square the item, and then extract some portion of the resulting digits. For example,
    if the item were 44, we would first compute 442=1,936442=1,936. By extracting the middle two 
    digits, 93, and performing the remainder step, we get 5 (93 % 1193 % 11).

    item - a number
    """
    squared_item = str(item**2)
    if len(squared_item) % 2 == 0:
        midpoint = len(squared_item) // 2
        mid_square = int(squared_item[midpoint-1] + squared_item[midpoint])
    else:
        mid_square = squared_item[len(squared_item) // 2]
    return int(mid_square) % tablesize


# Tests
class TestHashTree(unittest.TestCase):
    def test_hash_table_size(self):
        self.assertEqual(
            hash_table_size('cat', 11),
            4
        )

    def test_hash_fold(self):
        self.assertEqual(
            hash_fold(4365554601, 11),
            1
        )

    def test_mid_square(self):
        self.assertEqual(
            hash_mid_square(44, 11),
            5
        )

if __name__ == '__main__':
    unittest.main()