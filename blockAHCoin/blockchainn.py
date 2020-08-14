from block import Block
import datetime

block_chain = [Block.create_genesis_block()]

print("The genesis block has been created!")
print("Hash: %s" % block_chain[-1].hash)

num_blocks_to_add = 10

for i in range(1, num_blocks_to_add + 1):
    block_chain.append(Block(block_chain[i - 1].hash,
                             "Block number %d" % i,
                             datetime.datetime.now()))
    print("Block #%d created." % i)
    print("Hash: %s" % block_chain[-1].hash)
    
