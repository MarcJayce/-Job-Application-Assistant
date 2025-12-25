AI Job Application Assistant – Backend Architecture
📌 Overview
This backend powers an AI-driven job application assistant. It is designed to:
- Stay flexible with variable resume formats.
- Handle asynchronous AI tasks (resume tailoring, cover letter generation).
- Cleanly map to both JavaScript/TypeScript and Python workflows.
- Ensure reliability, scalability, and auditability.

🏗 High-Level System Design
API Gateway
- Handles authentication, validation, and synchronous endpoints.
- Supports:
- User CRUD
- Applications CRUD
- Dashboard reads
Async Workers
- Offloads AI tasks from the request thread.
- Processes:
- Resume tailoring
- Cover letter generation
- Improves reliability and speed.
Storage
- Document store: Raw JSON blobs (resume variants, job postings, AI outputs).
- Relational tables: Records and status tracking.
Event Bus
- Emits domain events to decouple components:
- ApplicationCreated
- AIJobQueued
- AIOutputReady
File Service
- Stores exports (PDF, DOCX) and attachments.
- Supports versioning.
Audit & Versioning
- Every edit is tracked.
- AI outputs never overwrite user edits.

📂 Data Models
Users, Profiles, and Auth
- User: id, email, password_hash, created_at, last_login, role
- Profile: user_id, full_name, contact, location, links, preferences
Resumes and Jobs (Flexible Schemas)
- Resume: id, user_id, title, format_type, latest_version_id, created_at
- ResumeVersion: id, resume_id, source_type, raw_json, text_blob, files[], created_at
- JobPosting: id, user_id, source_type, url, raw_json, text_blob, metadata, created_at
Exports and Attachments
- DocumentExport: id, application_id, doc_type, file_url, format, created_at
- Attachment: id, application_id or resume_id, file_url, mime_type, created_at
Audit and Events
- AuditLog: actor_id, entity_type, entity_id, action, diff_json, timestamp
- DomainEvent: event_type, payload_json, created_at, processed_at

🌐 API Surface
User & Profile
- POST /users – Create user
- GET /users/:id – Retrieve user
- PUT /users/:id – Update user
- DELETE /users/:id – Delete user
- GET /profiles/:user_id – Retrieve profile
- PUT /profiles/:user_id – Update profile
Resumes
- POST /resumes – Create resume
- GET /resumes/:id – Retrieve resume
- POST /resumes/:id/versions – Add new version
- GET /resumes/:id/versions – List versions
Job Postings
- POST /jobs – Add job posting
- GET /jobs/:id – Retrieve job posting
- GET /jobs – List job postings
Applications & Exports
- POST /applications – Create application
- GET /applications/:id – Retrieve application
- POST /applications/:id/exports – Generate export (PDF/DOCX)
- GET /applications/:id/exports – List exports
Attachments
- POST /attachments – Upload attachment
- GET /attachments/:id – Retrieve attachment
Events & Audit
- GET /events – List domain events
- GET /audit/:entity_id – Retrieve audit logs

⚙️ Key Principles
- Flexibility: Raw JSON storage supports variable resume/job schemas.
- Scalability: Async workers + event bus decouple heavy AI tasks.
- Reliability: Audit logs ensure traceability of every change.
- User-first: AI outputs never overwrite user edits; versioning is preserved.

🚀 Getting Started
- Clone the repository.
- Configure environment variables for:
- Database (SQL + NoSQL)
- File storage service
- Event bus
- Authentication provider
- Run migrations for relational tables.
- Start services:
- API Gateway
- Async Workers
- Event Bus
- Access API via REST endpoints.
