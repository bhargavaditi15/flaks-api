from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
# Example extracted text (for illustration)
details = [
    {
        # "id": 1,
        "Certification": "110364249R",
        "CertificationDesignations": "TLL",
        "IssuedTo": "DENNIS W. BARR",
        "Issued": "03/31/2021",
        "Expires": "03/31/2026"
    },
    {
        # "id": 2,
        "Certification": "555240732",
        "CertificationDesignations": "",
        "IssuedTo": "DUSTIN D. WARNER",
        "Issued": "",
        "Expires": ""
    },
    {
        # "id": 3,
        "Certification": "R020712246",
        "CertificationDesignations": "TLL,TSS,STC",
        "IssuedTo": "PAUL E. BURACKER",
        "Issued": "7/31/2022",
        "Expires": "7/31/2027"
    },
    { 
        # "id": 4,
        "Certification": "2106206751",
        "CertificationDesignations": "TLL",
        "IssuedTo": "FRANCIS J. MEIGHAN",
        "Issued": "6/30/2021",
        "Expires": "06/30/2026"
    },
    {
    #  "id": 5,
        "Certification": "99078087R",
        "CertificationDesignations": "TLL,TSS,BTF,STC",
        "IssuedTo": "WILLIAM S. FOUT JR",
        "Issued": "07/31/2019",
        "Expires": "07/31/2024"
    },
     {
        #  "id": 6,
        "Certification": "2102200605",
        "CertificationDesignations": "TLL,TSS,BTF,STC",
        "IssuedTo": "KEVIN W. FOUT",
        "Issued": "02/28/2021",
        "Expires": "02/28/2026"
    },
     {
        #  "id": 7,
        "Certification": "1606126791R",
        "CertificationDesignations": "TLL,TSS,BTF,STC",
        "IssuedTo": "JASON E. JOHNSON",
        "Issued": "06/30/2021",
        "Expires": "06/30/2026"
    }

]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app/api/details/all')
def show():
    return jsonify(details)

@app.route('/app/api/details', methods=['GET'])
def id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "unknown request"
    
    result = []

    for detail in details:
        if detail['id'] == id:
            result.append(detail)
    return jsonify(result)


# if __name__ == '__main__':
#     app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
