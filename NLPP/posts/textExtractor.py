"""
Takes text from pdf or other formats and returns the text as a string
use convertToText with given file path to find the file
"""

# Resolve Certificate errors with nltk module
# import os, ssl
# if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
#     ssl._create_default_https_context = ssl._create_unverified_context
# https://medium.com/@rqaiserr/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f
# Credit for the below function above
def PDFConverter(lang, filename):
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    import PyPDF2
    import textract

    #open allows you to read the file
    pdfFileObj = open(filename,'rb')
    #The pdfReader variable is a readable object that will be parsed
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #discerning the number of pages will allow us to parse through all #the pages
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    #The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
    #This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
    if text != "":
       text = text
    #If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
    else:
       text = textract.process(fileurl, method='tesseract')
    # Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
    # Now, we will clean our text variable, and return it as a list of keywords.
    #The word_tokenize() function will break our text phrases into #individual words
    tokens = word_tokenize(text)
    #we'll create a new list which contains punctuation we wish to clean
    punctuations = ['(',')',';',':','[',']',',']
    #We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
    #stop_words = stopwords.words('english')
    #We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
    #keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
    # Use tokens instead of keywords instead if want no repitition
    return(' '.join(tokens))

# Credit to https://medium.com/@MicroPyramid/extract-text-with-ocr-for-all-image-types-in-python-using-pytesseract-ec3c53e5fc3a
# for this image to text code
def imageToText(filename, lang="eng"):
    try:
        from PIL import Image
    except ImportError:
        import Image
    import pytesseract

    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

def convertToText(filename, lang):
    extension = filename[filename.index(".")+1:]
    text = "[WARNING] Text extraction is not 100% accurate, please review what was generated\n"
    try:
        if (extension == "pdf"):
            text += PDFConverter(lang,filename)
        elif (extension == "png"):
            text += imageToText(filename, lang="english")
        else:
            text = "[ERROR]: Unsupported File Type"
    except FileNotFoundError:
        text = "[ERROR]: File not found"

    return text

#print(convertToText("media/posts/temp/sample.pdf", "english"))
#print(convertToText("media/posts/temp/pdf_sample.pdf", "english"))