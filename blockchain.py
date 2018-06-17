# Initialize Blockchain
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ 
        Appends new value and the last value of the blockchain. 

        Arguments:
        :transaction_amount: The amount added to the blockchain.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the input of the user transaction amount as a float. """
    return float(input('Your transaction amount: '))

# The Gensis Block
tx_amount = get_user_input()
add_value(tx_amount)

while True:
    tx_amount = get_user_input()
    add_value(tx_amount, get_last_blockchain_value())

    # Output blockchain to the console
    for block in blockchain:
        print('Outputting block')
        print(block)
# end while True

print('Done!')