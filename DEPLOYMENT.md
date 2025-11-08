# 🚀 Deployment Guide

## Streamlit Cloud Deployment

### Step 1: Prepare Your Repository

Make sure your code is pushed to GitHub:

```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Fill in the details:
   - **Repository**: Select your repository
   - **Branch**: `main`
   - **Main file path**: `app.py`

### Step 3: Configure Secrets

**IMPORTANT**: You must add your API key as a secret!

1. In your app dashboard, click on **"⚙️ Settings"**
2. Go to the **"Secrets"** tab
3. Add the following:

```toml
api_key = "your_actual_google_gemini_api_key_here"
```

4. Click **"Save"**

### Step 4: Deploy!

Click **"Deploy"** and wait for your app to build and launch!

---

## Getting Your Google Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the generated key
5. Paste it in Streamlit secrets (for cloud) or `.env` file (for local)

---

## Local Development with Secrets

For local development, you can use either:

### Option 1: .env file (Current method)
```env
api_key=your_api_key_here
```

### Option 2: Streamlit secrets (Recommended for consistency)

Create `.streamlit/secrets.toml`:
```toml
api_key = "your_api_key_here"
```

---

## Troubleshooting Deployment

### Error: "API key not found"
- Make sure you've added the `api_key` to Streamlit secrets
- Check for typos in the secret name (must be exactly `api_key`)
- Ensure there are no extra spaces

### Error: "Module not found"
- Verify all dependencies are listed in `requirements.txt`
- Check that package names are correct

### App keeps restarting
- Check the logs in Streamlit Cloud dashboard
- Look for any import errors or missing dependencies

### Slow performance
- This is normal for free Streamlit Cloud tier
- Consider upgrading for better performance

---

## Environment Variables

The app supports both methods:

1. **Streamlit Secrets** (Recommended for deployment)
   - Secure and built into Streamlit Cloud
   - Works automatically in deployed apps

2. **.env file** (Good for local development)
   - Easy to use locally
   - Not deployed to cloud (in .gitignore)

The app will automatically try Streamlit secrets first, then fall back to .env file.

---

## Post-Deployment

After successful deployment:

1. ✅ Test all features (Report, News, Summary, Q&A, Feedback)
2. ✅ Verify API calls are working
3. ✅ Check that reports are generated correctly
4. ✅ Share your app URL!

Your app URL will be: `https://your-app-name.streamlit.app`

---

## Updating Your Deployed App

To update your deployed app:

```bash
git add .
git commit -m "Update app"
git push origin main
```

Streamlit Cloud will automatically detect changes and redeploy!

---

## Need Help?

- [Streamlit Cloud Documentation](https://docs.streamlit.io/streamlit-community-cloud)
- [Streamlit Community Forum](https://discuss.streamlit.io/)
- Check the main [README.md](README.md) for more information

---

**Happy Deploying!** 🎉
