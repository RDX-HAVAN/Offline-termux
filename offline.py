#!/bin/bash

# Setting up variables
LOGFILE="$HOME/approval_log.txt"
LOGO="==== APPROVAL SYSTEM ===="  # Placeholder for logo name/title

# Print the logo or system name at the top
echo "$LOGO"
echo "========================="

# Function to check if a user is approved
check_approval() {
    local username=$1
    grep -q "$username:approved" $LOGFILE
    return $?
}

# Function to approve a user
approve_user() {
    local username=$1
    echo "$username:approved" >> $LOGFILE
    echo "[`date`] $username has been approved." >> $LOGFILE
    echo "$username is now approved."
}

# Function to disapprove a user
disapprove_user() {
    local username=$1
    sed -i "/$username:approved/d" $LOGFILE
    echo "[`date`] $username has been disapproved." >> $LOGFILE
    echo "$username is now disapproved."
}

# Main menu for the approval system
echo "1. Approve User"
echo "2. Disapprove User"
echo "3. Check Approval Status"
echo "4. Exit"
read -p "Choose an option: " option

case $option in
    1)
        read -p "Enter username to approve: " username
        approve_user $username
        ;;
    2)
        read -p "Enter username to disapprove: " username
        disapprove_user $username
        ;;
    3)
        read -p "Enter username to check status: " username
        if check_approval $username; then
            echo "$username is approved."
        else
            echo "$username is not approved."
        fi
        ;;
    4)
        echo "Exiting the approval system."
        exit 0
        ;;
    *)
        echo "Invalid option. Please try again."
        ;;
esac
