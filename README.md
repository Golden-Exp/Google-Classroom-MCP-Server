# Google Classroom MCP Server

This is a Model Context Protocol (MCP) server that integrates with Google Classroom API. Currently, it supports retrieving courses from Google Classroom.

## Setup

1. Install dependencies:
```bash
npm install
```

2. Set up Google Cloud Project and OAuth 2.0 credentials:
   - Go to Google Cloud Console
   - Create a new project
   - Enable Google Classroom API
   - Create OAuth 2.0 credentials
   - Download the credentials and save them securely

3. Start the server:
```bash
npm start
```

## Available Tools

### get_courses
Retrieves a list of Google Classroom courses.

Parameters:
- `pageSize` (optional): Maximum number of courses to return
- `pageToken` (optional): Token for the next page of courses

## Note
This is a basic implementation. You'll need to add proper authentication by implementing the OAuth2 flow with Google.