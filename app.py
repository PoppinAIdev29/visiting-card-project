from flask import Flask, send_file, render_template_string

app = Flask(__name__)

# ---- Replace with your links ----
PDF_LINK = "https://drive.google.com/uc?export=download&id=1RS9hI5pjzQrh0dWc0ln-JnzzbyO6AnE0"
VCF_FILE = "Laxmipati_Sarees.vcf"  # save this file in your project folder

@app.route("/")
def home():
    # HTML triggers vCard download + redirects to PDF
    html = f"""
    <html>
    <head>
      <title>Laxmipati Sarees</title>
      <meta http-equiv="refresh" content="5;url={PDF_LINK}" />
    </head>
    <body>
      <h2>Saving Contact + Opening Brochure...</h2>
      <script>
        // Redirect to vCard download route
        window.location.href = "/download";
      </script>
      <p>If brochure doesn’t open automatically, <a href="{PDF_LINK}" target="_blank">click here</a>.</p>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route("/download")
def download_vcf():
    # Sends the vCard file for automatic download
    return send_file(VCF_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
