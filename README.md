# Web Crawler API

This project is a FastAPI-based web service that allows you to crawl a website up to a specified depth and retrieve all the links found. The API is designed to be fast, efficient, and easy to use.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Example](#example)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- Pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/web-crawler-api.git
   cd web-crawler-api
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the web crawler API, use the following command:

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

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
