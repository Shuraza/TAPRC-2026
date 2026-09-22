import datetime
import logging
import azure.functions as func
import requests

app = func.FunctionApp()

@app.timer_trigger(schedule="0/5 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_tipo1(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Opa deu certo.')
    

    
@app.route(route="http_trigger", auth_level=func.AuthLevel.FUNCTION)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    lastname= req.params.get('lastname')
    

    if name and lastname:
        return func.HttpResponse(f"Eai, {name} {lastname}. você conseguiu!!")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
        
        
    
@app.timer_trigger(schedule="0/30 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_trigger_tipo2(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')
        
    url = "url do projeto"
   
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Request successful: {response.text}")
        else:
            logging.error(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")

    logging.info(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))