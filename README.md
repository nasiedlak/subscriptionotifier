# Subscription Notifier

A simple Python project that allows users to receive email notifications for upcoming subscriptions renewals.

## Description

This is a command line application. Users enter their email address along with subscription information such as name and renewal date to receive notifications.

## Installation

1. Clone this repository
    ```
    git clone https://github.com/<Your GitHub Username>/SubscriptionNotifier.git
    ```
2. Navigate into the directory
    ```
    cd SubscriptionNotifier
    ```
3. Create a virtual environment
    ```
    python3 -m venv env
    ```
4. Activate a virtual environement
    - macOS and Linux:
        ```
        source env/bin/activate
        ```
    - Windows:
        ```
        .\env\Scripts\activate
        ```
5. Install the required packages
    ```
    pip install -r requirements.txt
    ```

## Usage

- Unix-based systems (macOS, Linux):
    1. Run and enter the requested information:
        ```
        python3 subscription_notifer.py
        ```
    2. To run the notifier daily, use a cron job:
        - Open the crontab editor:
            ```
            crontab -e
            ```
        - Add the following line to run the script daily at 12:00PM 
            ```
            0 12 * * * /path/to/your/python3 /path/to/subscription_notifier.py >> /path/to/logfile.log 2>&1
- Windows:
    1. Run and enter the requested information:
            ```
            python3 subscription_notifer.py
            ```
    2. Use [Task Scheduler](https://docs.bmc.com/docs/bacr20/using-task-scheduler-to-run-a-nightly-process-907294198.html)

## Help
    ```
    python3 subscription_notifer.py --help
    ```

## Contributing

Feel free to fork this repository and make contributions!

## License

MIT license. See LICENSE file for more details.
