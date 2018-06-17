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

def get_user_choice():
    user_input = input('Enter your choice: ')
    return user_input

def print_blockchain():
    print('Outputting block')
    print(block)
    print('Blockchain output completed.')

# The Gensis Block
tx_amount = get_user_input()
add_value(tx_amount)

while True:
    print('Please choose a menu f(x):')
    print('(1) Add a new transaction to the blockchain')
    print('(2) Print the blockchain')
    print('(q) Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_user_input()
        add_value(tx_amount, get_last_blockchain_value())
        print('Transaction Added.')
    elif user_choice == '2':
        # Output blockchain to the console
        for block in blockchain:
            print_blockchain()
    elif user_choice == 'q':
        break
    else:
        print('Input was invalid, please select a value from the list!')

# end while True

# Program complete
print('Done!')