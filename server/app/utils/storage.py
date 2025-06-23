from google.cloud import storage

def upload_file(bucket_name, file_stream, filename):
    from google.api_core.exceptions import GoogleAPIError
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(filename)
        file_stream.seek(0)  # לוודא שמתחילים מההתחלה
        blob.upload_from_file(file_stream)
        print(f"Uploaded {filename} to bucket {bucket_name}")
    except GoogleAPIError as e:
        print(f"Google API error: {e}")
        raise
    except Exception as e:
        print(f"General error: {e}")
        raise


def get_files(bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs()
    filenames = [blob.name for blob in blobs]
    return filenames