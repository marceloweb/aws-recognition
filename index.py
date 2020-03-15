import boto3

s3 = boto3.resource('s3')

def list_images():
    images = []
    bucket = s3.Bucket('fa-images-lab')
    for image in bucket.objects.all():
        images.append(image.key)
    print(images)
    return images

images=list_images()
