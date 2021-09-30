from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html >
        <head>
            <title>Hello, World</title>
        </head>
        <body style="width: 99%; background-color: #00DBDE;background-image: linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);">
            <h1 style="padding-top: 12%; width: 97%; margin: 0 auto; font-size: 18vw; user-select: none;">Hello World</h1>
        </body>
    </html>
    """


if __name__ == "__main__":
    import uvicorn

    print("Hello World")
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False, debug=True)
