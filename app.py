@app.route('/', methods = ['POST'])
def main():
	return render_template("index.html", result=answer, equation = equation)
	request.get(result).json()
	<input placeholder = "Expression" name="text"