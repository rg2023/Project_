from google.cloud import storage

def upload_file(bucket_name, file):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

def upload_file_from_path(bucket_name, file_path):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(os.path.basename(file_path))
    with open(file_path, "rb") as f:
        blob.upload_from_file(f)

def get_files(bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    filenames = [blob.name for blob in blobs]
    return filenames