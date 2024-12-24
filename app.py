from flask import Flask, render_template, request, jsonify
from covid import Covid

app = Flask(__name__)
cv = Covid(source="worldometers")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_covid_data', methods=['POST'])
def get_covid_data():
    choice = request.form['choice']

    try:
        if choice == '2':
            active = cv.get_total_active_cases()
            return jsonify({'active_cases': active})
        elif choice == '3':
            confirmed = cv.get_total_confirmed_cases()
            return jsonify({'confirmed_cases': confirmed})
        elif choice == '4':
            recovered = cv.get_total_recovered()
            return jsonify({'recovered_cases': recovered})
        elif choice == '5':
            deaths = cv.get_total_deaths()
            return jsonify({'death_cases': deaths})
        elif choice == "country":
            countries = cv.list_countries()
            return jsonify({"countries": countries})
        elif choice == "india":
            india = cv.get_status_by_country_name("India")
            return jsonify({"India": india})
        elif choice == "italy":
            italy = cv.get_status_by_country_name("Italy")
            return jsonify({"Italy": italy})
        elif choice == "canada":
            canada = cv.get_status_by_country_name("Canada")
            return jsonify({"Canada": canada})
        elif choice == "usa":
            usa = cv.get_status_by_country_name("USA")
            return jsonify({"USA": usa})
        else:
            return jsonify({"error": "Invalid choice"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
