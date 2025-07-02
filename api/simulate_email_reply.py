from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class EmailRequest(BaseModel):
    original_email: str
    original_language: str  # ISO code, e.g., 'fr', 'es', 'it'

class EmailResponse(BaseModel):
    translated_to_german: str
    german_ai_reply: str
    translated_back_to_original: str

def mock_translate(text: str, source_lang: str, target_lang: str) -> str:
    if source_lang == "fr" and target_lang == "de":
        return "Hallo, ich habe meine Bestellung nicht erhalten. Können Sie bitte den Lieferstatus prüfen? Danke."
    elif source_lang == "de" and target_lang == "fr":
        return "Bonjour, merci pour votre message. Nous vérifions immédiatement le statut de la livraison et vous répondrons sous peu."
    else:
        return f"[Translated {text} from {source_lang} to {target_lang}]"

def mock_generate_german_response(translated_text: str) -> str:
    responses = [
        "Vielen Dank für Ihre Nachricht. Wir prüfen den Lieferstatus sofort und melden uns in Kürze bei Ihnen.",
        "Es tut uns leid für die Unannehmlichkeiten. Wir sehen uns den Versandstatus an und informieren Sie schnellstmöglich.",
        "Ihre Bestellung wird derzeit geprüft. Wir senden Ihnen in Kürze ein Update zum Lieferstatus."
    ]
    return random.choice(responses)

@app.post("/")
async def simulate_email_reply(request: EmailRequest):
    german_text = mock_translate(request.original_email, request.original_language, "de")
    ai_reply_in_german = mock_generate_german_response(german_text)
    reply_in_original = mock_translate(ai_reply_in_german, "de", request.original_language)
    return EmailResponse(
        translated_to_german=german_text,
        german_ai_reply=ai_reply_in_german,
        translated_back_to_original=reply_in_original
    )

# For Vercel
from mangum import Mangum
handler = Mangum(app)