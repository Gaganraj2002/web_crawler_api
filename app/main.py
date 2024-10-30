from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .crawler import crawl_website
from loguru import logger

app = FastAPI()


class CrawlRequest(BaseModel):
    url: str
    depth: int


@app.post("/crawl", response_model=list)
async def crawl(request: CrawlRequest):
    try:
        logger.info(
            f"Starting crawl for URL: {request.url} with depth: {request.depth}"
        )
        crawled_links = crawl_website(request.url, request.depth)
        logger.info(f"Finished crawl for URL: {request.url}")
        return crawled_links
    except Exception as e:
        logger.error(f"Error during crawl: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Web Crawler API!"}
