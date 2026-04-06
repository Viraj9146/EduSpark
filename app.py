from flask import Flask, render_template, request

# Create Flask app FIRST
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    subject = request.form.get('subject')

    if not subject or subject.strip() == "":
        return render_template("index.html", message="Please enter a subject.")

    subject = subject.strip()
    formatted = subject.replace(" ", "+")

    links = [
        ("🎥 YouTube Video Tutorials",
         f"https://www.youtube.com/results?search_query={formatted}+lecture"),

        ("📘 Google Notes & Study Material",
         f"https://www.google.com/search?q={formatted}+notes+pdf"),

        ("📖 Wikipedia Overview",
         f"https://en.wikipedia.org/wiki/{subject.replace(' ', '_')}"),

        ("🧠 Research Articles (Google Scholar)",
         f"https://scholar.google.com/scholar?q={formatted}"),

        ("📚 Free Courses (Coursera Search)",
         f"https://www.coursera.org/search?query={formatted}"),

        ("💻 Practice Questions",
         f"https://www.google.com/search?q={formatted}+practice+questions")
    ]

    return render_template("index.html", links=links, subject=subject)

if __name__ == '__main__':
    app.run(debug=True)