# config.py
class Config:
    SECRET_KEY = 'your-secret-key'  # Your app's secret key for session handling
    PAYPAL_CLIENT_ID = "your-client-id"
    PAYPAL_CLIENT_SECRET = "your-client-secret"
    PAYPAL_API_BASE = "https://api-m.sandbox.paypal.com"  # For production, use 'https://api-m.paypal.com'
