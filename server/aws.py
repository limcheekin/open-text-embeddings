"""AWS Lambda function for the FastAPI endpoints.
"""
from mangum import Mangum
from embeddings import create_app

handler = Mangum(create_app())
