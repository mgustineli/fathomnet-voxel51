from google.cloud import storage
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def check_gcp_auth():
    print(
        f"Checking auth for credentials: {os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', 'Using Default/User Auth')}"
    )

    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    print(f"Using project ID: {project_id}")

    try:
        # distinct from just logging in, this checks if the library can actually authorize
        client = storage.Client(project=project_id)
        print(f"✅ SUCCESS! Authenticated with Project ID: {client.project}")

        # Optional: Verify you can actually read from your specific bucket
        bucket_name = "voxel51-test"
        bucket = client.bucket(bucket_name)
        if bucket.exists():
            print(f"✅ Verified access to bucket: gs://{bucket_name}")
        else:
            print(f"⚠️ Authenticated, but cannot find bucket: gs://{bucket_name}")

    except Exception as e:
        print(f"❌ FAILED. Error details: {e}")
        print(
            "Tip: Run 'gcloud auth application-default login' or set GOOGLE_APPLICATION_CREDENTIALS"
        )


if __name__ == "__main__":
    check_gcp_auth()
