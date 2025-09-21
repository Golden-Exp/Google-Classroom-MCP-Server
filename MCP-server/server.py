from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import json

# Initialize FastMCP server
mcp = FastMCP("Google-Classroom-MCP")

# Constants
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']

# Load client_id and client_secret from config.json
CONFIG_PATH = r"D:\code\Google-Classroom-MCP-Server\MCP-server\config.json"
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)
CLIENT_ID = config['web']['client_id']
CLIENT_SECRET = config['web']['client_secret']
AUTH_URI = config['web']['auth_uri']
TOKEN_URI = config['web']['token_uri']
REDIRECT_URI = config['web']['redirect_uri']
print(CLIENT_ID, CLIENT_SECRET)

def get_credentials():
    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "auth_uri": AUTH_URI,
                "token_uri": TOKEN_URI,
                "redirect_uri": REDIRECT_URI
            }
        },
        SCOPES
    )
    creds = flow.run_local_server(port=3000)
    return creds


@mcp.tool()
def list_courses():
    """
    Retrieve a list of Google Classroom courses accessible by the authenticated user.

    Returns:
        A list of dictionaries where each dictionary contains details for a course:
        - id: The unique identifier of the course.
        - name: The name of the course.

    Raises:
        Exception: If the Google Classroom API request fails.
    """
    creds = get_credentials()
    service = build('classroom', 'v1', credentials=creds)
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])
    return [{"id": c['id'], "name": c['name']} for c in courses]


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
