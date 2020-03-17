import boto3
import json

client = boto3.client('rekognition')
s3 = boto3.resource('s3')

def detect_faces():
