from setuptools import setup, find_packages

# Membaca isi README.md
long_description = ""
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="get_attachment_image",
    version="0.1.10",
    packages=find_packages(),
    install_requires=[
        # Daftar dependencies yang diperlukan, misalnya odoo jika diperlukan
    ],
    description="Paket untuk mendapatkan attachment gambar di Odoo",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Jika menggunakan Markdown
    author="Fasriyah Julia Alam",
    author_email="fasriyahjuliaalam@gmail.com",
    url="https://github.com/FJ-Alam/python_project.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
