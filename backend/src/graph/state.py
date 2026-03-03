import operator
from typing import Annotated, List, Dict, Optional, Any, TypedDict

# Define the schema for a single compliance result
# Error report 

class ComplianceIssue(TypedDict):
    category: str                    # e.g. FTC Disclosure
    description: str                 # Specific detail of violation
    severity: str                    # Critical warning
    timestamp: Optional[str]

# Define the global graph state

class VideoAuditState(TypedDict):
    '''
    Defines the data schema for langgraph execution content.
    '''
    # Input parameters
    video_url: str
    video_id: str

    # Ingestion and extraction data
    local_file_path: Optional[str]
    video_metadata: Dict[str, Any]         # e.g. {"duration": 15, "resolution": "1080p"}
    transcript: Optional[str]              # Fully extracted speech-to-text
    ocr_text: List[str]

    # Analysis output
    # Stores the list of all the violations found by AI

    compliance_results: Annotated[List[ComplianceIssue], operator.add]

    # Final deliverables
    final_status: str            # Pass or Fail
    final_report: str            # Markdown format

    # System Observability
    # Errors : API timeout, System level errors
    # List of system level crashes
    errors: Annotated[List[str], operator.add]

