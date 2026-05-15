import os
import requests

# Fake API keys
OPENAI_API_KEY = "sk-fake-DO-NOT-USE-1234567890abcdef"
ANTHROPIC_API_KEY = "sk-ant-fake-DO-NOT-USE-abcdef1234567890"
STRIPE_SECRET_KEY = "sk_test_FAKE_DO_NOT_USE_51MxExampleKeyHere"
GITHUB_TOKEN = "ghp_FAKE_DO_NOT_USE_1234567890abcdefghijklmnop"

# Fake AWS credentials
AWS_ACCESS_KEY_ID = "AKIAFAKEKEY1234567890"
AWS_SECRET_ACCESS_KEY = "fakeSecretAccessKey_DO_NOT_USE_1234567890abcdef"

# Fake database connection string
DATABASE_URL = (
    "postgresql://admin:FakePassword123!"
    "@prod-db.example.internal:5432/customer_data"
)

# Fake JWT
JWT_TOKEN = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "FAKEPAYLOADDO_NOT_USE."
    "FAKESIGNATURE1234567890"
)

# Fake Slack webhook
SLACK_WEBHOOK_URL = (
    "https://hooks.slack.com/services/"
    "T00000000/B00000000/FAKE_DO_NOT_USE_WEBHOOK"
)

# Fake private key
PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKE
DO NOT USE THIS KEY THIS IS ONLY TEST DATA
FAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKEFAKE
-----END RSA PRIVATE KEY-----
"""

# Fake config object
CONFIG = {
    "environment": "production",
    "admin_email": "admin@example.com",
    "api_key": OPENAI_API_KEY,
    "db_password": "FakeProdPassword_DO_NOT_USE_2026!",
    "encryption_key": "fake_32_byte_encryption_key_0000",
}


def call_fake_api():
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "X-API-Key": STRIPE_SECRET_KEY,
    }

    response = requests.get(
        "https://api.example.com/v1/customers",
        headers=headers,
        timeout=10,
    )

    return response.json()


def load_secret_from_env():
    return os.getenv("PROD_SECRET_KEY", "fake_env_secret_DO_NOT_USE")


if __name__ == "__main__":
    print("This file contains fake secrets for testing scanners only.")
