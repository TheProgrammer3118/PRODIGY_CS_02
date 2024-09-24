from PIL import Image
import os

def validate_key(key):
    """Ensure the key is an integer and within the acceptable range."""
    if not isinstance(key, int):
        raise ValueError("Key must be an integer.")
    return key % 256

def encrypt_image(input_image_path, output_image_path, key):
    """Encrypt the image using XOR encryption."""
    image = Image.open(input_image_path)
    pixels = image.load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            encrypted_pixel = (r ^ key, g ^ key, b ^ key)
            pixels[i, j] = encrypted_pixel

    image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    """Decrypt the image using XOR decryption."""
    image = Image.open(input_image_path)
    pixels = image.load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            decrypted_pixel = (r ^ key, g ^ key, b ^ key)
            pixels[i, j] = decrypted_pixel

    image.save(output_image_path)

def get_user_input(prompt, input_type=str, valid_range=None):
    """Generic function to get and validate user input."""
    while True:
        user_input = input(prompt).strip()
        try:
            value = input_type(user_input)
            if valid_range and value not in valid_range:
                print(f"Input must be within {valid_range}. Please try again.")
                continue
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def main():
    while True:
        print("\nImage Encryption Tool")
        print("Type '1' to encrypt an image")
        print("Type '2' to decrypt an image")
        print("Type '3' to exit")
        
        mode = get_user_input("Please select an option: ", int, [1, 2, 3])

        if mode == 3:
            print("Exiting the tool. Goodbye!")
            break

        input_image_path = get_user_input("Enter the path to the input image: ")
        output_image_path = get_user_input("Enter the path to save the output image (with a valid image extension): ")

        if not os.path.isfile(input_image_path):
            print("Input file does not exist.")
            continue

        while True:
            try:
                key = int(input("Enter the encryption key (integer): "))
                break
            except ValueError:
                print("Invalid key value. Please enter an integer.")
        
        if mode == 1:
            encrypt_image(input_image_path, output_image_path, validate_key(key))
            print(f"Image encrypted and saved to {output_image_path}")
        elif mode == 2:
            decrypt_image(input_image_path, output_image_path, validate_key(key))
            print(f"Image decrypted and saved to {output_image_path}")

if __name__ == "__main__":
    main()
