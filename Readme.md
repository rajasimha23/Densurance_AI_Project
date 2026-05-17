# Densurance AI Project - Setup Guide


## Pre-requisites

### 1. Configure AWS Access Keys (Windows + PowerShell)

#### Sign in to AWS Console

1. Go to the [AWS Console](https://console.aws.amazon.com)
2. Search for **AWS IAM**

#### Create Access Keys

1. Open your IAM user
2. Navigate to **Security credentials**
3. Under **Access keys**, click **Create access key**
4. Select **Command Line Interface (CLI)** and confirm the checkbox
5. Click **Next → Create access key**


> You will receive an **Access Key ID** and a **Secret Access Key**.
 Download or copy them immediately.

#### Configure PowerShell Environment Variables

Open PowerShell and run:

```powershell
$env:AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY"
$env:AWS_SECRET_ACCESS_KEY="YOUR_SECRET_KEY"
$env:AWS_REGION="your-region"
```

Verify the variables were set:

```powershell
echo $env:AWS_ACCESS_KEY_ID
echo $env:AWS_REGION
```

### 2. Install Python Packages

```bash
pip install boto3 python-dotenv openai
```

---

## Setting Up the AI Client

1. Go to **AWS Bedrock** and follow the "**Quick Start**" guide
2. Select the **"Generate Text"** option

**Step 1 : Generate API Key**
- Copy the API key
- Create a `.env` file in your folder and paste the key like this:
```powershell
AWS_BEARER_TOKEN_BEDROCK="paste-here"
```

**Step 2 : Set Environment Variables**
- Under *Set environment variables*, select **Windows**
- Copy the provided keys and paste them into your `.env` file
```powershell
OPENAI_API_KEY="your-key"
OPENAI_BASE_URL="your-url"
```

---

## Running the Application

1. Navigate to the `Densurance_AI_project` folder and run:
   ```bash
   python app.py
   ```
2. The server will start on **localhost:5000**
3. Open your browser and visit [http://localhost:5000](http://localhost:5000)
4. Fill out the form and click **Submit**
5. An HTML response containing a Risk Analysis in JSON format will be generated

---

## Saving Responses

1. `init_db()` is called automatically when `app.py` runs 
2. `risk.db` file is created on the first run 
3. All present and future responses are stored here. No external database needed.

---

## Potential Improvements

- **UI** - Currently basic HTML/CSS; significant room for improvement
- **AI model** - The current model is intentionally small; a more capable model would handle prompts more accurately
- **Database** - An external database could be integrated into the UI to display a full history of prompts and responses
- **General** - Every choice (UI, AI, backend, database) was made with simplicity as the priority

---

## What I Tried

- **Local LLM hosting**: Attempted to host a local LLM, but it requires dedicated hardware. Hosting on an EC2 instance turned out to be costly.
- **n8n**: Has associated costs, but would be free if self-hosted on your own machine. Yet to explore.
- **Cloud-hosted AI models**: Used as a last resort; token pricing is still being explored.