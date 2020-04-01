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
    for ids in faces_detected:
        result.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=ids,
                FaceMatchThreshold=80,
                MaxFaces=10
            )
        )
    return result

def generation_json(result_comparation):
    json = []
    for face in result_comparation:
        if(len(face.get('FaceMatches'))) >= 1:
            profile = dict(name=face['FaceMatches'][0]['Face']['ExternalImageId'],
                            faceMatch=round(face['FaceMatches'][0]['Similarity'],2))
            json.append(profile)
    return json

def data_public(data_json):
    file = s3.Object('fa-site-lab','dados.json')
    file.put(Body=json.dumps(data_json))

faces_detected = detect_face()
faces_id_detected = list_faces_detected(faces_detected)
result_comparations = compare(faces_id_detected)
result_json = generation_json(result_comparations)
data_public(result_json)
print(json.dumps(result_json, indent=4))
