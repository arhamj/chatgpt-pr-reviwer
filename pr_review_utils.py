import os
import requests
import openai

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up GitHub API
GITHUB_ACCESS_TOKEN = os.getenv("GH_ACCESS_TOKEN")

GITHUB_API_BASE_URL = "https://api.github.com"


def fetch_prs(repo):
    # Fetch open pull requests for a repository
    url = f"{GITHUB_API_BASE_URL}/repos/{repo}/pulls?state=open"
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()


def review_pr(pr):
    # Generate a ChatGPT review for a PR
    prompt = f"Review the following pull request:\nTitle: {pr['title']}\nDescription: {pr['body']}\n"
    response = openai.Completion.create(
        engine="text-davinci-002", prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.5)
    return response.choices[0].text.strip()


def post_review_comment(repo, pr, review):
    # Post the review as a comment on the PR
    url = f"{GITHUB_API_BASE_URL}/repos/{repo}/issues/{pr['number']}/comments"
    headers = {"Authorization": f"token {GITHUB_ACCESS_TOKEN}"}
    data = {"body": review}
    response = requests.post(url, headers=headers, json=data)
    return response.json()
