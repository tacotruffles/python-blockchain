# Initialize Blockchain
genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'John'


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    
    return blockchain[-1]


# Add a transaction to the open_transaction list. 
def add_transaction(recipient, sender=owner, amount=1.0):
    """ 
        Appends new value to the open transactions list.

        Arguments:
        :sender: The sender of coins.
        :recipient: The recipient of the coin amount.
        :amount: The amount of coins sent to the recipient (default = 1.0)
    """
    
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    open_transactions.append(transaction)
    

    # if last_transaction == None:
        # last_transaction = [1]


    #blockchain.append([last_transaction, transaction_amount])

# Combines open transactions and hashes previous block
# transaction_amount, last_transaction=[1]
def mine_block():
    ''' 
        Takes all the open transactions and puts them into a block on the blockchain

        Arguments:
        :transaction_amount: The amount added to the blockchain.
        :last_transaction: The last blockchain transaction (default [1]).
    '''
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    
    blockchain.append(block)


def get_transaction_value():
    """ Returns the input of the user transaction amount as a float. """
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount: '))
    return (tx_recipient, tx_amount)

def get_user_choice():
    user_input = input('Enter your choice: ')
    return user_input

def print_open_transactions():
    print('-' * 20)
    print(open_transactions)
    print('-' * 20)

def print_blockchain_elements():
    print('-' * 20)
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)

def verify_blockchain():
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        if blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break
    return is_valid


waiting_for_input = True

while waiting_for_input:
    print('Please choose a menu f(x):')
    print('(1) Add a new transaction')
    print('(2) Mine block')
    print('(3) Print print blockchain')
    print('(h) Manipulate the blockchaine')
    print('(q) Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        # Unpack tx_data Tuple
        recipient, amount = tx_data

        add_transaction(recipient, amount=amount)
        print_open_transactions()
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please select a value from the list!')

    # Verify Blockchain
    # if not verify_blockchain():
    #     print_blockchain_elements()
    #     print('Invalid blockchain!')
    #     break
else:
    print('Done!')
# end while True

# Program complete