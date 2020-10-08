import boto3

s3 = boto3.client('s3')

def download(file, bucket_name):
  try:
    image = s3.get_object(
      Bucket=bucket_name, 
      Key=file,
      ResponseContentType='image/jpg')
    
    return image['Body'].read()

  except Exception as e:
    # Todo: Improve
    print("Something Happened: ", e)


def upload(file, bucket_name):
  try:
    file.seek(0)
    s3.put_object(
        Body=file.stream,
        Bucket=bucket_name,
        Key=file.filename,
        ContentType='multipart/form-data'
    )

  except Exception as e:
    # Todo: Improve
    print("Something Happened: ", e)
    return e

  return f'http://{bucket_name}.s3.amazonaws.com/{file.filename}' 
