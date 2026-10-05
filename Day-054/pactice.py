from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Backend Server Active'}

@app.get('/health')
def health():
    return {'health': 'Alive Twin!'}

@app.get('/about')
def about():
    return {
  "project": "Backend Server Testing",
  "status": "development"
}



'''
Explaination:
    Deployment is what allows other people who u permit
    use ur work or get to know about ur work without the file sitting
    on ur desktop

    one of the best python based library used fopr this is FastAPI

    
    basic things to know when doing api

    Get:
    it is used to retrieve information from the deployed server
    whether it gets a result, some thing happening all depends on what is
    written to do in the get method

    POST:
    it is used to send data to the deployed server and wait for a 
    simple or a resulting response or an activity 
'''