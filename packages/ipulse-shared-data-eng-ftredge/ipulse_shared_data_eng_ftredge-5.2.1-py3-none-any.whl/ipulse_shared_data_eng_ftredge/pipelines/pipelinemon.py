# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=logging-fstring-interpolation
# pylint: disable=line-too-long
# pylint: disable=missing-class-docstring
# pylint: disable=broad-exception-caught
import json
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from contextlib import contextmanager
from typing import List, Optional, Union, Set, Dict, Any
import logging
from ipulse_shared_base_ftredge import LogLevel, AbstractResource, ProgressStatus, Action, Alert, ReviewStatus, Resource
from .pipelinelog import  PipelineLog as PLog

############################################################################
##### PIPINEMON Collector for Logs and Statuses of running pipelines #######
class Pipelinemon:
    """A class for collecting logs and statuses of running pipelines.
    This class is designed to be used as a context manager, allowing logs to be
    collected, stored and reported in a structured format. The logs can be retrieved and
    analyzed at the end of the pipeline executieon, or only the counts.
    """

    # LEVELS_DIFF = 10000  # The difference in value between major log levels

    def __init__(self, base_context: str, logger,
                 max_log_field_len:Optional[int]=8000, #by detault PipelineLog has 8000 per field length Limit
                 max_log_dict_byte_size:Optional[float]=256 * 1024 * 0.80): #by detault PipelineLog dict has 256 * 1024 * 0.80 -80% of 256Kb Limit 
        self._id = str(uuid.uuid4())
        self._logs = []
        self._early_stop = False
        self._early_stop_reason = None  # Track what caused early stop
        self._systems_impacted = []
        self._by_event_count = defaultdict(int)
        self._by_level_code_count = defaultdict(int)
        self._base_context = base_context
        self._context_stack = []
        self._logger = logger
        self._max_log_field_len = max_log_field_len
        self._max_log_bytes_limit = max_log_dict_byte_size
        self._start_time = None  # Add start time variable

    @contextmanager
    def context(self, context: str):
        """Safer context management with type checking"""
        if not isinstance(context, str):
            raise TypeError("Context must be a string")
        self.push_context(context)
        try:
            yield
        finally:
            self.pop_context()

    def push_context(self, context):
        self._context_stack.append(context)

    def pop_context(self):
        if self._context_stack:
            self._context_stack.pop()

    @property
    def current_context(self):
        return " >> ".join(self._context_stack)

    @property
    def base_context(self):
        return self._base_context
    
    @base_context.setter
    def base_context(self, value):
        self._base_context = value

    @property
    def id(self):
        return self._id
    
    @property
    def by_event_count(self):
        return dict(self._by_event_count)

    @property
    def by_level_code_count(self):
        return dict(self._by_level_code_count)

    @property
    def systems_impacted(self):
        return self._systems_impacted

    @systems_impacted.setter
    def systems_impacted(self, list_of_si: List[str]):
        self._systems_impacted = list_of_si

    def add_system_impacted(self, system_impacted: str)-> None:
        if self._systems_impacted is None:
            self._systems_impacted = []
        self._systems_impacted.append(system_impacted)

    def clear_systems_impacted(self):
        self._systems_impacted = []

    @property
    def max_log_dict_byte_size(self):
        return self._max_log_bytes_limit

    @max_log_dict_byte_size.setter
    def max_log_dict_byte_size(self, value):
        self._max_log_bytes_limit = value

    @property
    def max_log_field_size(self):
        return self._max_log_field_len

    @max_log_field_size.setter
    def max_log_field_size(self, value):
        self._max_log_field_len = value

    @property
    def max_log_traceback_lines(self):
        return self._max_log_traceback_lines

    @max_log_traceback_lines.setter
    def max_log_traceback_lines(self, value):
        self._max_log_traceback_lines = value

    @property
    def early_stop(self):
        return self._early_stop

    def set_early_stop(self, reason: str):
        """Sets the early stop flag and optionally logs an error."""
        self._early_stop = True
        self._early_stop_reason = reason  # Store the reason for early stop
        

    def reset_early_stop(self):
        self._early_stop = False

    @property
    def early_stop_reason(self):
        return self._early_stop_reason


    def start(self, pipeline_description: str):
        """Logs the start of the pipeline execution."""
        self._start_time = datetime.now(timezone.utc)  # Capture the start time
        self.add_log(PLog(
                        level=LogLevel.INFO,
                        resource=AbstractResource.PIPELINE_MONITOR,
                        action= Action.EXECUTE,
                        progress_status=ProgressStatus.IN_PROGRESS,
                        description=pipeline_description
                    ))

    def get_duration_since_start(self) -> Optional[str]:
        """Returns the duration since the pipeline started, formatted as HH:MM:SS."""
        if self._start_time is None:
            return None
        elapsed_time = datetime.now(timezone.utc) - self._start_time
        return str(elapsed_time)


    def _update_counts(self, log: PLog, remove=False):
        event_tuple = log.getEvent()
        level = log.level

        if remove:
            self._by_event_count[event_tuple] -= 1
            self._by_level_code_count[level.value] -= 1
        else:
            self._by_event_count[event_tuple] += 1
            self._by_level_code_count[level.value] += 1


    def add_log(self, log: PLog ):
        log.base_context = self.base_context
        log.context = self.current_context if self.current_context else "root"
        log.collector_id = self.id
        log.systems_impacted = self.systems_impacted
        log_dict = log.to_dict(max_field_len=self.max_log_field_size,
                               byte_size_limit=self.max_log_dict_byte_size)
        self._logs.append(log_dict)
        self._update_counts(log=log)  # Pass the context to _update_counts

        if self._logger:
            # We specifically want to avoid having an ERROR log level for this structured Pipelinemon reporting, to ensure Errors are alerting on Critical Application Services.
            # A single ERROR log level is usually added at the end of the entire pipeline
            if log.level.value >= LogLevel.WARNING.value:
                self._logger.warning(log_dict)
            elif log.level.value >= LogLevel.INFO.value:
                self._logger.info(log_dict)
            else:
                self._logger.debug(log_dict)

    def add_logs(self, logs: List[PLog]):
        for log in logs:
            self.add_log(log)

    def clear_logs_and_counts(self):
        self._logs = []
        self._by_level_code_count = defaultdict(int)
        self._by_event_count= defaultdict(int)
    

    def clear_logs(self):
        self._logs = []

    def get_all_logs(self,in_json_format=False):
        if in_json_format:
            return json.dumps(self._logs)
        return self._logs

    def contains_any_logs_for_levels(
        self,
        levels: Union[LogLevel, List[LogLevel]],
    ) -> bool:
        """
        Checks if any logs exist at the given log level(s).
        """
        if isinstance(levels, LogLevel):
            levels = [levels]
        return any(
            self.by_level_code_count.get(lvl.value, 0) > 0
            for lvl in levels
        )
    def contains_any_errors(self) -> bool:
        """
        Check if any logs exist at WARNING level or higher.
        (WARNING, ERROR, CRITICAL, etc.)
        """
        return any(
            count > 0 and code >= LogLevel.ERROR.value
            for code, count in self.by_level_code_count.items()
        )
    

    def count_total_logs_for_levels(self, level:  Union[LogLevel, List[LogLevel]]) -> int:
        """
        Returns the total number of logs at a specific level or list of levels (long-term memory).
        """
        if isinstance(level, LogLevel):
            level = [level]
        return sum(
            count
            for code, count in self.by_level_code_count.items()
            if code in {lvl.value for lvl in level}
        )


    def count_warnings_and_errors(self) -> int:
        """
        Count logs at WARNING level or higher.
        (WARNING, ERROR, CRITICAL, etc.)
        """
        return sum(
            count
            for code, count in self.by_level_code_count.items()
            if code >= LogLevel.WARNING.value
        )



    
    ######### VERY IMPORTANT FUNCTION FOR COUNTING #########
    def count_logs_for_events_containing(
    self, 
    levels: Union[LogLevel, List[LogLevel]], 
    context: Optional[str] = None, 
    exclude_nested_contexts: bool = False, 
    progress_status: Optional[Union[ProgressStatus, set, frozenset]] = None, 
    resource: Optional[Resource] = None
    ) -> int:
        """Count logs matching specified criteria.
        
        Args:
            levels: LogLevel(s) to match
            context: Context to filter by
            exclude_nested_contexts: If True, match context exactly
            progress_status: Single ProgressStatus, set/frozenset of ProgressStatus values,
                            or a ProgressStatus class attribute containing a frozenset
            resource: Optional resource type to filter by
        """
        # Convert single LogLevel to a list
        if isinstance(levels, LogLevel):
            levels = [levels]
        level_values = {level.value for level in levels}

        # Convert progress_status to set of names if needed
        allowed_status_names = None
        if progress_status is not None:
            # 1) If it's a set/frozenset of statuses
            if isinstance(progress_status, (set, frozenset)):
                # Each element should be a ProgressStatus
                allowed_status_names = {ps.name for ps in progress_status if isinstance(ps, ProgressStatus)}
            # 2) If it's a single ProgressStatus
            elif isinstance(progress_status, ProgressStatus):
                allowed_status_names = {progress_status.name}
            # else: leave it as None to skip status filtering
        

        def matches_criteria(log: Dict[str, Any]) -> bool:
            # Check level
            if log["level_code"] not in level_values:
                return False

            # Check context
            if context is not None:
                log_ctx = log.get("context", "")
                if exclude_nested_contexts:
                    if log_ctx != context:
                        return False
                else:
                    if not log_ctx.startswith(context):
                        return False

            # Check resource
            if resource is not None and log.get("resource") != resource.name:
                return False

            # Check progress status
            if allowed_status_names is not None:
                if log.get("progress_status") not in allowed_status_names:
                    return False

            return True

        return sum(matches_criteria(log) for log in self._logs)
    


    def count_logs_for_current_context(
        self, 
        levels: Union[LogLevel, List[LogLevel]],
        exclude_nested_contexts: bool = False,
        progress_status: Optional[ProgressStatus] = None
    ) -> int:
        """Count logs in current context matching criteria."""
        return self.count_logs_for_events_containing(
            levels=levels,
            context=self.current_context,
            exclude_nested_contexts=exclude_nested_contexts,
            progress_status=progress_status
        )
    
    def count_statuses_for_resource(
        self,
        status: ProgressStatus,
        resource: Resource,
        context: Optional[str] = None,
    ) -> int:
        """
        Count pipeline events with a specific status, regardless of log level.

        Args:
            progress_status: Status to count (e.g., COMPLETED, FAILED).
            resource: Resource type to filter by.
            context: Optional context to filter by.
        """
        return self.count_logs_for_events_containing(
            levels=list(LogLevel),  # all known log levels
            context=context,
            progress_status=status,
            resource=resource
        )

    def generate_execution_summary(self, countable_subj_name: str, total_countables: int, subj_resource:Resource=AbstractResource.PIPELINE_SUBJECT ) -> str:
        """Generate summary of pipeline execution."""

        duration = self.get_duration_since_start()
        
        # Count various statuses for pipeline resource/subject/iteration
        success = self.count_statuses_for_resource(status=ProgressStatus.success_statuses(), resource=subj_resource)
        issue = self.count_statuses_for_resource(status=ProgressStatus.closed_issue_statuses(), resource=subj_resource)
        unfinished = self.count_statuses_for_resource(status=ProgressStatus.UNFINISHED, resource=subj_resource)
        skipped = self.count_statuses_for_resource(status=ProgressStatus.skipped_statuses() ,resource=subj_resource)
        pending = self.count_statuses_for_resource(status=ProgressStatus.pending_statuses(), resource=subj_resource)
        done_with_notices= self.count_statuses_for_resource(status=ProgressStatus.DONE_WITH_NOTICES, resource=subj_resource)
        done_with_warnings= self.count_statuses_for_resource(status=ProgressStatus.DONE_WITH_WARNINGS, resource=subj_resource)
        
        # Count different log levels
        errors = self.count_total_logs_for_levels([LogLevel.ERROR, LogLevel.CRITICAL])
        warnings = self.count_total_logs_for_levels(LogLevel.WARNING)
        notices = self.count_total_logs_for_levels(LogLevel.NOTICE)
        infos = self.count_total_logs_for_levels(LogLevel.INFO)
        debugs = self.count_total_logs_for_levels(LogLevel.DEBUG)

        summary = f"""
        --------------------------------------------------
        Pipeline Execution Report
        --------------------------------------------------
        Base Context: {self.base_context}
        Pipeline ID: {self.id}
        Early Stop: {self.early_stop}
        Early Stop Reason: {self.early_stop_reason}
        Duration: {duration}

        --------------------------------------------------
        Status Summary:
        --------------------------------------------------
        - Done {subj_resource.name.lower()}(s): [{success}/{total_countables}] {countable_subj_name}(s)
            - Of Which Done With Notices: [{done_with_notices}]
            - Of Which Done With Warnings: [{done_with_warnings}]
        - Issue/Error  {subj_resource.name.lower()}(s): [{issue}/{total_countables}] {countable_subj_name}(s)
           - Of Which Unfinished: [{unfinished}]
        - Skipped  {subj_resource.name.lower()}(s): [{skipped}/{total_countables}] {countable_subj_name}(s)
        - Unfinished  {subj_resource.name.lower()}(s): [{pending}/{total_countables}] {countable_subj_name}(s)
        - Pending  {subj_resource.name.lower()}(s): [{pending}/{total_countables}] {countable_subj_name}(s)

        --------------------------------------------------
        Log Level Summary:
        --------------------------------------------------
        - Debugs: {debugs}
        - Infos: {infos}
        - Notices: {notices}
        - Warnings: {warnings}
        - Errors: {errors}
        --------------------------------------------------
        """
        return summary
    
    def get_breakdown_by_event(self):
        """Returns a str event breakdowns."""
        breakdown_print = """
        --------------------------------------------------
        Detailed Event Breakdown:
        --------------------------------------------------
        """
        for event, count in self._by_event_count.items():
            breakdown_print += f"\n     - {event}: {count}  "
        
        breakdown_print += "\n      -------------------------------------------------- \n"
        
        return breakdown_print
    
    def log_final_description(self, final_level:LogLevel, countable_subj_name: str, total_countables: int, final_description: Optional[str]=None, generallogger: Optional[logging.Logger]=None):
        if final_description:
            final_log_message = final_description
        else:
            final_log_message = self.generate_execution_summary(countable_subj_name=countable_subj_name, total_countables=total_countables)

        
        if final_level == LogLevel.ERROR:
            generallogger.error(final_log_message)
        elif final_level == LogLevel.WARNING:
            generallogger.warning(final_log_message)
        else:
            generallogger.info(final_log_message)

    def end(self, countable_subj_name: str, total_countables: int, generallogger: Optional[logging.Logger]=None):
        """Logs the end of the pipeline execution with the appropriate final status.
        Args: 
            countable_subj_name (str): The reference name for the countables processed. --> Can be Tasks, Iterations, Items, Tickers etc.
            total_countables (int): The total number of countables processed in the pipeline.
            generallogger (Optional[logging.Logger], optional): The logger to use for the final log message.
            """

        execution_duration = self.get_duration_since_start()
        final_level = LogLevel.INFO
        description = f"Pipeline execution completed in {execution_duration}."
        progress_status = ProgressStatus.DONE
        if self.early_stop:
            final_level = LogLevel.ERROR
            description = f"Pipeline execution stopped early due to {self.early_stop_reason}. Execution Duration: {execution_duration}."
            progress_status = ProgressStatus.FAILED
        elif self.contains_any_errors():
            final_level = LogLevel.ERROR
            description = f"Pipeline execution completed with errors. Execution Duration: {execution_duration}."
            progress_status = ProgressStatus.FINISHED_WITH_ISSUES
        elif self.contains_any_logs_for_levels(levels= LogLevel.WARNING):
            final_level = LogLevel.WARNING
            description = f"Pipeline execution completed with warnings. Execution Duration: {execution_duration}."
            progress_status = ProgressStatus.DONE_WITH_WARNINGS
        elif self.contains_any_logs_for_levels(levels= LogLevel.NOTICE):
            final_level = LogLevel.NOTICE
            description = f"Pipeline execution completed with notices. Execution Duration: {execution_duration}."
            progress_status = ProgressStatus.DONE_WITH_NOTICES
            
        
        execution_summary = self.generate_execution_summary(countable_subj_name=countable_subj_name, total_countables=total_countables, subj_resource=AbstractResource.PIPELINE_SUBJECT)
        pipeline_description= description + " \n" + execution_summary

       # TODO CHECK IF IT'S WORTH ADDING A LOG FOR STRT AND END OF PIPELINE MONITOR
        self.add_log(PLog(
            level=final_level,
            resource=AbstractResource.PIPELINE_MONITOR,
            action= Action.EXECUTE,
            progress_status=progress_status,
            description=pipeline_description
        ))

        final_pipeline_descirption_message = pipeline_description + " \n" + self.get_breakdown_by_event()

        if generallogger:
            self.log_final_description(final_level=final_level, countable_subj_name=countable_subj_name, total_countables=total_countables,
                                       final_description=final_pipeline_descirption_message, generallogger=generallogger)