# consists blocks
# blocks consist transaction
# blocks are connected through hashing
# unique digital fingerprint - transaction + previous blocks hash(fingerprint)

from chain_function import Block
from Translate import convert_to_spanish

y = input("How many transactions would you like to make today?")
blockchain = {for x in range(int(y + 1))}

blockchain = {}

genesis_block = Block("Chancellor on the brink...", ["Person(A) sent 1 BTC to Person(B)"])
second_block = Block(genesis_block.block_hash, ["Person(B) sent 2 BTC to Person (C)"])
third_block = Block(genesis_block.block_hash, ["Person(C) sent 3 BTC to Person (D)"])

blockchain["Result1"] = f'''BLOCK HASH: Genesis Block: {genesis_block.block_hash}'''
blockchain["Result2"] = f'''BLOCK HASH: Second Block: {second_block.block_hash}'''
blockchain["Result3"] = f'''BLOCK HASH: Third Block: {third_block.block_hash}'''

convert_to_spanish(blockchain["Result1"])
convert_to_spanish(blockchain["Result2"])
convert_to_spanish(blockchain["Result3"])

print(f"Hashes Completed; Total Number of Chain Items: {len(blockchain)}")
