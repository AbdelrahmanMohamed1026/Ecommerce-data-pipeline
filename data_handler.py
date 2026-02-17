from data_validator import validate_transaction

def process_file(data_path):
    
    processed_transactions = []
    unique_regions = set()      # Using set to remove duplicates
    try:
        with open(data_path, "r") as f:
            print("File successfully opened")
            
            for line in f:
                # Remove new lines and spaces
                raw_line= line.strip()
                try:
                    if validate_transaction(raw_line):
                        transaction= [p.strip() for p in raw_line.split(",")]
                        
                        transaction_id = transaction[0]
                        transaction_amount= transaction[1]
                        transaction_region= transaction[2]
                        transaction_date= transaction[3]
                        
                        transacrion_dict= {
                            "id": transaction_id,
                            "amount": transaction_amount,
                            "region": transaction_region,
                            "date": transaction_date 
                        }
                        
                        processed_transactions.append(transacrion_dict)
                        unique_regions.add(transaction_region)
                    else:
                        print(f"Skipping malformed line (invalid field count): {raw_line}")
                except (ValueError, IndexError) as e:
                    print(f"Error processing line '{raw_line}': {e}. Skipping...")
                    continue
                
            
    except FileNotFoundError:
        print("File not found")
    finally:
        print("File has been processed")
        
    return processed_transactions, unique_regions


def save_processed_data(data):
    with open("processed_data.txt", "w") as f:
        for record in data:
            f.write(str(record) + "\n")
    f.close()
    
if __name__== "__main__":
    clean_list, regions= process_file("raw_transactions.txt")
    
    save_processed_data(clean_list)
    print(f"Successfully saved {len(clean_list)} records.")