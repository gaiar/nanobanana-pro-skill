# Setup Guide — Nano Banana Pro

## 1. Install uv

```bash
brew install uv
```

Verify: `uv --version` should return `uv 0.x.x`.

## 2. Install Python Packages

```bash
cd ~/Developer/nanobanana-pro-skill && uv sync
```

This creates `.venv/`, installs Python 3.12 if needed, and installs all dependencies from `uv.lock`.

If `~/Developer/nanobanana-pro-skill/` does not exist, the project must be cloned or initialized first — this is a fatal error; inform the user.

## 3. Install gcloud CLI

```bash
brew install google-cloud-sdk
```

Verify: `gcloud --version`.

## 4. Configure GCP Project

```bash
gcloud init
# Or set project directly:
gcloud config set project <PROJECT_ID>
```

Verify: `gcloud config get-value project` returns a valid project ID (not `(unset)`).

The default project is `lounge-demand-tech-ai`.

## 5. Authenticate (Application Default Credentials)

```bash
gcloud auth application-default login
```

This opens a browser for OAuth. Verify: `gcloud auth application-default print-access-token` returns a token (not an error).

## 6. Enable Vertex AI API

```bash
gcloud services enable aiplatform.googleapis.com
```

Verify: `gcloud services list --enabled --filter=aiplatform` shows `aiplatform.googleapis.com`.

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `uv: command not found` | uv not installed | `brew install uv` |
| `uv sync` fails with Python error | Python 3.12 not available | `uv python install 3.12` |
| `gcloud: command not found` | gcloud not installed | `brew install google-cloud-sdk` |
| `403 Permission Denied` on generate | Vertex AI API not enabled | Step 6 above |
| `401 Unauthorized` on generate | ADC not configured | Step 5 above |
| `Project not set` error | No default project | Step 4 above |
