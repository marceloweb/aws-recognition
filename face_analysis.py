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

def list_faces_detected(faces_detected):
    face_id_detected = []
    for image in range(len(faces_detected['FaceRecords'])):
        face_id_detected.append(faces_detected['FaceRecords'][image]['Face']['FaceId'])
    return face_id_detected

def compare(faces_detected):
    result = []
    for i in faces_detected:
        result.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=i,
                FaceMatchThreshold=80,
                MaxFaces=10
            )
        )
    return result

faces_detected = detect_face()
faces_id_detected = list_faces_detected(faces_detected)
print(faces_id_detected)
