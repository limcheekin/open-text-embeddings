"""AWS Lambda function for the FastAPI endpoints.
"""
from mangum import Mangum
from open.text.embeddings.server.app import create_app

handler = Mangum(create_app())
