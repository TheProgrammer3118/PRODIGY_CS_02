# ✈️ Image Encryption Tool

Welcome to the **Image Encryption Tool**! This Python script allows you to easily encrypt and decrypt images using simple XOR encryption. With a user-friendly command-line interface, you can secure your images with a custom key. 🛡️

## 🔧 Features

- **Encrypt Images**: Secure your images with a user-defined integer key.
- **Decrypt Images**: Restore your encrypted images using the same key.
- **User-Friendly Interface**: Easy-to-follow prompts for quick use.
- **Supports Common Formats**: Works with popular image formats like PNG and JPG.

## 📋 Requirements

To get started, ensure you have Python 3.x and the Pillow library installed. You can install Pillow using the command `pip install Pillow`.

## 🚀 Usage

To begin, clone or download the repository from GitHub. Navigate to the project directory, and run the script using `python image_encryption_tool.py`. 

Once the script is running, follow the prompts: type `1` to encrypt an image, `2` to decrypt an image, or `3` to exit the program. When prompted, enter the path to the input image, specify the path to save the output image (be sure to use a valid image extension), and provide an integer key for the encryption or decryption process.

### Example Interaction

When you run the tool, you’ll see options like “Type '1' to encrypt an image” and so on. After selecting your desired action, you’ll be asked to enter the necessary file paths and key.

## 📖 How It Works

The script begins by loading the input image using the Pillow library. It then processes each pixel's RGB values using the XOR operation with the provided key. Finally, the encrypted or decrypted image is saved to the specified output path.

## ⚠️ Notes

Make sure that the input image path is valid before running the script. The encryption key should be an integer within a reasonable range (0-255). Always use valid image file extensions when specifying output paths.


## 👤 Author

[Dharmpreet Singh]
