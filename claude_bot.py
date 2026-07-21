import os
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

# Lấy Session Key và Chat URL từ biến môi trường của GitHub Secrets
SESSION_KEY = os.environ.get("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")
CHAT_URL = os.environ.get("https://claude.ai/chat/91491487-f4c8-4467-be8e-fa8d3f87e69a")

def send_message():
    with sync_playwright() as p:
        # Chạy trình duyệt Chromium
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.add_cookies([{
            'name': 'sessionKey',
            'value': SESSION_KEY,
            'domain': '.claude.ai',
            'path': '/',
            'httpOnly': True,
            'secure': True,
            'sameSite': 'Lax'
        }])

        page = context.new_page()
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Đang truy cập Claude...")
        
        try:
            page.goto(CHAT_URL, wait_until="networkidle", timeout=60000)
            
            editor_selector = 'div[contenteditable="true"]'
            page.wait_for_selector(editor_selector, timeout=15000)
            
            page.fill(editor_selector, 'tiếp')
            time.sleep(1)
            
            page.keyboard.press('Enter')
            print("-> ĐÃ GỬI 'TIẾP' THÀNH CÔNG!")
            time.sleep(5)

        except Exception as e:
            print(f"Lỗi thực thi: {e}")
        
        finally:
            browser.close()

if __name__ == "__main__":
    send_message()
