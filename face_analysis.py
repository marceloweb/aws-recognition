import boto3
import json

s3 = boto3.resource('s3')
client = boto3.client('rekognition')

def detect_face():
        faces_detected=client.index_faces(
            CollectionId='faces',
            DetectionAttributes=['DEFAULT'],
            ExternalImageId='TEMP',
            Image={
                'S3Object': {
                    'Bucket': 'fa-images-lab',
                    'Name': '_analysis.png'
                }
            }
        )
        return faces_detected

faces_detected=detect_face()
print(json.dumps(faces_detected, indent=4))
