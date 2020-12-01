from flask import Flask, render_template, request, url_for
from dbconnect import connect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
   return render_template('home.html')


@app.route('/scatter_plot', methods=["GET","POST"])
def scatter_plot():
	sql = "select latitude, longitude, mag from all_month"# where latitude between ? and ? and longitude between ? and ?;"
	cursor = connect.cursor()
	cursor.execute(sql)#, (latitude - step, latitude + step, longitude - step, longitude + step))
	result = cursor.fetchall()
	return render_template('scatter_plot.html', result=result, size=len(result))#, latitude_range=latitude_range, longitude_range =longitude_range)

@app.route('/line_chart', methods=["GET","POST"])
def line_chart():
	sql ="select t.ranges as magnitudes, count(*) as occurences from (select case when mag >= 0 and mag < 1 then 0 when mag >= 1 and mag < 2 then 1 when mag >= 2 and mag < 3 then 2 when mag >= 3 and mag < 4 then 3 when mag >= 4 and mag < 5 then 4 when mag >= 5 and mag < 6 then 5 when mag >= 6 and mag < 7 then 6 when mag >= 7 and mag < 8 then 7 when mag >= 8 and mag < 9 then 8 when mag >= 9 and mag < 10 then 9 else -1 end as ranges from all_month) t group by t.ranges order by magnitudes;"
	cursor = connect.cursor()
	cursor.execute(sql)

	return render_template('line_chart.html', result=cursor.fetchall())

def get_mag_data():
	cursor = connect.cursor()
	sql = """SELECT t.range as magnitudes, count(*) as occurance from (
		SELECT CASE WHEN mag >= 0 and mag < 1 THEN 0
		 WHEN mag >= 1 and mag < 2 THEN 1
		 WHEN mag >= 2 and mag < 3 THEN 2
		 WHEN mag >= 3 and mag < 4 THEN 3
		 WHEN mag >= 4 and mag < 5 THEN 4
		 WHEN mag >= 5 and mag < 6 THEN 5
		 WHEN mag >= 6 and mag < 7 THEN 6
		 WHEN mag >= 7 and mag < 8 THEN 7
		 WHEN mag >= 8 and mag < 9 THEN 8
		 WHEN mag >= 9 and mag < 10 THEN 9
		 ELSE -1 END as range from all_month) t group by t.range order by magnitudes"""
	cursor.execute(sql)
	return cursor.fetchall()

@app.route('/pie_chart', methods=["GET","POST"])
def pie_chart():
	result = get_mag_data()
	return render_template('pie_chart.html', result=result)

@app.route('/bar_chart', methods=["GET","POST"])
def bar_chart():
	result = get_mag_data()
	return render_template('bar_chart.html', result=result)