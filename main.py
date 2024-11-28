import heapq
from collections import Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq  # Compare nodes by frequency for the priority queue

def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap)
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree by merging nodes
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Return the root node of the tree

def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    if root:
        if root.char is not None:  # Leaf node (has a character)
            codes[root.char] = current_code
        generate_huffman_codes(root.left, current_code + "0", codes)  # Traverse left with "0"
        generate_huffman_codes(root.right, current_code + "1", codes)  # Traverse right with "1"
    return codes

def huffman_coding(input_string):
    # Step 1: Count character frequencies
    frequencies = Counter(input_string)

    # Step 2: Build the Huffman Tree
    root = build_huffman_tree(frequencies)

    # Step 3: Generate Huffman codes for each character
    huffman_codes = generate_huffman_codes(root)

    # Step 4: Encode the string
    encoded_string = ''.join(huffman_codes[char] for char in input_string)

    return encoded_string
