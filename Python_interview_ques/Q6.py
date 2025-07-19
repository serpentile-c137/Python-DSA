# Error Handling Best Practices in Pipelines

# Always log errors:
import logging

try:
    risky_job()
except Exception as e:
    logging.error(f"Error: {e}")

# Raise custom exceptions for clarity.
