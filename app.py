from flask import Flask, render_template, request, jsonify
import PyPDF2

app = Flask(__name__)

# Global variable to store extracted PDF text
pdf_text = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global pdf_text
    if 'pdf' not in request.files:
        return jsonify({'error': 'No PDF file uploaded'}), 400
    file = request.files['pdf']
    
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_text = ''
        for page_num in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page_num].extract_text()
        
        return jsonify({'message': 'PDF uploaded successfully'})
    
    except Exception as e:
        return jsonify({'error': 'Failed to process PDF'}), 500

@app.route('/ask', methods=['POST'])
def ask():
    global pdf_text
    question = request.form.get('question')
    
    if not pdf_text:
        return jsonify({'error': 'No PDF text found. Please upload a PDF first.'}), 400
    
    # Here you would add your logic for answering the question
    # For simplicity, we will check if a word from the question exists in the PDF text.
    if question in pdf_text:
        answer = f"Yes, the word '{question}' is found in the document."
    else:
        answer = f"No, the word '{question}' is not found in the document."
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
