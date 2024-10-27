

def insert_text(input_pdf, output_pdf, text, page_number, x, y):
    import PyPDF2

    with open(input_pdf, 'rb') as input_file, open (output_pdf, 'wb') as output_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        for i in range(len(reader.pages)):
            page = reader.pages[i]
            if i == page_number:
                annotation = PyPDF2.generic.AnnotationBuilder.free_text(
                    text=text,
                    x=x,
                    y=y,
                    # width=0,
                    # height=0,
                    font_name="Helvetica",
                    font_size=50,
                    # font_color=PyPDF2.generic.RgbColor(0, 0, 0),
                    # font_family=None,
                    # font_file=None,
                )
                print(annotation.text)
                page.add_annot(annotation)
            writer.add_page(page)

        writer.write(output_file)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Add text to a PDF file')
    parser.add_argument('input_pdf', type=str, help='The input PDF file')
    parser.add_argument('output_pdf', type=str, help='The output PDF file')
    parser.add_argument('text', type=str, help='The text to add')
    parser.add_argument('page_number', type=int, help='The page number to add the text')
    parser.add_argument('x', type=float, help='The x coordinate of the text')
    parser.add_argument('y', type=float, help='The y coordinate of the text')
    args = parser.parse_args()

insert_text(args.input_pdf, args.output_pdf, args.text, args.page_number, args.x, args.y)   