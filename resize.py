from PIL import Image
import os

def resize_images(folder_path, max_size=512):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate over each file in the folder
    for file_name in file_list:
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is an image
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            try:
                # Open the image file using Pillow
                image = Image.open(file_path)
                if image.format != 'PNG':
                    file_path = os.path.splitext(file_path)[0] + '.png'
                    image.save(file_path, 'PNG')
                    image = Image.open(file_path)
                # Calculate the new width and height while maintaining the aspect ratio
                width, height = image.size
                if width > height:
                    new_width = max_size
                    new_height = int(height * (new_width / width))
                else:
                    new_height = max_size
                    new_width = int(width * (new_height / height))

                # Resize the image
                resized_image = image.resize((new_width, new_height))

                # Save the resized image, overwriting the original file
                resized_image.save(file_path)
                print(f"Resized {file_name} successfully.")
            except Exception as e:
                print(f"Failed to resize {file_name}: {str(e)}")
        else:
            print(f"Ignored {file_name} as it is not an image.")


folder_path = ''  # Replace with the actual folder path
resize_images(folder_path)
