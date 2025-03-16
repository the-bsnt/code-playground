from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()
imagelist = []  

# EDIT BELOW USER INPUTS for desired outputs

folder = "images"  # Folder containing all the images.
name = "pdf_ready.pdf"  # Name of the output PDF file.

for dirpath, dirnames, filenames in os.walk(folder):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        full_path = os.path.join(dirpath, filename)
        imagelist.append(full_path)

imagelist.sort()
for i in range(0, len(imagelist)):
    print(imagelist[i])

for i in range(0, len(imagelist)):
    im1 = Image.open(imagelist[i]) 
    width, height = im1.size 
    if width > height:
        im2 = im1.transpose(Image.ROTATE_270)  
        os.remove(imagelist[i]) 
        im2.save(imagelist[i])  
        
print("\nFound " + str(len(imagelist)) + " image files. Converting to PDF....\n")

for image in imagelist:
    pdf.add_page()
    pdf.image(
        image, 0, 0, 210, 297
    )  
    # 210 and 297 are the dimensions of an A4 size sheet.

pdf.output(folder + name, "F")  # Save the PDF.

print("PDF generated successfully!")
