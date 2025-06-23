from google.cloud import storage

def upload_file(bucket_name, file_stream, filename):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_file(file_stream)

def get_files(bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    filenames = [blob.name for blob in blobs]
    return filenames