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
    target_url = input("Enter a website URL (e.g., https://example.com): ")
    scan_website(target_url)   
