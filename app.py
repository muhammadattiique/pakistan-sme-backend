from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session


import crud
import schemas


from database import (
    Base,
    engine,
    get_db,
)


from services.collector import collect_city
from services.enrichment_service import run_enrichment
from services.search_engine import search_businesses
from services.export_service import export_businesses


from services.ai_search import (
    create_index,
    semantic_search,
)


# ==================================================
# DATABASE
# ==================================================

Base.metadata.create_all(bind=engine)


# ==================================================
# APP
# ==================================================

app = FastAPI(

    title="Pakistan SME Intelligence Platform",

    version="4.0.0",

    description=
    "Pakistan SME Data Collection, AI Search, WhatsApp Intelligence and Automation"

)


# ==================================================
# CORS
# ==================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)



# ==================================================
# BASIC
# ==================================================

@app.get("/")
def root():

    return {

        "message":
        "Pakistan SME Intelligence Platform",

        "version":
        "4.0.0",

        "status":
        "running"

    }



@app.get("/health")
def health():

    return {

        "status":
        "healthy"

    }




# ==================================================
# COLLECTION
# ==================================================

@app.post("/collect")
def collect(

    city: str,

    db: Session = Depends(get_db)

):

    return collect_city(
        city,
        db
    )



# n8n friendly endpoint

@app.post("/collect/{city}")
def collect_automation(

    city: str,

    db: Session = Depends(get_db)

):

    return collect_city(
        city,
        db
    )





# ==================================================
# ENRICHMENT
# ==================================================

@app.post("/enrich")
def enrich(

    batch_size: int = 50,

    db: Session = Depends(get_db)

):

    result = run_enrichment(
        db,
        batch_size
    )


    return {

        "message":
        "Enrichment completed",

        "result":
        result

    }





# ==================================================
# BUSINESSES
# ==================================================

@app.get("/businesses")
def get_businesses(

    page: int = 1,

    limit: int = 20,

    db: Session = Depends(get_db)

):

    return crud.get_businesses(

        db,

        page,

        limit

    )




@app.get(
    "/businesses/{business_id}",
    response_model=schemas.Business
)
def get_business(

    business_id:int,

    db:Session=Depends(get_db)

):

    business = crud.get_business(
        db,
        business_id
    )


    if not business:

        raise HTTPException(

            status_code=404,

            detail="Business not found"

        )


    return business





@app.post(
    "/businesses",
    response_model=schemas.Business
)
def create_business(

    business:schemas.BusinessCreate,

    db:Session=Depends(get_db)

):

    return crud.create_business(
        db,
        business
    )





# ==================================================
# FILTERS
# ==================================================

@app.get("/cities")
def cities(

    db:Session=Depends(get_db)

):

    return crud.get_cities(db)



@app.get("/industries")
def industries(

    db:Session=Depends(get_db)

):

    return crud.get_industries(db)





# ==================================================
# SEARCH
# ==================================================

@app.get(
    "/search",
    response_model=list[schemas.Business]
)
def search(

    keyword:str|None=None,

    city:str|None=None,

    industry:str|None=None,

    db:Session=Depends(get_db)

):

    return crud.search_businesses(

        db,

        keyword,

        city,

        industry

    )





@app.get(
    "/advanced-search",
    response_model=list[schemas.Business]
)
def advanced_search(

    keyword:str|None=None,

    city:str|None=None,

    industry:str|None=None,

    db:Session=Depends(get_db)

):

    return search_businesses(

        db,

        keyword,

        city,

        industry

    )





# ==================================================
# EXPORT
# ==================================================

@app.get("/export")
def export(

    db:Session=Depends(get_db)

):

    file_path = export_businesses(db)


    return FileResponse(

        path=file_path,

        filename="businesses.csv",

        media_type="text/csv"

    )





# ==================================================
# AI SEARCH
# ==================================================

@app.post("/ai/create-index")
def create_ai_index(

    db:Session=Depends(get_db)

):

    return create_index(db)





# n8n AI refresh endpoint

@app.post("/ai/update")
def update_ai_index(

    db:Session=Depends(get_db)

):

    return create_index(db)





@app.get("/ai-search")
def ai_search(

    query:str,

    limit:int=10,

    db:Session=Depends(get_db)

):

    return semantic_search(

        db,

        query,

        limit

    )





# ==================================================
# AUTOMATION STATUS
# ==================================================

@app.get("/automation-status")
def automation_status():

    return {

        "collector":
        "available",

        "ai_index":
        "available",

        "n8n_ready":
        True

    }





# ==================================================
# STATISTICS
# ==================================================

@app.get("/stats")
def stats(

    db:Session=Depends(get_db)

):

    cities = crud.get_cities(db)

    industries = crud.get_industries(db)


    return {

        "total_businesses":
        crud.count_businesses(db),

        "total_cities":
        len(cities),

        "total_industries":
        len(industries)

    }