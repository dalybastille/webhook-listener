import configparser
import logging
from fastapi import FastAPI, Request

app = FastAPI()

# read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# get values from configuration file
port = config.getint('webhook', 'port')
ssl_keyfile = config.get('webhook', 'ssl_keyfile')
ssl_certfile = config.get('webhook', 'ssl_certfile')

# configure logging
logging.basicConfig(filename='/var/log/bastille/webhook.log', level=logging.INFO)

@app.post('/webhook')
async def webhook(request: Request):
    try:
        content = await request.json()
        logging.info('Webhook received with payload: %s', content)
        return {'message': 'OK'}
    except json.JSONDecodeError as e:
        # return error response for unparsable JSON
        return {'error': f'Unable to parse JSON: {str(e)}'}, 400

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=port, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile)
