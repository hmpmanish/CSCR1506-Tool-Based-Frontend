import subprocess
import os
import time

repo_path = r"C:\Users\Manish Pandey\Desktop\SU\CSCR1506-Tool-Based-Frontend"

while True:
    try:
        os.chdir(repo_path)

        # Stage changes
        subprocess.run(["git", "add", "."], check=True)

        # Check if anything to commit
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True
        ).stdout

        if status.strip():

            # Commit with timestamp
            commit_message = f"Auto commit {time.strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)

            # Get current branch
            branch = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True,
                text=True
            ).stdout.strip()

            # Pull latest changes
            pull = subprocess.run(["git", "pull", "origin", branch])
            if pull.returncode != 0:
                print("⚠ Pull failed. Resolve manually.")
                break

            # Push
            push = subprocess.run(["git", "push", "origin", branch])
            if push.returncode == 0:
                print("✅ Changes pushed successfully!")
            else:
                print("❌ Push failed!")
                break

        else:
            print("No changes to push.")

    except Exception as e:
        print("Error:", e)
        break

    time.sleep(10)