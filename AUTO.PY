import os, time

repo_path = r"C:\Users\Manish Pandey\Desktop\SU\CSCR1506-Tool-Based-Frontend"

while True:
    os.chdir(repo_path)
    # Check if there are changes
    status = os.system("git diff-index --quiet HEAD --")
    if status != 0:
        os.system("git add .")
        os.system('git commit -m "Auto update"')
        os.system("git push origin main")
        print("✅ Code auto pushed to GitHub!")
    else:
        print("No changes to push.")
    time.sleep(300)  # 5 minutes
