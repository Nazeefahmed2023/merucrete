from supabase import create_client
from django.conf import settings

from io import BytesIO

# Ensure these are set in settings.py
SUPABASE_URL = getattr(settings, "SUPABASE_URL", None)
SUPABASE_KEY = getattr(settings, "SUPABASE_KEY", None)
SUPABASE_BUCKET = getattr(settings, "SUPABASE_BUCKET", None)

if not SUPABASE_URL or not SUPABASE_KEY or not SUPABASE_BUCKET:
    raise ValueError("Supabase settings are missing! Add SUPABASE_URL, SUPABASE_KEY, and SUPABASE_BUCKET to settings.py.")

# Create Supabase client
_supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_file_and_get_public_url(file, file_name):
    """
    Uploads a file to Supabase Storage and returns its public URL.
    If the file already exists, it overwrites it.
    """
    # Read file content
    file_content = file.read()

    # Upload (with upsert=True to overwrite if exists)
    _supabase.storage.from_(SUPABASE_BUCKET).upload(
        path=file_name,
        file=file_content,
        file_options={"contentType": file.content_type, "upsert": True}
    )

    # Get public URL
    public_url = _supabase.storage.from_(SUPABASE_BUCKET).get_public_url(file_name)

    # Reset file pointer so Django can save it locally if needed
    file.seek(0)

    return public_url
