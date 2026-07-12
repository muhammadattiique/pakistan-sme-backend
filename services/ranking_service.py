from models import Business



def calculate_score(
    business: Business,
    query: str
):

    score = 0



    # AI similarity

    score += getattr(
        business,
        "ai_score",
        0
    ) * 50



    # Contact quality

    if business.website:
        score += 15


    if business.email:
        score += 15


    if business.phone:
        score += 10


    if business.whatsapp:
        score += 20



    # Name relevance

    if query.lower() in business.name.lower():

        score += 20



    return score





def rank_businesses(

    businesses,

    query

):

    return sorted(

        businesses,

        key=lambda x:

        calculate_score(

            x,

            query

        ),

        reverse=True

    )