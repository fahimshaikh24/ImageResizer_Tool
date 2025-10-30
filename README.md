# 🖼️ Image Resizer Tool

A simple batch **Image Resizer and Converter** built in **Python** using **Pillow (PIL)**.  
It automatically resizes all images in a folder and saves them to an output folder.


## ⚙️ How to Run :
1. Make sure Python is installed.  
    Check with:  
    python --version
2. Install the required library:
    pip install pillow
3. Open CMD or VS Code Terminal.
4. Go to the folder where image_resizer.py is saved:
    cd path/to/your/project
5. Create a folder named images_input and place your images inside it.
    Run the script:
    python image_resizer.py
    The resized images will be saved in the images_output folder.

## 🧾 Example Output
Before → After resizing (400x400)
When the script is run, all images inside the **images_input** folder are resized to the given dimensions (e.g., 400×400) and saved in **images_output**.

**🔗 Input Image:** [View Input Image](animals_input.jpg)  
**🔗 Output Image:** [View Output Image](animals_output.jpg)

<table>
<tr>
<td><img src="animals_input.jpg" width="300"></td>
<td><img src="animals_output.jpg" width="300"></td>
</tr>
<tr>
<td align="center">🌿 Original Image</td>
<td align="center">🖼️ Resized Image (400×400)</td>
</tr>
</table>


## 📋 Features
- Resize all images in a folder automatically
- Convert images to JPG format
- Works with multiple formats (.png, .jpg, .jpeg, .bmp, .gif)
- Creates output folder automatically
- Simple and beginner-friendly

## 🧠 Tools Used
- Python
- Pillow (PIL)
- OS module

## 👨‍💻 Author
Fahim Shaikh

SY BTECH in Computer Science & Engineering
