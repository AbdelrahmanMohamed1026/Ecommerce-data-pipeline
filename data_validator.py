def validate_transaction(record):
    # Splitting the string by comma to check field count
    fields = record.split(',')
    
    if len(fields) == 4:
        return True
    else:
        return False


def clean_and_structure(raw_data_list):
    clean_transactions = []
    
    for record in raw_data_list:
        if validate_transaction(record):
            # Strip whitespace and split
            parts = [p.strip() for p in record.split(',')]
            
            # Structuring the data: (ID, Amount: float, Currency, Date)
            structured_record = (
                parts[0], 
                float(parts[1]), 
                parts[2], 
                parts[3]
            )
            clean_transactions.append(structured_record)
            
    return clean_transactions


def calculate_total_sales(transaction_list):
    # If the list is empty then the sum is 0
    if len(transaction_list) ==0:
        return 0.0 
       
    # Calculating the total sales using recursion 
    return transaction_list[0][1] + calculate_total_sales(transaction_list[1:])


# Lambda function to extract the transaction ID (Index 0 of the tuple)
get_transaction_id = lambda transaction: transaction[0]