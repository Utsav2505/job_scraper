from scraper2 import linkedin_scraper
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd

app = FastAPI()

@app.get("/run")
async def run_scrapy():
    page_number=0
    webpage='https://www.linkedin.com/jobs/search/?currentJobId=3876184250&geoId=102713980&keywords=data%20analyst&location=India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true'
    linkedin_scraper(webpage, page_number)
    return {"message": "Process completed successfully"}

@app.get("/get_csv")
async def get_csv():
    csv_file_path = "data/job_data.csv" 
    df = pd.read_csv(csv_file_path)
    csv_string = df.to_csv(index=False)
    headers = {
        "Content-Disposition": "attachment; filename=job_data.csv",
        "Content-Type": "text/csv",
    }
    return Response(content=csv_string, status_code=200, headers=headers)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)