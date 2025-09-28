# ⏰ Using Cron to Schedule `script.py`

This guide explains how to use **cron** (the Unix/Linux task scheduler) to automatically run your `script.py` at regular intervals.

---

## 1. Open your crontab
Run this command in the terminal:

```bash
crontab -e
```

- **`crontab`** → command to edit and manage cron jobs (scheduled tasks).  
- **`-e`** → edit your personal crontab file.  
- When you run this, it opens the file in your default editor (`nano` or `vim`).  
    - Anything you add here becomes a scheduled job that your system will run automatically.  

## 2. Add a job
```bash
* * * * * /usr/bin/python3 ~/Documents/git/stock-trading-python-app/script.py
```

### 🕒 Cron Schedule Format
- **`* * * * *`** → schedule format:  
  - `minute hour day-of-month month day-of-week`  
- `*` means **every**.  
- So `* * * * *` means → run **every minute of every hour of every day**. 

- `/usr/bin/python3` → full path to Python 3.
- `~/Documents/.../script.py` → your script path.
- ~ expands to your home directory.

## 💾 Exiting the Editor
How you exit depends on the editor used by `crontab -e`:  
- **If it opens in nano:**  
  - `CTRL + O` → save changes  
  - `ENTER` → confirm filename  
  - `CTRL + X` → exit  
- **If it opens in vim/vi:**  
  - Press `ESC`  
  - Type `:wq`  
  - Press `ENTER`  


## 4. Verify cron job
```bash
crontab -l
```