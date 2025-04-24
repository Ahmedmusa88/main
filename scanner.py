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

openai.api_key = (from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
)
    
