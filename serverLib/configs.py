import datetime

MAX_STORE: int = 5 # Number of store boxes
DATABASE: str = "lostProperty.db" # Database file
EXPIRY_TIME: datetime.timedelta = datetime.timedelta(hours=3) # Time until item expires
PAGE_SIZE: int = 5 # Items per catalogue page