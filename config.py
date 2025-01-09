import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Flask Secret Key for Sessions and CSRF Protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or '988b7feb-9a3e-4c2a-a2b7-c7129e326334'

    # Azure Blob Storage Configuration
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'pdmflaskstorageaccount'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or (
        "DefaultEndpointsProtocol=https;"
        "AccountName=pdmflaskstorageaccount;"
        "AccountKey=n4lrttoYGFsgwVtWnsj0/NNlxSQXOurLGMcMgy8LFSVzHz48eaRvTqVZtnnkKejG12b+LaHKZhF3+AStL9WLWg==;"
        "EndpointSuffix=core.windows.net"
    )
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Add SAS Token and URL for Blob Container Access
    BLOB_SAS_TOKEN = os.environ.get('BLOB_SAS_TOKEN') or (
        "sp=racwdli&st=2025-01-07T00:32:30Z&se=2025-01-15T08:32:30Z&sv=2022-11-02&sr=c&sig=Pyi6A7LIH8oe9H8ByCiaKbVLdvC49s0R3gJHqO7bHD8%3D"
    )
    BLOB_SAS_URL = os.environ.get('BLOB_SAS_URL') or (
        "https://pdmflaskstorageaccount.blob.core.windows.net/images"
    )

    # Azure SQL Database Configuration
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'pdmflasksqlserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'pdmflasksqldb'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'pdmsqladmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'pdm-admin-2025#!'

    # SQLAlchemy Database URI (Adjust driver if necessary)
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+18+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication (MSAL)
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or "IhC8Q~YAAGO_C6Nvq1i4Gvtw45KLaHDyxbqtebea"
    CLIENT_ID = os.environ.get('CLIENT_ID') or "79b517eb-b734-4d7d-b831-4173fe9cf6fc"
    AUTHORITY = os.environ.get('AUTHORITY') or "https://login.microsoftonline.com/common"
    REDIRECT_PATH = os.environ.get('REDIRECT_PATH') or "/getAToken"

    # Microsoft Graph API Permissions Scope
    SCOPE = ["User.Read"]

    # Flask Session Configuration
    SESSION_TYPE = os.environ.get('SESSION_TYPE') or "filesystem"
