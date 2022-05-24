from flask import Flask, render_template
import Utils

app = Flask("mainScores")


@app.route('/')
def read_score():
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as read_file:
            content = read_file.read()
            return render_template('scoreHTML.html', SCORE=content)
    except:
        return render_template('ErrorHTML.html', ERROR=Utils.BAD_RETURN_CODE)


if __name__ == '__main__':
    app.run(debug=True)
