from flask import Flask, Response, redirect, render_template_string

app = Flask(__name__)

# ---- Replace with your links ----
PDF_LINK = "https://drive.google.com/uc?export=download&id=1RS9hI5pjzQrh0dWc0ln-JnzzbyO6AnE0"
VCF_CONTENT = """BEGIN:VCARD
VERSION:3.0
N:Sarawagi;Rakesh;;;
FN:Rakesh Sarawagi
TITLE:Director
ORG:Siddhi Vinayak Knots & Prints Pvt Ltd (Laxmipati Group)
EMAIL;TYPE=work:garments@laxmipati.com
TEL;TYPE=work,voice:+91XXXXXXXXXX
ADR;TYPE=work:;;A-26, Central Park, G.I.D.C, Pandesara;Surat;Gujarat;;India
ADR;TYPE=work:;;1168-93, Abhishek Textile Market, Ring Road;Surat;Gujarat;;India
ADR;TYPE=work:;;4103, J.J. A/c Market, Ring Road;Surat;Gujarat;;India
URL:https://www.laxmipati.com
END:VCARD
"""

@app.route("/")
def home():
    # This HTML triggers vCard download + opens PDF
    html = f"""
    <html>
    <head>
      <title>Laxmipati Sarees</title>
      <meta http-equiv="refresh" content="3;url={PDF_LINK}" />
    </head>
    <body>
      <h2>Saving Contact + Opening Brochure...</h2>
      <script>
        function downloadVCF() {{
            var vcfData = `{VCF_CONTENT}`;
            var blob = new Blob([vcfData], {{ type: 'text/vcard' }});
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = "Laxmipati_Sarees.vcf";
            link.click();
        }}
        downloadVCF();
      </script>
      <p>If brochure doesn’t open automatically, <a href="{PDF_LINK}">click here</a>.</p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
