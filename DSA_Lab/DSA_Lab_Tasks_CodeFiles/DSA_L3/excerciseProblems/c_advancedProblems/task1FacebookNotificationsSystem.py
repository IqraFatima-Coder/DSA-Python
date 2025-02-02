class NotificationSystem:
    def __init__(self, limit=5):
        self.notifications = []
        self.limit = limit

    def add_notification(self, notification):
        if len(self.notifications) >= self.limit:
            self.notifications.pop(0)  # Remove the oldest notification
        self.notifications.append(notification)

    def clear_all(self):
        self.notifications = []

    def view_latest_notifications(self):
        print("Latest Notifications:")
        for i, notification in enumerate(self.notifications[-5:], 1):  # Display only the latest 5 notifications
            print(f"{i}. {notification}")


# Example usage
notif_system = NotificationSystem()
notif_system.add_notification("New friend request")
notif_system.add_notification("Message from John")
notif_system.add_notification("Your post was liked")
notif_system.view_latest_notifications()
notif_system.clear_all()
notif_system.view_latest_notifications()
