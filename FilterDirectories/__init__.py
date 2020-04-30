import logging
import re
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    name = req.params.get('name')
    if not name:
        try:
                req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('childItems')
            folderarray= []
            folderarrayYear =[]
            for val1 in name:               
                logging.info('in loop')                                     
                logging.info(val1['name'])
                if(re.match('(\d{4})[/.-](\d{2})[/.-](\d{2})$',val1['name']) or re.match('(\d{4})[/.-](\d{2})$',val1['name']) ):
                    logging.info(val1['name'])
                    folderarray.append(val1['name'])
                if(re.match('(\d{4})$',val1['name'])):
                    folderarrayYear.append(val1['name'])

    if name:        
        # jsonload =json.dumps({'results': folderarray},{'resultYear' : folderarrayYear})
        # jsonloadYear =  json.dumps({'resultYear' : folderarrayYear})

        resultJson = {
           'results' : folderarray,
           'resultsYear' : folderarrayYear
        }

        jsonload = json.dumps(resultJson)
        logging.info(jsonload)
        # return func.HttpResponse(f"{{\"response \" :\"{json.dumps(folderarray)}\"}}")
        return func.HttpResponse(jsonload)
    else:
        return func.HttpResponse(
             "Please pass a childItems on the request body",
             status_code=400
        )
