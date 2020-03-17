# aws-recognition


### Copy images
```
$ aws s3 cp _analysis.png s3://my-bucket
```


### Detecting faces
```
$ aws rekognition list-faces --collection-id faces
$ aws rekognition list-faces --collection-id faces | grep ExternalImageId
$ python3 face_analysis.py
```
