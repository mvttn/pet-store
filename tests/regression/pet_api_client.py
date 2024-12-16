import requests

class PetApiClient:
    BASE_URL = "petstore.swagger.io/v2"

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def upload_image(self, pet_id, image_file, additional_metadata=None):
        """
        POST an image for a pet.
        :param pet_id: ID of the pet.
        :param image_file: Image file to be uploaded.
        :param additional_metadata: Optional additional metadata to pass with the image.
        :return: Response object from the upload request.
        """
        url = f"{self.BASE_URL}/pet/{pet_id}/uploadImage"
        files = {'file': image_file}
        data = {}
        if additional_metadata:
            data['additionalMetadata'] = additional_metadata
        
        response = requests.post(url, files=files, data=data, headers=self.headers)
        return response
  
    def create_pet(self, pet_data):
        """
        Sends a POST request to create a new pet.
        :param pet_data: Dictionary containing pet details.
        :return: Response object from the POST request.
        """
        url = f"{self.BASE_URL}/pet"
        response = requests.post(url, json=pet_data, headers=self.headers)
        return response

    def update_pet(self, pet_data):
        """
        Sends a PUT request to update an existing pet.
        :param pet_data: Dictionary containing pet details.
        :return: Response object from the PUT request.
        """
        url = f"{self.BASE_URL}/pet"
        response = requests.put(url, json=pet_data, headers=self.headers)
        return response

    def get_pets_by_status(self, status_value):
        """
        Fetch pets by status value.
        Valid statuses: 'available', 'pending', 'sold'
        
        :param: status_value: Status to filter by.
        :return: JSON response containing pets with the given statuses.
        """
        # Validate the input status list
        valid_statuses = ["available", "pending", "sold"]
        if status_value not in valid_statuses:
            raise ValueError("No valid statuses provided. Valid statuses are: 'available', 'pending', 'sold'.")

        # Construct the endpoint URL
        url = f"{self.BASE_URL}/pet/findByStatus"
        
        # Sending GET request with the list of valid statuses
        response = requests.get(url, params={'status': status_value})

        response.raise_for_status()
        
        return response.json()  # Return the list of pets in JSON format


    def get_pet_by_id(self, pet_id):
        """
        Sends a GET request to fetch a pet by ID.
        :param pet_id: ID of the pet to retrieve.
        :return: Response object from the GET request.
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_pet_by_id(self, pet_id, pet_data):
        """
        Update an existing pet using POST with pet_id as part of the URL.
        :param pet_id: ID of the pet to update.
        :param pet_data: Data to update the pet with.
        :return: Response object from the update request.
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        response = requests.post(url, json=pet_data, headers=self.headers)
        return response

    def delete_pet(self, pet_id, api_key=None):
        """
        Sends a DELETE request to remove a pet by ID.
        :param pet_id: ID of the pet to delete.
        :param api_key: Optional API key for authentication.
        :return: Response object from the DELETE request.
        """
        url = f"{self.BASE_URL}/pet/{pet_id}"
        headers = self.headers
        if api_key:
            headers['api_key'] = api_key
        response = requests.delete(url, headers=headers)
        return response