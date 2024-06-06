import matplotlib

matplotlib.use("Agg")
from flask import Flask, render_template, request, send_file
import BB
import BT

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", table_generated = False)

@app.route("/generate_table", methods=["POST"])
def generate_table():
    try:
        bc = BB.formula(int(request.form["budget"]))

        if bc['components'] is None:
            return render_template(
                "index.html",
                table_generated = False,
                error = "No combination found within the budget."
            )

        return render_template(
            "index.html",
            table_generated=True,
            cpu_name = bc['components'][0][0],
            gpu_name = bc['components'][1][0],
            ram_name = bc['components'][2][0],
            ssd_name = bc['components'][3][0],
            cpu_price = bc['components'][0][1],
            gpu_price = bc['components'][1][1],
            ram_price = bc['components'][2][1],
            ssd_price = bc['components'][3][1],
            cpu_score = bc['components'][0][2],
            gpu_score = bc['components'][1][2],
            ram_score = bc['components'][2][2],
            ssd_score = bc['components'][3][2],
            cpu_url = f"https://www.amazon.com/s?field-keywords={bc['components'][0][0].replace(' ', '+')}&ref=cs_503_search",
            gpu_url = f"https://www.amazon.com/s?field-keywords={bc['components'][1][0].replace(' ', '+')}&ref=cs_503_search",
            ram_url = f"https://www.amazon.com/s?field-keywords={bc['components'][2][0].replace(' ', '+')}&ref=cs_503_search",
            ssd_url = f"https://www.amazon.com/s?field-keywords={bc['components'][3][0].replace(' ', '+')}&ref=cs_503_search",
            tot_score = bc['total_benchmark'],
            tot_price = bc['total_price']
        )

    except Exception as e:
        return render_template(
            "index.html", 
            table_generated=False,
            error = str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)