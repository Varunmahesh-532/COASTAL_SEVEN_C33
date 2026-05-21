from fastapi import FastAPI

app = FastAPI()

series_details = {
    109:{
        "name": "Harry Potter",
        "Auther": "Varun"
    },
    135:{
        "name": "THE BOYS",
        "Auther": "Mahesh"
    }
}
@app.get('/webseries/{series_id}')
def websires(series_id: int):
    series = series_details.get(series_id)
    if series:
        return series
    return {
        f"ERROR: Series not available with {series_id}"
    }
        
