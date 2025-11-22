from fastapi import APIRouter
from pydantic import BaseModel
from core.models import predict_emotion
from core.mapping import EMOTION_TO_GENRE
from core.spotify import search_playlist_by_genre

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/emotion")
def get_emotion(payload: TextInput):
    prediction = predict_emotion(payload.text)
    top_emotion = prediction["emotion"]

    # Map emotion to genres
    genres = EMOTION_TO_GENRE.get(top_emotion.lower(), ["pop"])
    
    # Get playlists from Spotify
    playlists = []
    for genre in genres:
        playlists += search_playlist_by_genre(genre)

    prediction["playlists"] = playlists
    return prediction
