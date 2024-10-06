#!/bin/bash
set +m

# Accept optional solution_name argument
solution_name="$1"

# Define colors and effects
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
BLINK='\033[5m'
BOLD='\033[1m'
NC='\033[0m' # No Color
CLEAR='\033[2J\033[H' # Clear screen and move cursor to the top

# Notification interval in seconds (1 minute = 60 seconds)
NOTIFY_INTERVAL=60

# Start the timer
echo -e "${CLEAR}"
if [ -n "$solution_name" ]; then
    echo -e "${GREEN}Timer started for solution: ${YELLOW}$solution_name${NC}. Press [Enter] to stop the timer."
else
    echo -e "${GREEN}Timer started. Press [Enter] to stop the timer.${NC}"
fi
start_time=$(date +%s)

# Function to update elapsed time
update_time() {
    while true; do
        current_time=$(date +%s)
        elapsed_time=$(( current_time - start_time ))

        # Format elapsed time into hours, minutes, and seconds
        hours=$(( elapsed_time / 3600 ))
        minutes=$(( (elapsed_time % 3600) / 60 ))
        seconds=$(( elapsed_time % 60 ))

        # Clear the line and print elapsed time
        printf "\r${BLUE}Elapsed time: ${RED}%02d hours, %02d minutes, and %02d seconds${NC}" $hours $minutes $seconds

        # Sleep for 1 second before updating
        sleep 1
    done
}

# Function to notify every minute with bling-bling effect for 3 seconds
notify_time() {
    next_notification_time=$(( start_time + NOTIFY_INTERVAL ))
    while true; do
        current_time=$(date +%s)
        sleep_time=$(( next_notification_time - current_time ))
        if [ $sleep_time -le 0 ]; then
            # If sleep_time is negative, skip sleep
            sleep_time=0
        fi
        sleep $sleep_time
        # Clear the screen and print a loud, blinking, and colorful notification with a system bell
        echo -e "${CLEAR}${BLINK}${BOLD}${YELLOW}✨✨ Another minute has passed! ✨✨${NC}\a"
        sleep 3
        # After 3 seconds, clear the screen and resume the timer display
        echo -e "${CLEAR}"
        # Calculate next notification time
        next_notification_time=$(( next_notification_time + NOTIFY_INTERVAL ))
    done
}

# Start the elapsed time update and notification in the background
update_time & timer_pid=$!
disown $timer_pid
notify_time & notify_pid=$!
disown $notify_pid

# Wait for user to press Enter
read

# Kill the background processes
kill $timer_pid
kill $notify_pid

# Stop timer and calculate final elapsed time
end_time=$(date +%s)
elapsed_time=$(( end_time - start_time ))

# Format final elapsed time
hours=$(( elapsed_time / 3600 ))
minutes=$(( (elapsed_time % 3600) / 60 ))
seconds=$(( elapsed_time % 60 ))

# Final output when timer stops
echo -e "\n${BLUE}Final elapsed time: ${RED}$hours hours, $minutes minutes, and $seconds seconds${NC}"

# If solution_name is provided, record to timer_record.csv
if [ -n "$solution_name" ]; then
    # Get current date
    current_date=$(date '+%Y-%m-%d %H:%M:%S')

    # Format time_cost as hh:mm:ss
    time_cost=$(printf "%02d:%02d:%02d" $hours $minutes $seconds)

    # Check if timer_record.csv exists, if not, create it with headers
    if [ ! -f timer_record.csv ]; then
        echo "Date,Solution Name,Time Cost" > timer_record.csv
    fi

    # Append the record to timer_record.csv
    echo "$current_date,$solution_name,$time_cost" >> timer_record.csv

    # Notify the user that the timer data has been recorded
    echo -e "${GREEN}Timer data for solution '${YELLOW}$solution_name${GREEN}' has been recorded in 'timer_record.csv'.${NC}"
fi