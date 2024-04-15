from scraper2 import linkedin_scraper
from fastapi import FastAPI, Response, File, UploadFile, Response
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd
import os

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the LinkedIn Jobs Scraper API Service"}

@app.get("/run")
async def run_scrapy():
    page_number=0
    webpage='https://www.linkedin.com/jobs/search/?currentJobId=3876184250&geoId=102713980&keywords=data%20analyst&location=India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true'
    linkedin_scraper(webpage, page_number)
    return {"message": "Process completed successfully"}

@app.get("/get_csv")
async def get_csv():
    file_path = f"data/job_data.csv"
    with open(file_path, "rb") as file:
        file_content = file.read()
    return Response(content=file_content, media_type="application/octet-stream", headers={"Content-Disposition": "attachment; filename=job_data.csv"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)