# Python tool for extracting average altitude above ground (m) from EXIFs in directory
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

def get_altitude(image_path):
    try:
        output = subprocess.check_output(["exiftool", "-RelativeAltitude", "-s3", image_path], universal_newlines=True)
        altitude = float(output.strip())
        return altitude
    except subprocess.CalledProcessError as e:
        print(f"Error processing image: {image_path}")
        print(f"Error message: {str(e)}")
    except ValueError as e:
        print(f"Error converting altitude value: {str(e)}")
    return None

def process_images(directory):
    image_files = [
        os.path.join(directory, filename)
        for filename in os.listdir(directory)
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".tiff"))
    ]

    with ThreadPoolExecutor() as executor:
        altitudes = list(executor.map(get_altitude, image_files))

    altitudes = [alt for alt in altitudes if alt is not None]

    if len(altitudes) > 0:
        average_altitude = sum(altitudes) / len(altitudes)
        return average_altitude
    else:
        return None

# Prompt the user to enter the directory path
directory = input("Enter the directory path containing the images: ")

# Check if the directory exists
if not os.path.isdir(directory):
    print("Invalid directory path. Please provide a valid directory.")
    exit(1)

average_altitude = process_images(directory)

if average_altitude is not None:
    print(f"Average relative altitude above ground: {average_altitude:.2f} meters")
else:
    print("No valid relative altitude data found in the images.")
