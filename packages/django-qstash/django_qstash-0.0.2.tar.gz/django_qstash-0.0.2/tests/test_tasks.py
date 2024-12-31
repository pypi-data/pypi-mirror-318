from unittest.mock import Mock, patch

import pytest

from django_qstash.tasks import shared_task


@shared_task
def sample_task(x, y):
    return x + y


@shared_task(name="custom_task", deduplicated=True)
def sample_task_with_options(x, y):
    return x * y


@pytest.mark.django_db
class TestQStashTasks:
    def test_basic_task_execution(self):
        """Test that tasks can be executed directly"""
        result = sample_task(2, 3)
        assert result == 5

    def test_task_with_options(self):
        """Test that tasks with custom options work"""
        result = sample_task_with_options(4, 5)
        assert result == 20

    @patch("django_qstash.tasks.qstash_client")
    def test_task_delay(self, mock_client):
        """Test that delay() sends task to QStash"""
        mock_response = Mock()
        mock_response.message_id = "test-id-123"
        mock_client.message.publish_json.return_value = mock_response

        result = sample_task.delay(2, 3)

        assert result.task_id == "test-id-123"
        mock_client.message.publish_json.assert_called_once()

    @patch("django_qstash.tasks.qstash_client")
    def test_task_apply_async(self, mock_client):
        """Test that apply_async() works with countdown"""
        mock_response = Mock()
        mock_response.message_id = "test-id-456"
        mock_client.message.publish_json.return_value = mock_response

        result = sample_task.apply_async(args=(2, 3), countdown=60)

        assert result.task_id == "test-id-456"
        call_kwargs = mock_client.message.publish_json.call_args[1]
        assert call_kwargs["delay"] == "60s"
