from PIL import Image, ImageFilter

def apply_edge_detection(input_path, output_path):
    try:
        # Open the input image
        image = Image.open(input_path)

        # Apply edge detection filter
        edges_image = image.filter(ImageFilter.FIND_EDGES)

        # Save the edge-detected image
        edges_image.save(output_path)
        print("Edge detection complete. Edge-detected image saved as", output_path)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    input_image_path ="C:/Users/Nicy Joseph/Downloads/WhatsApp Image 2023-08-31 at 8.35.57 PM.jpeg"
    output_image_path ="C:/Users/Nicy Joseph/Desktop/dt/appa.jpeg"
    apply_edge_detection(input_image_path, output_image_path)

