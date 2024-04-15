from scraper2 import linkedin_scraper
from fastapi import FastAPI, Response, File, UploadFile, Response
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd
import os

app = FastAPI()

@app.get("/run")
async def run_scrapy():
    page_number=0
    webpage='https://www.linkedin.com/jobs/search/?currentJobId=3876184250&geoId=102713980&keywords=data%20analyst&location=India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true'
    linkedin_scraper(webpage, page_number)
    return {"message": "Process completed successfully"}

@app.get("/get_csv")
async def get_csv(response: Response):
    file_path = f"data/job_data.csv"
    if os.path.exists(file_path):
        response.headers["Content-Disposition"] = f"attachment; filename=data/job_data.csv"
        response.headers["Content-Type"] = "text/csv"
        with open(file_path, "r") as file:
            return file.read()
    else:
        return {"error": "File not found"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)