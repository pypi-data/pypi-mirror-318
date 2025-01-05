from dataclasses import dataclass, field
from typing import Any, Dict, Optional,Union,List
from datetime import datetime, timezone
import json
import uuid
from ipulse_shared_base_ftredge import (ProgressStatus, to_enum, evaluate_combined_progress_status)

@dataclass
class OpResult:
    """Base class for operation results with status tracking"""
    _operation_id: str = field(default_factory=lambda: str(uuid.uuid4()))  # Default to UUID
    _data: Any = None
    _overall_status: ProgressStatus = ProgressStatus.IN_PROGRESS
    _execution_state: List[str] = field(default_factory=list)
    _issues: List[Any] = field(default_factory=list)
    _warnings: List[Any] = field(default_factory=list)
    _notices: List[Any] = field(default_factory=list)
    _metadata: Dict[str, Any] = field(default_factory=dict)
    _start_time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    _duration_s: float = 0.0
    _total_operations: int = 1  # Default to 1 for the current operation

    @property
    def operation_id(self) -> str:
        """Get operation ID"""
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value: str) -> None:
        """Set operation ID"""
        self._operation_id = value

    @property
    def data(self) -> Any:
        """Get data"""
        return self._data
    
    @data.setter
    def data(self, value: Any) -> None:
        """Set data"""
        self._data = value

    def add_data(self, values: Any, name:str) -> None:
        """Add data to a dict with a name"""
        if not self.data:
            self.data = {}
        elif not isinstance(self.data, dict):
            raise ValueError("Data must be a dictionary to add more values")
        self.data[name] = values

    @property
    def overall_status(self) -> ProgressStatus:
        """Get overall status"""
        return self._overall_status
    
    @overall_status.setter
    def overall_status(self, value: Union[ProgressStatus, str]) -> None:
        """Set overall status"""
        self._overall_status = to_enum(value=value,enum_class=ProgressStatus,required=True, default=ProgressStatus.UNKNOWN)

    @property
    def execution_state(self) -> List[str]:
        """Get execution state"""
        return self._execution_state

    @property
    def execution_state_str(self) -> str:
        """Get execution state as a formatted string"""
        return "\n".join(f">>[[{entry}]]" for entry in self._execution_state)

    def add_state(self, state: str) -> None:
        """Add execution state with a timestamp"""
        timestamp = datetime.now(timezone.utc).isoformat()
        self._execution_state.append(f"[t:{timestamp}]--{state}")

    @property
    def issues(self) -> List[Any]:
        """Get issues"""
        return self._issues

    @property
    def issues_str(self) -> str:
        """Get issues as a string"""
        return "\n".join(f">>[i:{issue}]" for issue in self._issues)

    def add_issue(self, issue: Any) -> None:
        """Add issue"""
        self._issues.append(issue)

    @property
    def warnings(self) -> List[Any]:
        """Get warnings"""
        return self._warnings

    @property
    def warnings_str(self) -> str:
        """Get warnings as a string"""
        return "\n".join(f">>[w:{warning}]" for warning in self._warnings)

    def add_warning(self, warning: Any) -> None:
        """Add warning"""
        self._warnings.append(warning)

    @property
    def notices(self) -> List[Any]:
        """Get notices"""
        return self._notices

    @property
    def notices_str(self) -> str:
        """Get notices as a string"""
        return "\n".join(f">>[n:{notice}]" for notice in self._notices)

    def add_notice(self, notice: Any) -> None:
        """Add notice"""
        self._notices.append(notice)


    @property
    def get_notes(self) -> str:
        """Get all notes"""
        return f">>ISSUES: {self.issues_str}\n >>WARNINGS:{self.warnings_str}\n >>NOTICES:{self.notices_str}"
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Get metadata"""
        return self._metadata
    
    @metadata.setter
    def metadata(self, value: Dict[str, Any]) -> None:
        """Set metadata"""
        self._metadata = value

    def add_metadata(self, **kwargs) -> None:
        """Add metadata key-value pairs"""
        self.metadata.update(kwargs)

    @property
    def start_time(self) -> datetime:
        """Get start time"""
        return self._start_time
    
    
    @property
    def elapsed_time(self) -> float:
        """Get elapsed time in seconds"""
        return (datetime.now(timezone.utc) - self.start_time).total_seconds()
    @property
    def duration_s(self) -> float:
        """Get duration in seconds"""
        return self._duration_s
    
    @duration_s.setter
    def duration_s(self, value: float) -> None:
        """Set duration in seconds"""
        self._duration_s = value

    def set_duration(self) -> None:
        """Set final duration  in seconds"""
        self._duration_s =(datetime.now(timezone.utc) - self.start_time).total_seconds()

    @property
    def total_operations(self) -> int:
        """Get total operations"""
        return self._total_operations

    @total_operations.setter
    def total_operations(self, value: int) -> None:
        """Set total operations"""
        self._total_operations = value

    def increment_total_operations(self, value: int) -> None:
        """Increment total operations"""
        self._total_operations += value

    @property
    def is_closed(self) -> bool:
        """Check if operation is closed"""
        return self.overall_status in ProgressStatus.closed_or_skipped_statuses()

    def integrate_result(self, child_result: "OpResult", combine_status=True,  skip_data: bool = True, skip_metadata:bool=True) -> None:
        """Integrate a child operation result into this result"""
        # Add child's operation ID to execution state
        self.add_state(f"Integrating Child OpR {child_result.operation_id}")

        # Aggregate issues, warnings, notices
        self._issues.extend(child_result.issues)
        self._warnings.extend(child_result.warnings)
        self._notices.extend(child_result.notices)

        # Merge execution states
        self._execution_state.extend(child_result.execution_state)

        # Merge metadata
        if not skip_metadata:
            self._metadata.update(child_result.metadata)

        # Sum total operations
        self.increment_total_operations(child_result.total_operations)

        # Optionally merge data
        if not skip_data and child_result.data:
            if self._data is None:
                self._data = child_result.data
            elif isinstance(self._data, dict) and isinstance(child_result.data, dict):
                self._data.update(child_result.data)

        # Determine overall status using priority
        if combine_status:
            self.overall_status = evaluate_combined_progress_status(
                [self.overall_status, child_result.overall_status]
            )

    
    def final(self, status:Optional[ProgressStatus]=None, force_if_closed:bool=True, raise_issue_on_unknown:bool=True) -> None:
        """Mark operation as complete"""


        if self.is_closed:
            if force_if_closed and status:
                if self.overall_status in ProgressStatus.issue_statuses():
                    self.warnings.append(f"Operation is already closed at value {self.overall_status}, forcing status to {status}")
                else:
                    self.notices.append(f"Operation is already closed at value {self.overall_status}, forcing status to {status}")
                self.overall_status = to_enum(value=status,enum_class=ProgressStatus,required=True, default=ProgressStatus.UNKNOWN)
            else:
                self.warnings.append(f"Operation is already closed, not changing status to {status}")
        elif status:
            self.overall_status = to_enum(value=status,enum_class=ProgressStatus,required=True, default=ProgressStatus.UNKNOWN)
            if self.overall_status == ProgressStatus.UNKNOWN:
                if raise_issue_on_unknown:
                    raise ValueError("Invalid final Progress Status provided")
                else :
                    self.warnings.append(f"Invalid final Progress Status provided: {status}")
        elif self.issues:
            self.overall_status = ProgressStatus.FINISHED_WITH_ISSUES
        elif self.warnings:
            self.overall_status = ProgressStatus.DONE_WITH_WARNINGS
        elif self.notices:
            self.overall_status = ProgressStatus.DONE_WITH_NOTICES
        else:
            self.overall_status = ProgressStatus.DONE
        self._end_time = datetime.now(timezone.utc)
        if self.overall_status == ProgressStatus.UNKNOWN and raise_issue_on_unknown:
                    raise ValueError("Invalid final Progress Status provided")
        self.set_duration()
        self.add_state("CLOSED STATUS")


    

    @property
    def info(self) -> str:
        """Get all information as a JSON string"""
        return json.dumps({
            "overall_status": self.overall_status.name,
            "operation_id": self.operation_id,
            "execution_state": self.execution_state_str,
            "issues": self.issues_str,
            "warnings": self.warnings_str,
            "notices": self.notices_str,
            "metadata": self.metadata,
            "total_operations": self.total_operations,
            "start_time": self.start_time.isoformat(),
            "duration_s": self.duration_s
        }, default=str, indent=2)
    
    def __str__(self) -> str:
        """String representation of the object"""
        return self.info

    def to_dict(self, infos_as_str: bool = True) -> Dict[str, Any]:
        """Convert to dictionary format"""
        return {
            "data": self.data,
            "status": {
                "overall_status": self.overall_status.name,
                "operation_id": self.operation_id,
                "execution_state": self.execution_state_str if infos_as_str else self.execution_state,
                "issues": self.issues_str if infos_as_str else self.issues,
                "warnings": self.warnings_str if infos_as_str else self.warnings,
                "notices": self.notices_str if infos_as_str else self.notices,
                "metadata": json.dumps(self.metadata, default=str, indent=2) if infos_as_str else self.metadata,
                "total_operations": self.total_operations,
                "start_time": self.start_time.isoformat(),
                "duration_s": self.duration_s
            }
        }
