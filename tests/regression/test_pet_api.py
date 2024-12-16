from .pet_api_client import PetApiClient
from unittest.mock import patch
import json
import requests
import unittest

class TestPetApiClient(unittest.TestCase):
    def setUp(self):
        self.client = PetApiClient()
        self.pet_data = {
            "id": 123,
            "category": {"id": 1, "name": "Dog"},
            "name": "Bobby Updated",
            "photoUrls": ["http://example.com/dog_updated.jpg"],
            "tags": [{"id": 1, "name": "Friendly"}],
            "status": "sold"
        }

    @patch('requests.post')
    def test_create_pet(self, mock_post):
        """
        Test creating a new pet.
        """
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Pet created successfully", "code": 200}

        # Test creating a new pet
        response = self.client.create_pet(self.pet_data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Pet created successfully", "code": 200})

    @patch('requests.put')
    def test_update_pet(self, mock_put):
        """
        Test updating an existing pet.
        """
        mock_response = mock_put.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Pet updated successfully", "code": 200}

        # Test updating an existing pet
        response = self.client.update_pet(self.pet_data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Pet updated successfully", "code": 200})

    @patch('requests.get')
    def test_get_pet_by_id(self, mock_get):
        """
        Test retrieving a pet by its ID.
        """
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = self.pet_data

        # Test getting pet details by ID
        response = self.client.get_pet_by_id(self.pet_data['id'])

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.pet_data)

    @patch('requests.delete')
    def test_delete_pet(self, mock_delete):
        """
        Test deleting a pet.
        """
        mock_response = mock_delete.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Pet deleted successfully", "code": 200}

        # Test deleting the pet
        response = self.client.delete_pet(self.pet_data['id'])

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Pet deleted successfully", "code": 200})

    @patch('requests.get')
    def test_get_pets_by_status_no_valid_status(self, mock_get):
        """Test that get_pets_by_status raises an error when no valid statuses are provided."""
        
        with self.assertRaises(ValueError):
            self.client.get_pets_by_status(['unknown_status'])

    @patch('requests.get')
    def test_get_pets_by_status_api_error(self, mock_get):
        """Test that get_pets_by_status raises an HTTPError when the API returns a non-200 status code."""
        
        # Simulate a 500 Internal Server Error response
        mock_get.return_value.status_code = 500
        mock_get.return_value.text = 'Internal Server Error'
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("Internal Server Error")

        # Now, we expect an HTTPError to be raised due to the non-2xx status code
        with self.assertRaises(requests.exceptions.HTTPError):
            self.client.get_pets_by_status('available')

    @patch('requests.get')
    def test_get_pets_by_status_empty_response(self, mock_get):
        """Test that get_pets_by_status handles an empty response."""
        
        # Define an empty response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'pets': []}

        pets = self.client.get_pets_by_status('available')

        # Assert that the response contains no pets
        self.assertEqual(len(pets['pets']), 0)

    @patch('requests.post')
    def test_upload_image(self, mock_post):
        """
        Test uploading an image for a pet.
        """
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Image uploaded successfully", "code": 200}

        # Simulate the file upload
        with open('dummy_image.jpg', 'w') as f:
            f.write("dummy image content")  # Create a dummy file for testing

        # Test image upload
        with open('dummy_image.jpg', 'rb') as file:
            response = self.client.upload_image(self.pet_data['id'], file)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Image uploaded successfully", "code": 200})

    @patch('requests.post')
    def test_update_pet_by_id(self, mock_post):
        """
        Test updating a pet using POST with pet_id as part of the URL.
        """
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Pet updated successfully", "code": 200}

        # Test updating the pet by pet_id
        response = self.client.update_pet_by_id(self.pet_data['id'], self.pet_data)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Pet updated successfully", "code": 200})


if __name__ == "__main__":
    unittest.main()