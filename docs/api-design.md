# 🌐 HCM Nexus AI — API Design & Data Model

## 📌 Overview

This document defines the API contracts and initial database schema for **HCM Nexus AI**, an AI-powered workforce intelligence and automation platform built on top of Oracle Cloud HCM.

The API layer is designed using REST principles with versioning support and modular scalability.

---

## 🔗 Base URL

```
/api/v1/
```

---

## 🔐 Authentication APIs

### 1. Login

**Endpoint**

```
POST /api/v1/auth/login
```

**Request**

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

**Response**

```json
{
  "access_token": "jwt_token",
  "user": {
    "id": 1,
    "name": "Sudip",
    "role": "HR_ADMIN"
  }
}
```

---

## 👥 Employee APIs

### 2. Get Employees

**Endpoint**

```
GET /api/v1/employees
```

**Query Parameters**

* department
* location
* joining_date

---

### 3. Employee Details

**Endpoint**

```
GET /api/v1/employees/{id}
```

---

## 📊 Analytics APIs

### 4. Dashboard Metrics

**Endpoint**

```
GET /api/v1/analytics/dashboard
```

**Response**

```json
{
  "total_employees": 1200,
  "active_employees": 1100,
  "attrition_rate": 12.5
}
```

---

### 5. Attrition Insights

**Endpoint**

```
GET /api/v1/analytics/attrition
```

---

## 🤖 AI Assistant API

### 6. AI Query

**Endpoint**

```
POST /api/v1/ai/query
```

**Request**

```json
{
  "query": "Show employees joined last 3 months"
}
```

**Response**

```json
{
  "type": "table",
  "columns": ["employee_id", "name", "department"],
  "data": []
}
```

---

## ⚡ Automation APIs

### 7. Trigger Workflow

**Endpoint**

```
POST /api/v1/automation/trigger
```

**Request**

```json
{
  "event": "NEW_EMPLOYEE",
  "employee_id": "E123"
}
```

---

## 🛠️ Admin APIs

### 8. Create Workflow Rule

**Endpoint**

```
POST /api/v1/admin/rules
```

**Request**

```json
{
  "name": "Onboarding Workflow",
  "trigger_event": "NEW_EMPLOYEE",
  "action": "INITIATE_ONBOARDING",
  "is_active": true
}
```

---

## 🧠 API Design Principles

* RESTful and resource-oriented
* Versioned APIs (`/api/v1/`)
* Stateless communication
* Secure using JWT authentication
* Scalable and modular endpoints

---

## 🗄️ Database Schema (Initial Design)

### 👤 User

* id
* name
* email
* password
* role
* created_at

---

### 👥 Employee

* id
* employee_id
* name
* department
* location
* joining_date
* salary
* created_at

---

### 📊 AnalyticsData

* id
* metric_name
* metric_value
* created_at

---

### ⚡ WorkflowRule

* id
* name
* trigger_event
* action
* is_active
* created_at

---

### 🤖 AIQueryLog

* id
* user_id
* query
* response
* created_at

---

## 🔗 Entity Relationships

* User → role-based access control
* Employee → source data from Oracle HCM
* AnalyticsData → derived from employee data
* WorkflowRule → triggered by system or employee events
* AIQueryLog → stores AI interactions

---

## ⚙️ Future Enhancements

* Multi-tenant architecture
* Advanced role & permission system
* ML-based predictive analytics tables
* Audit logs for compliance
* Integration logs for HCM Connector

---

## 👨‍💻 Author

Sudip Bera
Oracle Cloud HCM Technical Consultant | Full Stack Developer
