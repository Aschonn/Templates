from optparse import Option
from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

#-----------------------------#

'''
    Static Database of basketball teams and base class
    made changes

'''
DATA = {
    'teams': {
            0: 'timberwolves',
            1: 'heat',
            2: 'knicks',
            3: 'lakers',
            4: 'celtics',
            5: 'mavericks',
            6: 'jazz',
            7: 'magic',
            8: 'trailblazers',
            9: 'hornets'
        }
    }


class Team(BaseModel):
    team : str


#--------------- endpoints ----------------#


@app.get("/teams")
def root():
    return {'data': DATA}


# read user inputed ID

@app.get("/teams/{team_id}")
def team_item(team_id: int): # you can also add default parameters using Optional[str] = None method

    if team_id in DATA['teams']: 
        return {"data": DATA['teams'][team_id], 
                "team_id_used": team_id, 
                "message": "team already exists."}    
    else:
        return {"data": DATA,
                "team_id_used": team_id,
                "message": "There is no team with that Id."}    


# update static database

@app.put("/teams/{team_id}")
def update_team(team_id : int, new_team : Team):


    
    if team_id in DATA['teams'] and DATA["teams"][team_id] != new_team.team: 

        DATA["teams"][team_id] = new_team.team

        return {
                "data": DATA, 
                "team_id_used": team_id, 
                "team_name_inputed": new_team.team, 
                "message": "team has been updated."
                }    

    else:
            
        return {"data":  DATA,
                "team_id_used": team_id,
                "team_with_id": DATA["teams"][team_id],
                "team_name_inputed": new_team.team,
                "message": "ID is not associated with a team."    
                }   




# SIMPLE DELETE REQUEST ON SAMPLE

@app.delete("/items/{item_id}")
async def delete_team(team_id : int): 
    
    
    if team_id in DATA['teams']:

        del DATA["teams"][team_id]

        return {
                    "data": DATA, 
                    "team_id_used": team_id, 
                    "message": "team has been deleted."
                }    

    else:
            
        return {
                    "data":  DATA,
                    "team_id_used": team_id,
                    "team_with_id": DATA["teams"][team_id],
                    "message": "ID is not associated with a team."    
                }   


