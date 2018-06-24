# Initialize Blockchain
MINING_REWARD = 10 #coins
genesis_block = {'previous_hash': '', 'index': 0, 'transactions': []}
blockchain = [genesis_block]
open_transactions = []
owner = 'John'
participants = {'John'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    # Gather past transactions on the blockchain
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]

    # Including any open transactions that haven't been mined yet
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant] 
    tx_sender.append(open_tx_sender)

    # Calculate total amount sent by sender
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    
    # Gather past transactions received by sender
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]

    # Gather any pending coins to be received by sender
    """ TODO: ???????? """
    
    # Calculate the total amount received by sender
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_received - amount_sent

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    
    return blockchain[-1]

def verify_transaction(transaction):
    """
        Make sure sender has enough coins to send for the current transaction
    """
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']



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

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True

    return False
    

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
    hashed_block = hash_block(last_block)

    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }

    # Clone the open transaction list to avoid issues with failed mining of this block
    copied_transactions = open_transactions[:]

    copied_transactions.append(reward_transaction)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    
    blockchain.append(block)
    return True


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
    ''' Validate current blockchain '''
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False

    return True


waiting_for_input = True

while waiting_for_input:
    print('Please choose a menu f(x):')
    print('(1) Add a new transaction')
    print('(2) Mine block')
    print('(3) Print print blockchain')
    print('(4) Output participants')
    print('(h) Manipulate the blockchain')
    print('(q) Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        # Unpack tx_data Tuple
        recipient, amount = tx_data

        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed.')
        print_open_transactions()
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 'index': 0, 'transactions': [{'sending': 'Bilbo', 'recipient': 'Gollum', 'amount': 23.0}]}
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please select a value from the list!')

    # Verify Blockchain
    if not verify_blockchain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
    print("SENDER BALANCE: " + str(get_balance('John')))
else:
    print('Done!')
# end while True

# Program complete