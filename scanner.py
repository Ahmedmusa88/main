import requests

def scan_website(url):
    print(f"Scanning {url}...")

    try:
        response = requests.get(url, timeout=5)
        print("✅ Website is reachable.")

        # Check for security headers
        security_headers = [
            'Content-Security-Policy',
            'Strict-Transport-Security',
            'X-Content-Type-Options',
            'X-Frame-Options',
            'X-XSS-Protection'
        ]

        print("\n🔐 Security Headers:")
        for header in security_headers:
            if header in response.headers:
                print(f"✔️ {header}: {response.headers[header]}")
            else:
                print(f"❌ {header} not found")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error reaching website: {e}")

# مثال على الاستخدام
if __name__ == "__main__":
   import sys

if len(sys.argv) > 1:
    target_url = sys.argv[1]
else:
    print("يرجى إرسال رابط الموقع عند تشغيل البرنامج.")
    sys.exit(1)
import openai

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

print(response.choices[0].message.content)
import requests
import sys
from openai import OpenAI

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

# Set up OpenAI client with your API key
client = OpenAI(api_key="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")  # Replace with your OpenAI API key

# Send request to the GPT model to write a bedtime story about a unicorn
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."}
    ]
)

# Send request for a haiku about AI
completion = client.chat.completions.create

    
