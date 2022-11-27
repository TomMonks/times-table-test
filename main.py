import random
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors


def create_pdf_questions(num1, num2, file_name='tt_quiz.pdf'):

    document_title = "Monks' Family Times Table Quiz"
    title = "Monks' Family Times Table Quiz"

    number = [i+1 for i in range(len(num1))]
    text_lines =[f'{q}: {a} X {b} = ' for q, a, b in zip(number, num1, num2)] 
   
    pdf = canvas.Canvas(file_name)
  
    # setting the title of the document
    pdf.setTitle(document_title)


    # creating the title by setting it's font
    # and putting it on the canvas
    pdf.setFont('Courier-Bold', 24)
    pdf.drawCentredString(300, 770, title)

    # creating the subtitle by setting it's font,
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    
    # drawing a line
    pdf.line(30, 710, 550, 710)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)

    for line in text_lines:
        text.textLine(line)
        
    pdf.drawText(text)

    # saving the pdf
    pdf.save()


def create_pdf_answers(answers, file_name='tt_quiz_solutions.pdf'):

    document_title = "Answers"
    title = "Answers"

    number = [i+1 for i in range(len(answers))]
    text_lines =[f'{i}: {a}' for i, a in zip(number, answers)] 
   
    pdf = canvas.Canvas(file_name)
  
    # setting the title of the document
    pdf.setTitle(document_title)


    # creating the title by setting it's font
    # and putting it on the canvas
    pdf.setFont('Courier-Bold', 24)
    pdf.drawCentredString(300, 770, title)

    # creating the subtitle by setting it's font,
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    
    # drawing a line
    pdf.line(30, 710, 550, 710)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)

    for line in text_lines:
        text.textLine(line)
        
    pdf.drawText(text)

    # saving the pdf
    pdf.save()




def print_questions(num1, num2):
    number = [i+1 for i in range(len(num1))]
    for q, a, b in zip(number, num1, num2):
        print(f'{q}: {a} X {b} = ')

def print_answers(answers):
    for i in range (len(answers)):
        print(f'{i}: {answers[i]}')

def main(n_questions, random_seed=None):
    random.seed(random_seed)

    num_1 = [random.randint(2, 12) for _ in range(n_questions)]
    num_2 = [random.randint(2, 12) for _ in range(n_questions)]

    answers = [a * b for a, b in zip(num_1, num_2)]

    print_questions(num_1, num_2)
    print_answers(answers)
    create_pdf_questions(num_1, num_2)
    create_pdf_answers(answers)

if __name__ == '__main__':
    main(20)

        