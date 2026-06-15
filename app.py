from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevDeploy</title>
        <style>
            body{
                background:#0f172a;
                color:white;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
                font-family:Arial;
            }
            .card{
                text-align:center;
                padding:40px;
                border-radius:15px;
                background:#1e293b;
                box-shadow:0 0 20px rgba(0,0,0,0.4);
            }
            h1{
                color:#38bdf8;
            }
            p{
                color:#cbd5e1;
            }
        </style>
    </head>

    <body>

        <div class="card">
            <h1>DevDeploy</h1>

            <h2>CI/CD Pipeline Successful</h2>

            <p>Docker + Jenkins + GitHub + Render</p>

            <p>Built by Ayush Gupta</p>
        </div>

    </body>

    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)