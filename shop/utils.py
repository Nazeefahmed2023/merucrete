from supabase import create_client
from django.conf import settings

# Connect to Supabase
_supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

def upload_file_and_get_public_url(file, file_name):
    """
    Uploads a file to Supabase storage and returns the public URL
    """
    bucket = settings.SUPABASE_BUCKET

    # Upload file
    _supabase.storage.from_(bucket).upload(file_name, file)

    # Get public URL
    public_url = _supabase.storage.from_(bucket).get_public_url(file_name)
    return public_url
