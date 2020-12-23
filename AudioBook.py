import pyttsx3  # Load Python Text To Speech version 3
import PyPDF2  # Load PDF manipulator

book = open("E:\Subject\Syllabus.pdf", "rb")  # give the Path of PDF file and open in read mode
pdfReader = PyPDF2.PdfFileReader(book)  # create a prf reader object

pages = pdfReader.numPages
print("Total page in Book:", pages)
starting_page = 6  # give the page number wheres the reading will start

speaker = pyttsx3.init()  # initialize a speaker

for num in range(starting_page, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)  # print the text of PFD
    speaker.say(text)  # Read the text
    speaker.runAndWait()
book.close()
print("END")
