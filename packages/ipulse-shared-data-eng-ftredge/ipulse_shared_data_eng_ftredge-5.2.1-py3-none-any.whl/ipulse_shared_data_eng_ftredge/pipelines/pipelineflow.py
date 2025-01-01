""" Shared pipeline configuration utility. """
import uuid
from typing import List, Optional, Dict, Union,Any
import copy
from collections import defaultdict

from ipulse_shared_base_ftredge import (Action, DataResource, DatasetScope, ProgressStatus)

# PENDING_STATUSES = {
#     ProgressStatus.NOT_STARTED,
#     ProgressStatus.STARTED,
#     ProgressStatus.IN_PROGRESS,
#     ProgressStatus.PAUSED,
#     ProgressStatus.UNKNOWN,
#     ProgressStatus.BLOCKED_BY_UNRESOLVED_DEPENDENCY
# }

# SKIPPED_STATUSES = {
#     ProgressStatus.INTENTIONALLY_SKIPPED,
#     ProgressStatus.CANCELLED,
#     ProgressStatus.DISABLED
# }

# SUCCESS_STATUSES = {
#     ProgressStatus.DONE,
#     ProgressStatus.DONE_WITH_NOTICES,
#     ProgressStatus.DONE_WITH_WARNINGS
# }

# CLSOED_ISSUE_STATUSES = {
#     ProgressStatus.FINISHED_WITH_ISSUES,
#      ProgressStatus.UNFINISHED,
#     ProgressStatus.FAILED,
# }

# ISSUE_STATUSES = {ProgressStatus.UNKNOWN}.union(CLSOED_ISSUE_STATUSES)
# FAILED_OR_SKIPPED_STATUSES = {ProgressStatus.FAILED}.union(SKIPPED_STATUSES)
# PROCESSED_STATUSES = SUCCESS_STATUSES.union({ProgressStatus.FINISHED_WITH_ISSUES,
#                                             ProgressStatus.FAILED,
#                                             ProgressStatus.STARTED,
#                                             ProgressStatus.IN_PROGRESS})
# NOT_STARTED_OR_SKIPPED_STATUSES= {ProgressStatus.NOT_STARTED}.union(SKIPPED_STATUSES)
# SUCCESS_OR_SKIPPED_STATUSES = SUCCESS_STATUSES.union(SKIPPED_STATUSES)
# CLOSED_STATUSES=SUCCESS_OR_SKIPPED_STATUSES.union(CLSOED_ISSUE_STATUSES)
# CLSOED_OR_SKIPPED_STATUSES=CLSOED_ISSUE_STATUSES.union(SKIPPED_STATUSES)

# def calculate_status_counts(statuses: List[ProgressStatus]) -> Dict[str, Any]:
#     """
#     Calculate counts of statuses in a list.
#     Returns a dictionary with counts of each status.
#     """
#     status_counts = defaultdict(int)
#     status_counts = {
#         'total_statuses': len(statuses),
#         'detailed': defaultdict(int),
#         'by_category': {
#             'PENDING_STATUSES': 0,
#             'SUCCESS_STATUSES': 0,
#             'SKIPPED_STATUSES': 0,
#             'CLSOED_ISSUE_STATUSES': 0,
#             'ISSUE_STATUSES': 0,
#             'FAILED_OR_SKIPPED_STATUSES': 0,
#             'PROCESSED_STATUSES': 0,
#             'NOT_STARTED_OR_SKIPPED_STATUSES': 0,
#             'SUCCESS_OR_SKIPPED_STATUSES': 0,
#             'CLOSED_STATUSES': 0,
#             'CLSOED_OR_SKIPPED_STATUSES': 0
#         }
#     }

#     # Count individual statuses
#     for status in statuses:
#         status_counts["detailed"][status.name] += 1

#         for category in status_counts["by_category"]:
#             if status in globals()[category]:
#                 status_counts["by_category"][category] += 1
#     return {
#         "detailed": dict(status_counts["detailed"]),
#         "by_category": dict(status_counts["by_category"]),
#         "total_statuses": status_counts["total_statuses"]
#     }

def calculate_status_counts(statuses: List[ProgressStatus]) -> Dict[str, Any]:
    """
    Calculate counts of statuses in a list.
    Returns a dictionary with counts of each status.
    """
    # Dynamically fetch all status group attributes from ProgressStatus
    status_groups = {
        attr: getattr(ProgressStatus, attr)
        for attr in dir(ProgressStatus)
        if attr.isupper() and isinstance(getattr(ProgressStatus, attr), frozenset)
    }

    status_counts = {
        'total_statuses': len(statuses),
        'detailed': defaultdict(int),
        'by_category': {group_name: 0 for group_name in status_groups}
    }

    # Count individual statuses
    for status in statuses:
        status_counts["detailed"][status.name] += 1

        # Count statuses in each group
        for group_name, group_set in status_groups.items():
            if status in group_set:
                status_counts["by_category"][group_name] += 1

    return {
        "detailed": dict(status_counts["detailed"]),
        "by_category": dict(status_counts["by_category"]),
        "total_statuses": status_counts["total_statuses"]
    }


def extract_statuses(steps: Union[List[Union['PipelineTask', 'PipelineDynamicGroupOfIterations', 'PipelineSequence']],
                                 Dict[str, Union['PipelineTask', 'PipelineDynamicGroupOfIterations', 'PipelineSequence' ]]]) -> List[ProgressStatus]:
    """Extract statuses from a list of steps."""
    if isinstance(steps, dict):
        steps = list(steps.values())
    return [step.status for step in steps]



def calculate_overall_status(status_counts:Dict[str, int],
                             current_status:Optional[ProgressStatus]=None,
                             final:bool=False) -> ProgressStatus:
    """
    Calculate the current status of the iteration based on task statuses.
    
    Returns:
        ProgressStatus: Current status of the iteration
    """

    total_statuses = status_counts['total_statuses']

    if current_status and current_status not in ProgressStatus.PENDING_STATUSES:
        return current_status

    if final:
        # If ANY pending tasks, and status is final, return unfinished
        if status_counts["by_category"]['PENDING_STATUSES'] > 0:
            if status_counts["by_category"]['ISSUE_STATUSES'] >0:
                return ProgressStatus.FAILED # if there are issues and pending tasks, return failed
            return ProgressStatus.UNFINISHED # if there are pending tasks but no issues, return unfinished
        
        # Means noting is pending
        if status_counts["by_category"]['ISSUE_STATUSES'] >0:
            if status_counts["by_category"]['FAILED_OR_SKIPPED'] == total_statuses:
                return ProgressStatus.FAILED
            else:
                return ProgressStatus.FINISHED_WITH_ISSUES

        if status_counts["detailed"]['DONE_WITH_WARNINGS'] > 0:
            return ProgressStatus.DONE_WITH_WARNINGS

        # All non-skipped tasks successful but some have notices
        if status_counts["detailed"]['DONE_WITH_NOTICES'] > 0:
            return ProgressStatus.DONE_WITH_NOTICES
        return ProgressStatus.DONE
    else:
        if status_counts["by_category"]['PENDING_STATUSES'] == 0:
            return calculate_overall_status(status_counts, current_status, final=True)
        
        if status_counts["by_category"]['NOT_STARTED_OR_SKIPPED_STATUSES']==total_statuses:
            return ProgressStatus.NOT_STARTED
        
        return ProgressStatus.IN_PROGRESS


class PipelineTask:
    """
    Represents a single task in a pipeline.
    """
    def __init__(
        self,
        n: str,
        a: Optional[Action] = None,
        s: Optional[DataResource] = None,
        d: Optional[DataResource] = None,
        scope: Optional[DatasetScope] = None,
        dependencies: Optional[List[str]] = None,
        disabled: bool = False,
        config: Optional[Dict] = None,
    ):
        """
        Initialize a PipelineTask.
        :param n: Name of the task.
        :param s: Source of data for the task.
        :param a: Action to perform.
        :param d: Destination for the task output.
        :param scope: Scope of the dataset being processed.
        :param dependencies: List of task names that this task depends on.
        :param config: Task-specific configuration.
        :param enabled: Whether the task is enabled.
        """
        self.id=uuid.uuid4()
        self.name = n
        self.action = a
        self.source = s
        self.destination = d
        self.data_scope = scope
        self.dependencies = dependencies or []
        self.config = config or {}
        self.disabled = disabled
        self._status = ProgressStatus.DISABLED if self.disabled else ProgressStatus.NOT_STARTED
        # self.completed = False  # Tracks whether the step is completed
        self.pipeline_flow = None  # Reference to the parent PipelineFlow

    @property
    def is_success(self) -> bool:
        """Check if task is completed based on status"""

        return self.status in ProgressStatus.SUCCESS_STATUSES
    
    @property
    def is_success_or_skipped(self) -> bool:
        """Check if task is completed or skipped based on status"""
        return self.status in  ProgressStatus.SUCCESS_OR_SKIPPED_STATUSES
    
    @property
    def is_finished(self) -> bool:
        """Check if task is finished based on status"""
        return self.status not in ProgressStatus.PENDING_STATUSES
    
    @property
    def has_issues(self) -> bool:
        """Check if task has issues based on status"""
        return self.status in ProgressStatus.ISSUE_STATUSES
    
    @property
    def is_pending(self) -> bool:
        """Check if task is pending based on status"""
        return self.status in ProgressStatus.PENDING_STATUSES

    @property
    def status (self) -> ProgressStatus:
        return self._status
    
    @status.setter
    def status(self, s:ProgressStatus):
        self._status = s
        

    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow'):
        """
        Associate the task with a pipeline flow.
        :param pipeline_flow: The parent PipelineFlow.
        """
        self.pipeline_flow = pipeline_flow

    
    def validate_start(self, set_status:Optional[ProgressStatus]=ProgressStatus.IN_PROGRESS, sequence_ref:Optional[Union[int,str]]=None) -> bool:
        """
        Ensure the Group is enabled and all dependencies are completed.
        """
        ### TODO add check Dependency relationship requirement feature
        # Some Dependency must be in SUCCESS_STATUSES some in SUCCESS_OR_SKIPPED_STATUSES some simply EXECUTED_STATUSES some FAILED_OR_DONE_WiTH_ERRORS
        if self.disabled:
            self.status =ProgressStatus.DISABLED
            return False
        if self.status in ProgressStatus.SKIPPED_STATUSES:
            self.status = ProgressStatus.INTENTIONALLY_SKIPPED
            return False # Return True as the group is skipped
        if self.dependencies:
            for dependency_name in self.dependencies:
                dependency_step = self.pipeline_flow.get_step(name=dependency_name, sequence_ref=sequence_ref)
                if dependency_step.status not in ProgressStatus.SUCCESS_OR_SKIPPED_STATUSES:
                    self.status = ProgressStatus.BLOCKED_BY_UNRESOLVED_DEPENDENCY
                    return False
        self.status = set_status
        return True

    def nb_tasks(self) -> int:
        """Get the total number of tasks in the group."""
        return 1
    

    def __str__(self):
        if self.is_success:
            status_symbol = "✔"
        elif self.status in ProgressStatus.ISSUE_STATUSES :
            status_symbol = "✖"
        elif self.status in ProgressStatus.PENDING_STATUSES:
            status_symbol = "..."
        elif self.status in ProgressStatus.SKIPPED_STATUSES:
            status_symbol = "//"
        else:
            status_symbol = "?"

        parts = [f">> {self.name}"]
        if self.action:
            parts.append(self.action.value)
        if self.source:
            parts.append(f"from {self.source.value}")
        if self.destination:
            parts.append(f"to {self.destination.value}")
        if self.data_scope:
            parts.append(f"scope={self.data_scope.value}")
        
        parts.append(f"[Status: {status_symbol} {self.status.name}] ")
        return f"{' :: '.join(parts)}"


class PipelineSequenceTemplate:
    """
    Represents a single iteration of a dynamic iteration group.
    """
    def __init__(self,
                 steps: List[Union['PipelineTask', 'PipelineDynamicGroupOfIterations']]):
        # self.iteration_ref = iteration_ref
        self.steps: Dict[str, Union['PipelineTask', 'PipelineDynamicGroupOfIterations']] = {step.name: step for step in steps}

    def clone_steps(self) -> Dict[str, Union['PipelineTask', 'PipelineDynamicGroupOfIterations']]:
        """Create a deep copy of the steps for a new iteration."""
        
        return {name: copy.deepcopy(step) for name, step in self.steps.items()}
    
    @property
    def nb_tasks(self) -> int:
        return sum(
            step.nb_tasks() if hasattr(step, 'nb_tasks') else 1
            for step in self.steps.values() if step.disabled
        )
    
    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow'):
        """Associate the iteration's tasks with the pipeline flow."""
        for step in self.steps.values():
            step.set_pipeline_flow(pipeline_flow)

    def __str__(self):
        # iteration_status = f"[Iteration {self.iteration_ref} :: Status: {self.status.value}]"
        steps_str = "\n".join(f"    {str(step)}" for step in self.steps.values())
        # return f"{iteration_status}\n{steps_str}"
        return steps_str
    

class PipelineSequence:
    """
    Represents a single iteration of a dynamic iteration group.
    """

    def __init__(self,
                 sequence_template: PipelineSequenceTemplate,
                 sequence_ref: Union[int, str]):
        self.sequence_ref = sequence_ref
        self.steps = sequence_template.clone_steps()
        self._status = ProgressStatus.NOT_STARTED
        self.pipeline_flow = None  # Reference will be set later
        self.status_counts = None


    @property
    def status(self) -> ProgressStatus:
        """
        Get the current status of the sequence.
        """
        return self._status
    
    @status.setter
    def status(self, s: ProgressStatus):
        self._status = s

   
    def update_status_counts_and_overall_status(self, final:bool):
        """
        Update the current status of the sequence based on task statuses.
        If iteration is in PENDING state, evaluate progress without failing for pending tasks.
        Otherwise return existing final status.
        """
        statuses=extract_statuses(self.steps)
        self.status_counts = calculate_status_counts(statuses)
        self.status = calculate_overall_status(status_counts=self.status_counts,current_status=self.status,final=final)

    @property
    def nb_tasks(self) -> int:
        return sum(
            step.nb_tasks() if hasattr(step, 'nb_tasks') else 1
            for step in self.steps.values() if not step.disabled
        )

    ######## TODO ENSURE THIS IS CALCULATED TAKING INTO ACCOUNT THE NUMBER OF TASKS IN THE ITERATION AND POSSIBLY DYNAMIC ITERATION GROUPS WITHIN
    # @property
    # def progress_percentage(self) -> float:
    #     """
    #     Compute the progress percentage for the sequence.
    #     :return: Progress as a float percentage.
    #     """
    #    pass 
        


    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow'):
        """Associate the sequence's tasks with the pipeline flow."""
        self.pipeline_flow = pipeline_flow
        for step in self.steps.values():
            step.set_pipeline_flow(pipeline_flow)

    def close(self):
        """
        Close the sequence and set the status to disabled.
        """
        self.update_status_counts_and_overall_status(final=True)

    def __str__(self):
        """
        Generate a string representation of the sequence. Doesn't update status. Ensure status is updated before calling.
        """
        sequence_status = f"[Sequence {self.sequence_ref} :: Status: {self.status.value}]"
        steps_str = "\n".join(f"    {str(step)}" for step in self.steps.values())
        return f"{sequence_status}\n{steps_str}"
    

class PipelineDynamicGroupOfIterations:
    def __init__(self,
                 name: str,
                 iteration_template: PipelineSequenceTemplate,
                 disabled: bool = False,
                 dependencies: Optional[List[str]] = None,
                 max_iterations: Optional[int] = 100,
                 ):
        """
        Initialize the PipelineDynamicIterationGroup.

        :param name: Name of the loop group.
        :param task_templates: Templates of tasks that will be cloned for each iteration.
        :param enabled: Whether the loop group is enabled.
        :param dependencies: List of dependencies.
        :param max_iterations: Maximum number of iterations allowed. Useful to ensure termination within Cloud Function or other Execution environment.
        """
        self.name = name
        self.disabled = disabled
        self.dependencies = dependencies or []
        self.iteration_template:PipelineSequenceTemplate = iteration_template
        # self.iteration_statuses: Dict[Union[int, str], ProgressStatus] = {}
        self.status_counts = None
        self._iterations: Dict[Union[int, str], PipelineSequence] = {}
        self.max_iterations = max_iterations
        self._status = ProgressStatus.DISABLED if  self.disabled else ProgressStatus.NOT_STARTED
        self.pipeline_flow : PipelineFlow =None  # Reference will be set later

    
    
    @property
    def total_iterations(self) -> int:
        return len(self._iterations)
    
    @property
    def status(self) -> ProgressStatus:
        return self._status
        
    @status.setter
    def status(self, s:ProgressStatus):
        self._status = s
    
    @property
    def iterations(self) -> Dict[Union[int, str], PipelineSequence]:
        return self._iterations
    
    
    def set_iterations(self, iteration_refs: List[Union[int, str]]):
        self._iterations = {
            ref: PipelineSequence(self.iteration_template, ref)
            for ref in iteration_refs
        }
        for iteration in self.iterations.values():
            iteration.set_pipeline_flow(self.pipeline_flow)

    def get_iteration(self, iteration_ref: Union[int, str]) -> PipelineSequence:
        return self.iterations[iteration_ref]
    
    def add_iteration(self, iteration_ref: Union[int, str]):
        self.iterations[iteration_ref] = PipelineSequence(self.iteration_template, iteration_ref)
    
    def set_pipeline_flow(self, pipeline_flow: 'PipelineFlow'):
            """Associate the loop group and its iterations with the pipeline flow."""
            self.pipeline_flow = pipeline_flow

    # #TODO check if not better to get status of the iteration directly from the iteration object
    # def get_iteration_status(self, iteration_ref: Union[int,str]) -> ProgressStatus:
    #     """Retrieve the status for a specific iteration."""
        
    #     if iteration_ref not in self.iterations:
    #         raise ValueError(f"Iteration {iteration_ref} not found in group {self.name}")
    #     ## TODO : ADD UPDATER FUNCTION TO UPDATE THE STATUS OF THE ITERATIONS
    #     return self.iteration_statuses.get(iteration_ref, ProgressStatus.NOT_STARTED)
    
    def get_iteration_status(self, iteration_ref: Union[int,str]) -> ProgressStatus:
        """Retrieve the status for a specific iteration."""
        
        if iteration_ref not in self.iterations:
            raise ValueError(f"Iteration {iteration_ref} not found in group {self.name}")

        return self.iterations[iteration_ref].status

    def update_status_counts_and_overall_status(self, final:bool):
        """
        Update the current status of the sequence based on task statuses.
        If iteration is in PENDING state, evaluate progress without failing for pending tasks.
        Otherwise return existing final status.
        """
        if not self.iterations:
            return
        statuses=extract_statuses(self.iterations)
        self.status_counts = calculate_status_counts(statuses)
        self.status = calculate_overall_status(status_counts=self.status_counts,current_status=self.status,final=final)

    def close_step(self):
        """
        Close the group and set the status to disabled.
        """
        self.update_status_counts_and_overall_status(final=True)
    
    def get_status_counts_for_step_across_iterations(self, step_name: str) -> Dict[str, int]:
        """
        Get aggregated status counts for a specific task across all iterations.
        """
        status_counts = defaultdict(int)

        for iteration in self.iterations.values():
            if step_name in iteration.steps:
                status:ProgressStatus = iteration.steps[step_name].status
                status_counts[status.value] += 1
                    
        return dict (status_counts)


    def validate_start(self, set_status:Optional[ProgressStatus]=ProgressStatus.IN_PROGRESS) -> bool:
        """
        Ensure the Group is enabled and all dependencies are completed.
        """
        ### TODO add check Dependency relationship requirement feature
        # Some Dependency must be in SUCCESS_STATUSES some in SUCCESS_OR_SKIPPED_STATUSES some simply EXECUTED_STATUSES some FAILED_OR_DONE_WiTH_ERRORS
        if self.disabled:
            self.status =ProgressStatus.DISABLED
            return False
        if self.total_iterations == 0 or self.status in ProgressStatus.SKIPPED_STATUSES:
            self.status = ProgressStatus.INTENTIONALLY_SKIPPED
            return False # Return True as the group is skipped
        if self.max_iterations< self.total_iterations:
            self.status = ProgressStatus.FAILED
            raise ValueError(f"Total iterations {self.total_iterations} cannot be greater than max iterations {self.max_iterations}")
        if self.dependencies:
            for dependency_step_name in self.dependencies:
                dependency_step = self.pipeline_flow.get_step(name=dependency_step_name)
                if dependency_step.status not in ProgressStatus.SUCCESS_OR_SKIPPED_STATUSES:
                    self.status = ProgressStatus.BLOCKED_BY_UNRESOLVED_DEPENDENCY
                    return False
        self.status = set_status
        return True

    def nb_tasks(self) -> int:
        """Get the total number of tasks in the group."""
        return self.iteration_template.nb_tasks * self.total_iterations



    #TODO add step statuses across iterations
    # def __str__(self):
    #     group_status = f"[Status: {self.status.value}; Total_Iterations: {self.total_iterations}]:: Group: {self.name}"
    #     iteration_template_str = str(self.iteration_template)
    #     return f"{group_status}\n{iteration_template_str}"
    

    def __str__(self):
        indent=0
        header = f"{' ' * indent}**  {self.name} [Status: {self.status.name}]"
        if self.iterations:
            if not self.status_counts:
                self.update_status_counts_and_overall_status(final=False)

            iteration_info = (f"Total Iterations: {self.total_iterations}, Total_Statuses: {self.status_counts['total_statuses']}, "
                                + ", ".join(f"{status}: {count}" for status, count in self.status_counts['detailed'].items() if count > 0))
            header += f" [{iteration_info}]"
        else:
            header += " [No iterations yet]"

        # Template tasks with their aggregated statuses
        template_flow = []
        for step_name in self.iteration_template.steps:
            if self.iterations:
                step_status_counts = self.get_status_counts_for_step_across_iterations(step_name=step_name)
                step_info =  (f"[Total Iterations: {self.total_iterations}, "
                                + ", ".join(f"{status}: {count}" for status, count in step_status_counts.items() if count > 0))
                template_flow.append(
                    f"{' ' * (indent + 2)}>> {step_name} {step_info}"
                )
            else:
                template_flow.append(
                    f"{' ' * (indent + 2)}>> {step_name} [No iterations yet]"
                )
        return f"{header}\n{chr(10).join(template_flow)}" if template_flow else header




class PipelineFlow:
    """
    Enhanced Pipeline configuration utility with unique name enforcement.
    """

    def __init__(self, base_context_name:str, disabled: bool = True):
        self.steps: Dict[str, Union['PipelineTask', 'PipelineDynamicGroupOfIterations']] = {}
        self.base_context=base_context_name
        self._status = ProgressStatus.NOT_STARTED if not disabled else ProgressStatus.DISABLED
        self.status_counts = None


    def add_step(self, step: Union['PipelineTask', 'PipelineDynamicGroupOfIterations']):
        """
        Add a step which is a PipelineTask or PipelineLoopGroup to the pipeline.
        :param task_or_group: Single PipelineTask or PipelineLoopGroup.
        """
        if not step.disabled:
            if step.name in self.steps:
                raise ValueError(f"Step (Task, Group etc) with name '{step.name}' already exists in the pipeline.")
            self.steps[step.name] = step
            step.set_pipeline_flow(self)  # Associate the step with this pipeline flow

    def get_step(self, name: str, sequence_ref: Optional[Union[int, str]] = None) -> Union['PipelineTask', 'PipelineDynamicGroupOfIterations']:
        """
        Retrieve a task or group by name, searching recursively through all groups.
        :param name: Name of the task or group to retrieve.
        :return: Task or group with the given name.
        :raises KeyError: If no task or group exists with the given name.
        """
        # First, check top-level steps
        if name in self.steps:
            return self.steps[name]

        # Then, recursively check inside groups
        for step in self.steps.values():
            if isinstance(step, PipelineDynamicGroupOfIterations):
                if sequence_ref is not None:
                    if sequence_ref in step.iterations:
                        iteration = step.iterations[sequence_ref]
                        if name in iteration.steps:
                            return iteration.steps[name]
                else:
                    # If not found in iterations, check template
                    if name in step.iteration_template.steps:
                        return step.iteration_template.steps[name]
                    

        raise KeyError(
            f"Step '{name}' not found in pipeline flow. And not found in a specified iteration or template."
        )
    
    
    def get_dependent_step(self,step: Union['PipelineTask', 'PipelineDynamicGroupOfIterations'],
                           sequence_ref: Optional[Union[int, str]] = None) -> List[Union['PipelineTask', 'PipelineDynamicGroupOfIterations']]:   
        """
        Get all dependencies for a step, optionally from a specific iteration.
        
        Args:
            task: Task to get dependencies for
            iteration_ref: Optional reference to specific iteration
        """
        return [
            self.get_step(name=dep, sequence_ref=sequence_ref)
            for dep in step.dependencies
        ]

    def validate_dependencies(self) -> bool:
        """
        Recursively validate that all dependency steps exist for all steps in the pipeline.
        Checks dependencies at all nesting levels of PipelineDynamicGroupOfIterations.
        """
        def _validate_step_dependencies(step: Union['PipelineTask', 'PipelineDynamicGroupOfIterations'], 
                                    context: str = '') -> None:
            """
            Recursively validate dependencies for a step and its nested components.
            
            Args:
                step: The step to validate
                context: String describing the current validation context/path
            """
            # Validate direct dependencies of the step
            for dep in step.dependencies:
                try:
                    self.get_step(dep)
                except KeyError as exc:
                    raise ValueError(
                        f"Dependency '{dep}' for step '{step.name}' not found in pipeline. "
                        f"Context: {context}"
                    )  from exc

            # If step is a dynamic group, validate its template and iterations
            if isinstance(step, PipelineDynamicGroupOfIterations):
                # Validate template steps
                for template_step in step.iteration_template.steps.values():
                    _validate_step_dependencies(
                        template_step,
                        f"{context} -> {step.name}(template)"
                    )

        # Start validation from top-level steps
        for step in self.steps.values():
            _validate_step_dependencies(step, "root")

        return True
    

        
    def get_pipeline_flow_str(self) -> str:
        """
        Generate a string representation of the pipeline flow, including task statistics across iterations.
        """

        return "\n".join(str(step) for step in self.steps.values() if not step.disabled).strip() + "\n"


    def get_pipeline_description(self) -> str:
        """
        Generate the complete pipeline description with base context and pipeline flow.
        :return: String representing the pipeline description.
        """
        return f"{self.base_context}\nflow:\n{self.get_pipeline_flow_str()}"
    



# def get_pipeline_flow(self) -> str:
#         """
#         Generate a string representation of the pipeline flow, including task statistics across iterations.
#         """
#         def _generate_flow(step, indent=0):
#             if isinstance(step, PipelineTask):
#                 return f"{' ' * indent} >> [Status: {step.status.value}] {step.name}"
#             elif isinstance(step, PipelineDynamicGroupOfIterations):
#                 # Group header with iteration counts
#                 header = f"{' ' * indent}** [Status: {step.status.value}] {step.name}"
#                 if step.iterations:
#                     iter_statuses = step.get_total_statuses_by_category()
#                     iteration_info = (f"Total Iterations: {len(step.iterations)}, "
#                                     f"Completed: {iter_statuses['completed']}, "
#                                     f"Failed: {iter_statuses['failed']}, "
#                                     f"Pending: {iter_statuses['pending']}")
#                     header += f" [{iteration_info}]"
#                 else:
#                     header += " [No iterations yet]"

#                 # Template tasks with their aggregated statuses
#                 template_flow = []
#                 for task_name in step.iteration_template.steps:
#                     if step.iterations:
#                         task_statuses = step.get_status_counts_for_step_across_iterations(task_name)
#                         task_info = (f"[Total: {sum(task_statuses.values())}, "
#                                 f"Completed: {task_statuses['completed']}, "
#                                 f"Failed: {task_statuses['failed']}, "
#                                 f"Pending: {task_statuses['pending']}]")
#                         template_flow.append(
#                             f"{' ' * (indent + 2)}>> {task_name} {task_info}"
#                         )
#                     else:
#                         template_flow.append(
#                             f"{' ' * (indent + 2)}>> {task_name}"
#                         )

#                 return f"{header}\n{chr(10).join(template_flow)}" if template_flow else header

#         return "\n".join(
#             _generate_flow(step) for step in self.steps.values() if not step.disabled
#         ).strip() + "\n"
