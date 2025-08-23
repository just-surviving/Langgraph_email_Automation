# 🚀 Deployment Guide

This guide covers deploying the LangGraph Email Agent to various cloud platforms.

## 📋 Prerequisites

Before deploying, ensure you have:

- ✅ GitHub repository set up with your code
- ✅ API keys for Groq and Google Gemini
- ✅ Gmail API credentials configured
- ✅ Environment variables ready

## 🐳 Docker Deployment

### Local Docker Testing

1. **Build the image:**
   ```bash
   docker build -t langgraph-email-agent .
   ```

2. **Run locally:**
   ```bash
   docker run -p 8000:8000 --env-file .env langgraph-email-agent
   ```

3. **Test the deployment:**
   ```bash
   curl http://localhost:8000/health
   ```

### Docker Compose (Recommended for Development)

```bash
docker-compose up --build
```

## ☁️ Cloud Platform Deployment

### Option 1: Render (Recommended)

Render is excellent for Python applications and offers a generous free tier.

#### Step-by-Step Deployment

1. **Sign up at [render.com](https://render.com)**

2. **Connect your GitHub repository:**
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select `just-surviving/langgraph-email-agent`

3. **Configure the service:**
   - **Name:** `langgraph-email-agent` (or your preferred name)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn deploy_api:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT --workers 1`

4. **Add environment variables:**
   - `MY_EMAIL`: Your Gmail address
   - `GROQ_API_KEY`: Your Groq API key
   - `GOOGLE_API_KEY`: Your Google Gemini API key
   - `PORT`: Leave as `$PORT` (Render sets this automatically)

5. **Deploy:**
   - Click "Create Web Service"
   - Wait for build and deployment (usually 2-5 minutes)

6. **Access your service:**
   - Your service will be available at: `https://your-service-name.onrender.com`
   - Health check: `https://your-service-name.onrender.com/health`
   - API docs: `https://your-service-name.onrender.com/docs`

#### Render Configuration Tips

- **Auto-deploy:** Enable automatic deployments on git push
- **Health checks:** Render will automatically monitor your `/health` endpoint
- **Scaling:** Upgrade to paid plans for better performance and uptime

### Option 2: Railway

Railway offers excellent Python support and automatic deployments.

#### Step-by-Step Deployment

1. **Sign up at [railway.app](https://railway.app)**

2. **Connect your repository:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `just-surviving/langgraph-email-agent`

3. **Railway will automatically:**
   - Detect Python project
   - Install dependencies from `requirements.txt`
   - Use the `Procfile` for startup

4. **Add environment variables:**
   - Go to "Variables" tab
   - Add:
     - `MY_EMAIL`: Your Gmail address
     - `GROQ_API_KEY`: Your Groq API key
     - `GOOGLE_API_KEY`: Your Google Gemini API key

5. **Deploy:**
   - Railway automatically deploys on every git push
   - Monitor deployment in the "Deployments" tab

6. **Access your service:**
   - Railway provides a public URL automatically
   - Find it in the "Settings" → "Domains" section

### Option 3: Heroku

Heroku is a classic choice with excellent Python support.

#### Step-by-Step Deployment

1. **Install Heroku CLI:**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   ```

4. **Set environment variables:**
   ```bash
   heroku config:set MY_EMAIL=your_email@gmail.com
   heroku config:set GROQ_API_KEY=your_groq_api_key
   heroku config:set GOOGLE_API_KEY=your_gemini_api_key
   ```

5. **Deploy:**
   ```bash
   git push heroku main
   ```

6. **Open your app:**
   ```bash
   heroku open
   ```

## 🔧 Environment Variables

All platforms require these environment variables:

```bash
MY_EMAIL=your_email@gmail.com
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

## 🧪 Testing Your Deployment

### Health Check
```bash
curl https://your-app-url.com/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "LangGraph Email Agent"
}
```

### API Documentation
Visit `https://your-app-url.com/docs` for interactive API documentation.

### Sample Usage
Use the included `sample_usage.py` script:
```bash
python sample_usage.py
```

## 📊 Monitoring and Maintenance

### Health Monitoring
- All platforms will monitor your `/health` endpoint
- Set up alerts for downtime
- Monitor response times and error rates

### Logs
- **Render:** View logs in the dashboard
- **Railway:** Check logs in the "Deployments" tab
- **Heroku:** `heroku logs --tail`

### Updates
- Push changes to your GitHub repository
- Platforms will automatically redeploy
- Monitor deployment status

## 🚨 Troubleshooting

### Common Issues

1. **Build Failures:**
   - Check `requirements.txt` for missing dependencies
   - Verify Python version compatibility
   - Check build logs for specific errors

2. **Runtime Errors:**
   - Verify environment variables are set correctly
   - Check application logs
   - Ensure API keys are valid

3. **Performance Issues:**
   - Upgrade to paid plans for better resources
   - Optimize your code and dependencies
   - Consider caching strategies

### Getting Help

- Check platform-specific documentation
- Review application logs
- Test locally with Docker first
- Verify all environment variables are set

## 🎯 Next Steps

After successful deployment:

1. **Test the API endpoints**
2. **Set up monitoring and alerts**
3. **Configure custom domain (optional)**
4. **Set up CI/CD for automatic deployments**
5. **Monitor usage and performance**

---

**Happy Deploying! 🚀**

For additional support, check the main [README.md](README.md) or open an issue on GitHub.
