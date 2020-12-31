# check_process
Check if a process if running in Linux

Add it to CRON to run it every 15 minutes
crontab -e

* /15 * * * /usr/bin/python3 /home/pi/telegram_service.py
