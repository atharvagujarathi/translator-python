from fastapi import FastAPI
from deep_translator import GoogleTranslator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)



@app.post("/translate")
async def translate_text(data: dict):
    try:
        text = data.get("q", "")
        source_lang = data.get("source", "hi")
        target_lang = data.get("target", "ta")

        if not text:
            return {"error": "No text provided"}

        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return {"translatedText": translated_text}
    except Exception as e:
        return {"error": str(e)}

# Run the API with: uvicorn setup_argos:app --host 0.0.0.0 --port 8080  it is imp
