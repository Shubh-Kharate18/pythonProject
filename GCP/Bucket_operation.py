from google.cloud import storage

from google.cloud import bigquery

if __name__ == '_main_':
    storage_client = storage.Client()
    bucket = storage_client.bucket("bwt-creatbucket-session")
    bucket.storage_class="STANDARD"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print("bucket name: " + str(new_bucket.name))
    print("bucket storage class: " + str(new_bucket.storage_class))
    print("bucket location: " + str (new_bucket.location))



if __name__ == '__main__':
    obj=bigquery.client()