from dataclasses import dataclass, field
from datetime import datetime
from functools import wraps
from typing import List, Optional


# Deorator
def log_action(action_name: Optional[str] = None):
    """Decorator to log method calls with timestamps and results.
    Demonstrates a parameterized decorator."""
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            timestamp = datetime.now()
            action = action_name or func.__name__
            print(f"[{timestamp}] Starting {action} for {self.__class__.__name__}"
                  f"(Account: {getattr(self, 'account_number', 'N/A')})")
            
            try:
                result = func(self, *args, **kwargs)
                print(f"[{datetime.now()}] Completed {action} successfully. Result: {result}")
                return result
            except Exception as e:
                print(f"[{datetime.now()}] ERROR in {action}: {e}")
                raise
        return wrapper
    return decorator

# DataClass
@dataclass
class Transaction:
    """Immutable data container for financial transactions."""
    amount: float
    transaction_type: str # 'deposit', 'withdrawl', 'interest'
    timestamp: datetime = field(default_factory=datetime.now)
    description: str = ""

@dataclass
class Customer:
    """Customer data using dataclass for automatic __init__, __repr__, etc."""
    customer_id: str
    name: str
    email: str
    phone: str
    accounts: List['BankAccount'] = field(default_factory=list)
    
    def add_account(self, account: 'BankAccount'):
        self.accounts.append(account)
        print(f"Added {account.__class__.__name__} to customer {self.name}")

# OOP - Base Class

class BankAccount:
    """Base Class demonstrating encapsulation and basic OOP principles."""
    
    def __init__(self, account_number: str, customer: Customer, initial_balance: float = 0.0):
        self.account_number = account_number
        self.customer = customer
        self._balance: float = initial_balance # protected attribute
        self._transactions: List[Transaction] = []
        self.customer.add_account(self)
    
    @property
    def balance(self):
        """Encapsulation: controlled access to balance."""
        return self._balance
    
    @log_action("Deposit")
    def deposit(self, amount: float, description: str = "Deposit") -> bool:
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._transactions.append(
            Transaction(amount, "deposit", description=description)
        )
        return True
    
    @log_action("Withdrawal")
    def withdraw(self, amount: float, description: str = "Withdrawl") -> bool:
        """Withdraw money with validation."""
        if amount <= 0:
            raise ValueError("Withdrawl amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        self._transactions.append(
            Transaction(amount, "withdrawal", description=description)
        )
        return True
    
    def get_transaction_history(self) -> List[Transaction]:
        """Return copy of transaction history (encapsulation)."""
        return self._transactions
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.account_number}, Balance: ${self.balance:.2f})"


# INHERITENCE & POLYMORPHISM
class SavingsAccount(BankAccount):
    """Inherited class with additional features (interest)."""
    
    def __init__(self, account_number: str, customer: Customer, 
                 initial_balance: float = 0.0, interest_rate: float = 0.03):
        super().__init__(account_number, customer, initial_balance)
        self.interest_rate = interest_rate

    @log_action("Apply Interest")
    def apply_interest(self) -> float:
        """Polymorphic behavior specific to SavingsAccount."""
        interest = self.balance * self.interest_rate
        self.deposit(interest, description="Monthly Interest")
        return interest


class CheckingAccount(BankAccount):
    """Another derived class with overdraft protection (limited)."""
    
    def __init__(self, account_number: str, customer: Customer, 
                 initial_balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(account_number, customer, initial_balance)
        self.overdraft_limit = overdraft_limit

    @log_action("Withdrawal (Checking)")
    def withdraw(self, amount: float, description: str = "Withdrawal") -> bool:
        """Overridden method demonstrating polymorphism."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > (self.balance + self.overdraft_limit):
            raise ValueError("Exceeds overdraft limit")
        
        self._balance -= amount
        self._transactions.append(
            Transaction(amount, "withdrawal", description=description)
        )
        return True

