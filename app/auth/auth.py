from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# Path: app\auth\auth.py
app = FastAPI()


@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {
        'acess_token': form_data.username + 'token'
    }


@app.get('/')
async def index(token: str = Depends(oauth2_scheme)):
    return {'token': token}
