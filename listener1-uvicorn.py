import logging
from fastapi import FastAPI, Request

app = FastAPI()

# configure logging
logging.basicConfig(filename='webhook.log', level=logging.INFO)

@app.post('/webhook')
async def webhook(request: Request):
    content = await request.json()
    logging.info('Webhook received with payload: %s', content)
    return {'message': 'OK'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
