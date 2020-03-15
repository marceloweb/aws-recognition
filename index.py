import boto3

s3 = boto3.resource('s3')
client = boto3.client('rekognition')

def list_images():
    images = []
    bucket = s3.Bucket('fa-images-lab')
    for image in bucket.objects.all():
        images.append(image.key)
    return images

def index_collection(images):
    for i in images:
        response=client.index_faces(
                CollectionId='faces',
                DetectionAttributes=[
                ],
                ExternalImageId=i[:-4],
                Image={
                    'S3Object': {
                        'Bucket': 'fa-images-lab',
                        'Name': i,
                    },
                },
        )

images=list_images()
index_collection(images)
