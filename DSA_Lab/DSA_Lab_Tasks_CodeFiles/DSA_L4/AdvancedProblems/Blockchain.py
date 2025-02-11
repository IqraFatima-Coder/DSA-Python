class BlockNode:
    def __init__(self, block_number, transactions):
        self.block_number = block_number
        self.transactions = transactions
        self.next = None

class Blockchain:
    def __init__(self):
        self.head = None

    def add_block(self, transactions):
        block_number = 1
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            block_number = temp.block_number + 1
        
        new_block = BlockNode(block_number, transactions)
        if not self.head:
            self.head = new_block
        else:
            temp.next = new_block
        
        print(f'Block {block_number} added with transactions: {transactions}')

    def display_chain(self):
        if not self.head:
            print("No blocks in the chain.")
            return

        temp = self.head
        while temp:
            print(f'Block {temp.block_number}: {temp.transactions}')
            temp = temp.next

# Example Usage
blockchain = Blockchain()
blockchain.add_block(["TX1: User1 -> User2: 50 BTC", "TX2: User3 -> User4: 30 BTC"])
blockchain.add_block(["TX3: User1 -> User3: 20 BTC"])

blockchain.display_chain()
