import ast      # Safe way to convert string representation of dict to actual dict

class Transaction():
    def __init__(self, id, amount, region, date):
        self._id = id
        self._amount= amount
        self._region= region
        self._date = date
        
    def get_details(self):
        return (f"Transaction id: {self._id},\n Amount of transaction is {self._amount} and region is {self._region} on date of {self._date}")
        
        
class InternationalTransaction(Transaction):
    def __init__(self, id, amount, region, date, currency_code):
        super().__init__(id, amount, region, date)
        self._currency_code= currency_code
        
    def get_details(self):
        # Overriding to include the currency code
        base_details = super().get_details()
        return f"{base_details}, Currency: {self._currency_code}"
        
class DataLoader():
    def __init__(self):
        self.transactions= []
    
    @staticmethod    
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False
        
    def load_transactions(self, filepath):
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    # Convert string line back to dictionary
                    data_dict = ast.literal_eval(line.strip())
                    
                    # Get the value of amount to check if it is greater than 0
                    amt = data_dict.get('amount', 0)
                    
                    if self.validate_amount(amt):
                        # Check for which class to use
                        if 'currency_code' in data_dict:
                            obj = InternationalTransaction(
                                data_dict['id'], data_dict['amount'], 
                                data_dict['region'], data_dict['date'],
                                data_dict['currency_code']
                            )
                        else:
                            obj = Transaction(
                                data_dict['id'], data_dict['amount'], 
                                data_dict['region'], data_dict['date']
                            )
                        
                        self.transactions.append(obj)
                        
        except FileNotFoundError:
            print(f"Error: {filepath} not found.")
        