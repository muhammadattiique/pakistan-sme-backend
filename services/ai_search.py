import os
import pickle

import faiss
from sentence_transformers import SentenceTransformer
from sqlalchemy.orm import Session

from models import Business

from services.ranking_service import rank_businesses



MODEL_NAME = "all-MiniLM-L6-v2"


INDEX_FILE = "business_index.faiss"

DATA_FILE = "business_data.pkl"



model = SentenceTransformer(
    MODEL_NAME
)



# ==========================================================
# CREATE AI INDEX
# ==========================================================

def create_index(
    db: Session
):

    businesses = (
        db.query(Business)
        .all()
    )


    if not businesses:

        return {

            "message":
            "No businesses available"

        }



    texts = []

    ids = []



    for business in businesses:


        text = " ".join([

            business.name or "",

            business.industry or "",

            business.city or "",

            business.address or "",

            business.website or "",

            business.phone or "",

            business.email or "",

            business.whatsapp or "",

            business.source or "",

        ]).lower()



        texts.append(text)


        ids.append(
            business.id
        )



    vectors = model.encode(

        texts,

        convert_to_numpy=True,

        normalize_embeddings=True,

        show_progress_bar=True,

    )



    dimension = vectors.shape[1]



    index = faiss.IndexFlatIP(
        dimension
    )



    index.add(
        vectors
    )



    faiss.write_index(

        index,

        INDEX_FILE

    )



    with open(

        DATA_FILE,

        "wb"

    ) as file:


        pickle.dump(

            ids,

            file

        )



    return {


        "message":

        "AI index created successfully",


        "businesses":

        len(ids)


    }





# ==========================================================
# AI SEMANTIC SEARCH + RANKING
# ==========================================================

def semantic_search(

    db: Session,

    query: str,

    limit: int = 10,

):


    if not os.path.exists(INDEX_FILE):

        return {


            "error":

            "AI index not found. Create the index first."


        }



    index = faiss.read_index(

        INDEX_FILE

    )



    query_vector = model.encode(

        [query.lower()],

        convert_to_numpy=True,

        normalize_embeddings=True,

    )



    scores, positions = index.search(

        query_vector,

        limit * 3,

    )



    with open(

        DATA_FILE,

        "rb"

    ) as file:

        ids = pickle.load(file)



    results = []



    for score, position in zip(

        scores[0],

        positions[0]

    ):


        if position >= len(ids):

            continue



        business = (

            db.query(Business)

            .filter(

                Business.id == ids[position]

            )

            .first()

        )



        if business:


            business.ai_score = round(

                float(score),

                3

            )


            results.append(

                business

            )



    # Apply B2B ranking

    ranked = rank_businesses(

        results,

        query

    )



    return ranked[:limit]