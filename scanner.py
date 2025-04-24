import requests
import sys
import openai

# Function to scan the website and check security headers
def scan_website(url):
    print(f"🔍 Scanning: {url}")

    try:
        response = requests.get(url, timeout=5)
        print("✅ Website is reachable.\n")

        # Security headers to check
        security_headers = [
            'Content-Security-Policy',
            'Strict-Transport-Security',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'X-XSS-Protection'
        ]

        print("🔐 Security Headers:")
        for header in security_headers:
            if header in response.headers:
                print(f"✔️ {header}: {response.headers[header]}")
            else:
                print(f"❌ {header} not found")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error reaching website: {e}")

# Check if a website URL is provided when running the program
if len(sys.argv) > 1:
    website_url = sys.argv[1]
else:
    print("Please provide a website URL when running the program.")
    sys.exit(1)

# Scan the website
scan_website(website_url)

# Set up OpenAI client with your API key (store it securely)
openai.api_key = "YOUR_API_KEY"  # Make sure to replace this with a secure method to fetch the API key

# Send request to the GPT model to write a bedtime story about a unicorn
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}]
)

# Output the generated story
print("🦄 Bedtime Story:", response['choices'][0]['message']['content'])

    
