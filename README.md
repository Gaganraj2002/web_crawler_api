# Web Crawler API

This project is a FastAPI-based web service that allows you to crawl a website up to a specified depth and retrieve all the links found. The API is designed to be fast, efficient, and easy to use. It is deployed on Platform.sh and can be accessed via the live link below.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Example](#example)
- [Live Usage](#live-usage)
- [Local Usage](#local-usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Gaganraj2002/web_crawler_api.git
   cd web_crawler_api
   ```

2. Create a virtual environment and activate it:

   ### For Windows:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   ### For macOS and Linux:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## API Endpoints

### 1. Root Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  {
    "message": "Welcome to the Web Crawler API!"
  }
  ```

### 2. Crawl Endpoint

- **URL**: `/crawl`
- **Method**: `POST`
- **Description**: Initiates a web crawl starting from the specified URL up to the specified depth.
- **Request Body**:
  ```json
  {
    "url": "https://example.com",
    "depth": 2
  }
  ```
- **Response**:
  ```json
  [
    "https://example.com",
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page1/subpage1",
    "https://example.com/page1/subpage2"
  ]
  ```

## Example

### Request

```bash
curl -X POST "http://127.0.0.1:8000/crawl" -H "Content-Type: application/json" -d '{"url": "https://example.com", "depth": 2}'
```

### Response

```json
[
  "https://example.com",
  "https://example.com/page1",
  "https://example.com/page2",
  "https://example.com/page1/subpage1",
  "https://example.com/page1/subpage2"
]
```

## Live Usage

The Web Crawler API is deployed on Platform.sh and can be accessed via the following live link:

[Live Link](https://main-bvxea6i-lvpxr7l2r2eog.fr-4.platformsh.site/)

### Live Request

```bash
curl -X POST "https://main-bvxea6i-lvpxr7l2r2eog.fr-4.platformsh.site/crawl" -H "Content-Type: application/json" -d '{"url": "https://example.com", "depth": 2}'
```

### Live Response

```json
[
  "https://example.com",
  "https://example.com/page1",
  "https://example.com/page2",
  "https://example.com/page1/subpage1",
  "https://example.com/page1/subpage2"
]
```

## Local Usage

To run the web crawler API locally, follow these steps:

1. Ensure you have completed the [Installation](#installation) steps.

2. Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Access the API at `http://127.0.0.1:8000`.
