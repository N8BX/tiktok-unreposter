import os
import time
import subprocess
import pygetwindow as gw
import pyperclip
import keyboard
import sys

# ✅ MARDINLI DEVELOPER | Instagram & GitHub: @N8BX

# --- 1. Detect Chrome path
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
]
chrome_path = next((p for p in chrome_paths if os.path.exists(p)), None)

if not chrome_path:
    print("❌ Chrome not found!")
    input("Press any key to exit...")
    sys.exit()

# --- 2. Ask for number of reposts
try:
    max_reposts = int(input("Enter how many reposts you want to remove: "))
except ValueError:
    print("❌ Invalid number.")
    sys.exit()

# --- 3. Open TikTok profile in new Chrome window
profile_url = "https://www.tiktok.com/profile"
subprocess.Popen([chrome_path, "--new-window", profile_url])
print("✅ Opened TikTok profile page.")
time.sleep(2)

# --- 4. Maximize Chrome window
chrome_window = None
for window in gw.getWindowsWithTitle("TikTok") + gw.getWindowsWithTitle("Google Chrome"):
    if "TikTok" in window.title or "Google Chrome" in window.title:
        chrome_window = window
        break

if chrome_window:
    chrome_window.maximize()
    chrome_window.activate()
    print("✅ Chrome maximized.")
else:
    print("❌ Could not detect Chrome window.")
    sys.exit()

# --- 5. Open DevTools & allow pasting
keyboard.press_and_release("ctrl+shift+i")
time.sleep(2)
pyperclip.copy("allow pasting")
keyboard.press_and_release("ctrl+v")
keyboard.press_and_release("enter")
time.sleep(1)

# --- 6. Open Reposts tab directly
open_repost_tab = """
let interval = setInterval(() => {
    let tab = document.querySelector('p[data-e2e="repost-tab"]');
    if (tab) {
        tab.click();
        console.log("✅ Repost tab opened!");
        clearInterval(interval);
    } else {
        console.log("❌ Repost tab not found...");
    }
}, 1000);
"""
pyperclip.copy(open_repost_tab)
keyboard.press_and_release("ctrl+v")
keyboard.press_and_release("enter")
time.sleep(2)

# --- 7. Start removing reposts
print(f"\n🔥 Script started by MARDINLI DEVELOPER (@N8BX)")
print(f"➡ Removing up to {max_reposts} reposts...\n")

repost_count = 0

while repost_count < max_reposts:
    chrome_window.activate()
    time.sleep(1)

    # Click first reposted video
    click_video_js = """
    let interval = setInterval(() => {
        const first = document.querySelector('.css-1mdo0pl-AVideoContainer');
        if (first) {
            first.click();
            console.log("✅ Reposted video clicked!");
            clearInterval(interval);
        } else {
            console.log("❌ No reposted video found.");
        }
    }, 1000);
    """
    pyperclip.copy(click_video_js)
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("enter")
    time.sleep(2)

    # Click repost icon
    remove_repost_js = """
    setTimeout(() => {
        let icon = document.querySelector('path[fill="#FFC300"]');
        if (icon) {
            let svg = icon.closest('svg');
            if (svg) {
                svg.dispatchEvent(new MouseEvent('click', { bubbles: true }));
                console.log("✅ Repost removed.");
            }
        } else {
            console.log("❌ Repost icon not found.");
        }
    }, 1000);
    """
    pyperclip.copy(remove_repost_js)
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("enter")
    time.sleep(2)

    repost_count += 1
    print(f"🔄 Removed repost {repost_count} of {max_reposts}")

    # Go to next video
    next_video_js = """
    let interval = setInterval(() => {
        const btn = document.querySelector('button[data-e2e="arrow-right"]');
        if (btn) {
            btn.click();
            console.log("✅ Next video clicked!");
            clearInterval(interval);
        } else {
            console.log("❌ Next video button not found.");
        }
    }, 1000);
    """
    pyperclip.copy(next_video_js)
    keyboard.press_and_release("ctrl+v")
    keyboard.press_and_release("enter")

    # Return focus to terminal
    time.sleep(2)
    for win in gw.getWindowsWithTitle("Command Prompt") + gw.getWindowsWithTitle("Windows PowerShell") + gw.getWindowsWithTitle("Terminal"):
        try:
            win.activate()
            break
        except:
            pass
    time.sleep(2)

# --- 8. Done
print(f"\n✅ All done! Total reposts removed: {repost_count}")
print("🚀 Script by MARDINLI DEVELOPER | IG/GitHub: @N8BX")
