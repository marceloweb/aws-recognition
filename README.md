# aws-recognition

### Download AWS Cli

### Configure
```
$ aws configure
```

### Sync local images with bucket
```
$ aws s3 sync . s3://fa-images-lab
```

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
