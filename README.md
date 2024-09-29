
It is a GitHub Action that automatically analyzes code changes in your repository, identifies potential performance improvements, and detects code smells using OpenAI's GPT model. It is designed to review code files such as Python, JavaScript, TypeScript, Java, C, C++, Go, Ruby, PHP, and C#. The analysis results are sent to a specified Discord channel for easy review.

## Installation

To use this action in your repository, follow the steps below:

1. Copy the YAML configuration into the .github/workflows directory of your project.
2. Ensure you have the following secrets added to your repository:
    * OPENAI_API_KEY: Your OpenAI API key to send requests for code analysis.
    * DISCORD_WEBHOOK_URL: A Discord webhook URL where the analysis results will be sent.
    * AGENTOPS_API_KEY: API KEY FROM AGENT OPS.
3. Ensure your project has the necessary dependencies:
    * Python 3.x
    * jq installed for JSON manipulation.

## How to Use

This action runs automatically on every push to the main branch. It analyzes code files changed in the commit and sends performance and code smell suggestions to a Discord channel. The following file types are supported: .py, .js, .ts, .java, .c, .cpp, .go, .rb, .php, and .cs.

# Workflow Breakdown

1. Checkout the repository: The action first checks out the repository to analyze the latest commit.
2. Set up Python: The Python environment is set up with the required version (3.x).
3. Install dependencies: Installs jq and the requests library for making HTTP requests.
4. Get committer's name: Retrieves the name of the person who made the commit.
5. Check for code files: The workflow identifies any code files that were changed and sends them to GPT for analysis.
6. Send suggestions to Discord: Suggestions for improving code quality and performance are sent to the configured Discord channel
