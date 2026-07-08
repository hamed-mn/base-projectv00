from web3 import Web3

# 1. Connect to the network (replace with your RPC URL)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

# 2. Set up your wallet
private_key = 'YOUR_PRIVATE_KEY'
account = w3.eth.account.from_key(private_key)

# 3. Define the contract
contract_address = '0xYourContractAddressHere'
contract_abi = '[{"inputs":[],"name":"yourFunctionName","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# 4. Build the transaction dictionary
transaction = contract.functions.yourFunctionName().build_transaction({
    'chainId': 1, # e.g., 1 for Ethereum Mainnet
    'gas': 2000000,
    'maxFeePerGas': w3.to_wei('2', 'gwei'),
    'maxPriorityFeePerGas': w3.to_wei('1', 'gwei'),
    'nonce': w3.eth.get_transaction_count(account.address),
})

# 5. Sign and broadcast the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

print(f"Transaction successful! Hash: {w3.to_hex(txn_hash)}")
hssssdwwsswsssasdasdjhhjklkjkklljkhhhi  h u h hkih 
