
def api_format_return(data=[],message="",request="",data_items=True) :
    return {
    "data":data ,
    "message": message,
    "request": request,
    "data_items":data_items
    }