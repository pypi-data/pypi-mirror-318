import unittest
from datetime import datetime, timezone
import time
from typing import Dict, Any
from ipulse_shared_base_ftredge import ProgressStatus, evaluate_combined_progress_status
from ipulse_shared_data_eng_ftredge import OpResult

class TestOpResult(unittest.TestCase):
    def setUp(self):
        self.op_result = OpResult()

    def test_initialization(self):
        """Test default initialization"""
        self.assertIsNotNone(self.op_result.operation_id)
        self.assertEqual(self.op_result.overall_status, ProgressStatus.IN_PROGRESS)
        self.assertEqual(self.op_result.total_operations, 1)
        self.assertIsNone(self.op_result.data)
        self.assertEqual(len(self.op_result.execution_state), 0)
        self.assertIsNotNone(self.op_result.start_time)
        self.assertEqual(self.op_result.duration_s, 0.0)

    def test_data_management(self):
        """Test data property and methods"""
        # Test simple data assignment
        test_data = {"key": "value"}
        self.op_result.data = test_data
        self.assertEqual(self.op_result.data, test_data)

        # Test add_data method
        self.op_result.data = {}  # Start with empty dict
        self.op_result.add_data(values=["item1", "item2"], name="list_data")
        self.assertEqual(self.op_result.data["list_data"], ["item1", "item2"])

        # Test add_data with invalid initial data type
        self.op_result.data = "string"
        with self.assertRaises(ValueError):
            self.op_result.add_data(values=[1,2,3], name="numbers")

    def test_status_management(self):
        """Test status handling and transitions"""
        # Test direct status assignment
        self.op_result.overall_status = ProgressStatus.DONE
        self.assertEqual(self.op_result.overall_status, ProgressStatus.DONE)

        # Test string status assignment
        self.op_result.overall_status = "FAILED"
        self.assertEqual(self.op_result.overall_status, ProgressStatus.FAILED)

        self.op_result.overall_status = "FAIL"
        self.assertEqual(self.op_result.overall_status, ProgressStatus.UNKNOWN)

        # Test final() method with different scenarios
        # 1. Final with issues
        self.op_result = OpResult()
        self.op_result.add_issue("Test issue")
        self.op_result.final()
        self.assertEqual(self.op_result.overall_status, ProgressStatus.FINISHED_WITH_ISSUES)

        # 2. Final with warnings
        self.op_result = OpResult()
        self.op_result.add_warning("Test warning")
        self.op_result.final()
        self.assertEqual(self.op_result.overall_status, ProgressStatus.DONE_WITH_WARNINGS)

        # 3. Final with notices
        self.op_result = OpResult()
        self.op_result.add_notice("Test notice")
        self.op_result.final()
        self.assertEqual(self.op_result.overall_status, ProgressStatus.DONE_WITH_NOTICES)

        # 4. Clean completion
        self.op_result = OpResult()
        self.op_result.final()
        self.assertEqual(self.op_result.overall_status, ProgressStatus.DONE)

        self.op_result = OpResult()
        self.op_result.add_issue("Test issue")
        self.op_result.final(ProgressStatus.DONE)
        self.assertEqual(self.op_result.overall_status, ProgressStatus.DONE)

    def test_execution_state_tracking(self):
        """Test execution state management"""
        self.op_result.add_state("Started operation")
        self.op_result.add_state("Processing")
        self.op_result.add_state("Completed")

        # Check state entries
        self.assertEqual(len(self.op_result.execution_state), 3)
        
        # Verify timestamp format in state entries
        for state in self.op_result.execution_state:
            self.assertRegex(state, r"\[t:.*\]--.*")

        # Check string representation
        state_str = self.op_result.execution_state_str
        self.assertIn("Started operation", state_str)
        self.assertIn("Processing", state_str)
        self.assertIn("Completed", state_str)

    def test_issues_warnings_notices(self):
        """Test adding and retrieving issues, warnings, and notices"""
        # Test issues
        self.op_result.add_issue("Critical error")
        self.op_result.add_issue("Data corruption")
        self.assertEqual(len(self.op_result.issues), 2)
        self.assertIn("Critical error", self.op_result.issues_str)

        # Test warnings
        self.op_result.add_warning("Performance degradation")
        self.assertEqual(len(self.op_result.warnings), 1)
        self.assertIn("Performance degradation", self.op_result.warnings_str)

        # Test notices
        self.op_result.add_notice("Process completed")
        self.assertEqual(len(self.op_result.notices), 1)
        self.assertIn("Process completed", self.op_result.notices_str)

        # Test combined notes
        notes = self.op_result.get_notes
        self.assertIn("ISSUES", notes)
        self.assertIn("WARNINGS", notes)
        self.assertIn("NOTICES", notes)

    def test_metadata_management(self):
        """Test metadata handling"""
        # Test direct assignment
        test_metadata = {"source": "test", "version": "1.0"}
        self.op_result.metadata = test_metadata
        self.assertEqual(self.op_result.metadata, test_metadata)

        # Test add_metadata method
        self.op_result.add_metadata(new_field="value", another_field=123)
        self.assertEqual(self.op_result.metadata["new_field"], "value")
        self.assertEqual(self.op_result.metadata["another_field"], 123)

    def test_timing_operations(self):
        """Test timing-related functionality"""
        # Test start time
        self.assertIsNotNone(self.op_result.start_time)
        
        # Test elapsed time
        time.sleep(0.1)  # Small delay
        elapsed = self.op_result.elapsed_time
        self.assertGreater(elapsed, 0)

        self.op_result.final()
        self.assertIsNotNone(self.op_result.duration_s)
        self.assertGreater(self.op_result.duration_s, 0)


    def test_operation_counting(self):
        """Test operation counting functionality"""
        self.assertEqual(self.op_result.total_operations, 1)
        
        # Test increment
        self.op_result.increment_total_operations(2)
        self.assertEqual(self.op_result.total_operations, 3)

        # Test direct setting
        self.op_result.total_operations = 5
        self.assertEqual(self.op_result.total_operations, 5)

    def test_normal_result_integration(self):
        """Test integrating child operation results"""
        # Create child result
        child_result = OpResult()
        child_result.add_warning("Child warning")
        child_result.add_issue("Child issue")
        child_result.add_notice("Child notice")
        child_result.add_metadata(child_specific_meta="value")
        child_result.data = {"child_data": "value"}
        child_result.final(status=ProgressStatus.DONE_WITH_WARNINGS)

        # Test integration with default settings (skip_data=True, skip_metadata=True)
        self.op_result.integrate_result(child_result=child_result,combine_status=True)
        self.assertEqual(len(self.op_result.warnings), 1)
        self.assertEqual(len(self.op_result.issues), 1)
        self.assertEqual(len(self.op_result.notices), 1)
        self.assertIsNone(self.op_result.data)  # Data should be skipped
        self.assertEqual(len(self.op_result.metadata), 0)  # Metadata should be skipped

        # Test integration with data and metadata
        self.op_result = OpResult()  # Fresh instance
        self.op_result.integrate_result(child_result, skip_data=False, skip_metadata=False)
        self.assertEqual(self.op_result.data, {"child_data": "value"})
        self.assertEqual(self.op_result.metadata["child_specific_meta"], "value")

    def test_not_combined_status_integration(self):
            # Test status combination in Combine not Forced and child didn't have issues
            child_result = OpResult()
            child_result.final(status=ProgressStatus.FAILED)
            self.op_result.integrate_result(child_result, combine_status=False)
            self.assertEqual(self.op_result.overall_status, ProgressStatus.IN_PROGRESS)
            self.op_result.final()
            self.assertEqual(self.op_result.overall_status, ProgressStatus.DONE)

    def test_not_combined_status_integration_with_issues(self):
            # Test status combination in Combine not Forced and child had issues
            child_result = OpResult()
            child_result.add_issue("Child issue 3")
            child_result.final(status=ProgressStatus.FAILED)
            self.op_result.integrate_result(child_result, combine_status=False)
            self.assertEqual(self.op_result.overall_status, ProgressStatus.IN_PROGRESS)
            self.op_result.final()
            self.assertEqual(self.op_result.overall_status, ProgressStatus.FINISHED_WITH_ISSUES)


    def test_status_aggregation(self):
        """Test status aggregation logic"""
        # Test priority ordering
        status_pairs = [
            (ProgressStatus.DONE, ProgressStatus.FAILED),  # FAILED should win
            (ProgressStatus.DONE_WITH_NOTICES, ProgressStatus.DONE_WITH_WARNINGS),  # WARNINGS should win
            (ProgressStatus.IN_PROGRESS, ProgressStatus.DONE),  # IN_PROGRESS should win
            (ProgressStatus.CANCELLED, ProgressStatus.FAILED),  # FAILED should win
        ]

        for status1, status2 in status_pairs:
            result = evaluate_combined_progress_status([status1, status2])
            self.assertEqual(result, max(status1, status2, key=lambda x: x.value))

    def test_serialization(self):
        """Test dictionary and string serialization"""
        # Prepare a result with various data
        self.op_result.add_state("Started")
        self.op_result.add_warning("Test warning")
        self.op_result.add_metadata(test_key="test_value")
        self.op_result.data = {"test": "data"}

        # Test to_dict()
        result_dict = self.op_result.to_dict()
        self.assertIn("data", result_dict)
        self.assertIn("status", result_dict)
        self.assertIn("overall_status", result_dict["status"])
        self.assertIn("execution_state", result_dict["status"])

        # Test str representation
        result_str = str(self.op_result)
        self.assertIn("overall_status", result_str)
        self.assertIn("operation_id", result_str)

        # Test info property
        info = self.op_result.info
        self.assertIsInstance(info, str)
        self.assertIn("test_key", info)

if __name__ == '__main__':
    unittest.main()