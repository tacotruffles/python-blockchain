# Initialize Blockchain
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ 
        Appends new value and the last value of the blockchain. 

        Arguments:
        :transaction_amount: The amount added to the blockchain.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    """ Returns the input of the user transaction amount as a float. """
    return float(input('Your transaction amount: '))

def get_user_choice():
    user_input = input('Enter your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)
    print('Blockchain output completed.')

def verify_blockchain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break
        block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose a menu f(x):')
    print('(1) Add a new transaction to the blockchain')
    print('(2) Print the blockchain')
    print('(h) Manipulate the blockchaine')
    print('(q) Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_user_input()
        add_value(tx_amount, get_last_blockchain_value())
        print('Transaction Added.')
    elif user_choice == '2':
        # Output blockchain to the console
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please select a value from the list!')

    if not verify_blockchain():
        print('Invalid blockchain!')
        break

# end while True

# Program complete
print('Done!')