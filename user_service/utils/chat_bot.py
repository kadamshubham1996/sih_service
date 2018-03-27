from flask import current_app as app


def get_resopnse_from_bot(query):
    response = app.bot.get_response(query)
    if response.confidence > 0.7:
        data = response.serialize()
        return data
    # else:
    #     data = {"Action":"unable_to_response","Msg":query}
    #     return data
