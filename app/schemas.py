from pydantic import BaseModel

class TaskRequest(BaseModel):
    objective: str

class TaskRequest(BaseModel):
    objective: str
    plan: list
    review_notes: str
    final_reports: str
    markdown_report: str | None = None
    pdf_report: str | None = None