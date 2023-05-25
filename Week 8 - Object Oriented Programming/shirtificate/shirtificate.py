# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# CS50 Shirtificate

# Generate a shirtificate

from fpdf import FPDF


def main():

    # Get name from user
    name = input("Name: ")

    # PDF's meta-data
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    # Source image
    pdf.image('shirtificate.png', 8, 50, 190)

    # Title
    pdf.set_font('helvetica', 'B', size=40)
    pdf.text(50, 30, txt='CS50 Shirtificate')

    # Shirt's text
    pdf.set_font('helvetica', 'B', size=20)
    pdf.set_text_color(255)
    pdf.cell(190, 200, txt=f'{name} took CS50', align='C')

    # Output file
    pdf.output('shirtificate.pdf')


if __name__ == '__main__':
    main()