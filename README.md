# Notification_Service_System

## Overview

This project is a **Notification Service System** built using **FastAPI**. It provides API endpoints to:

- Send notifications (Email, SMS, In-app)
- Retrieve notifications for a user

The system is designed with extensibility in mind, including support for queuing (RabbitMQ) and retry logic for failed notifications.

---

## Features

- **Send Notification:** POST `/notifications`
- **Get User Notifications:** GET `/users/{id}/notifications`
- Supports 3 types of notifications: Email, SMS, and In-app
- Bonus (optional): Uses RabbitMQ to queue notifications for processing
- Retry failed notifications with exponential backoff

---

## Folder Structure

notification-system/
├── api/
│ └── main.py # FastAPI app with API routes
├── core/
│ ├── config.py # Configuration variables (like RabbitMQ, DB settings)
│ └── queue.py # RabbitMQ connection and queue helpers
├── services/
│ ├── notification_service.py # Logic to send and retry notifications
│ └── retry.py # Retry logic using Tenacity
├── models/
│ └── notification.py # Pydantic models for request/response validation
├── requirements.txt # Required Python packages
└── README.md # This file

---

## Prerequisites

- Python 3.8+
- RabbitMQ (optional but recommended for queuing)
- Git (optional, for cloning repo)

---

## Setup Instructions

### 1. Clone the Repository (Optional)

If you have Git installed, you can clone the repo directly:

```bash
git clone https://github.com/yourusername/notification-system.git
cd notification-system
