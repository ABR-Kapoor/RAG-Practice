from server.main import app

# Vercel requires the app to be named 'app' or exported as default
def handler(request):
    return app(request)

# Alternative: Export the app directly
# This is what Vercel will use
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)