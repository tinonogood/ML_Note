At cmd line: search help for fuction as.numeric

		help("as.numeric")

Check pkg "data.table", "e1071" and install them 

		"data.table" %in% rownames(installed.packages())
		View(installed.package)

		install.packages("data.table")

Vector(1,4,2,NA,7,20,NA,15,10,5), replace NA by median

		library(Hmisc)
		v_new <- impute(v, median)

Check datatype of all row from https://goo.gl/ByTnpD

		movie = read.csv("https://goo.gl/ByTnpD", sep="|", stringsAsFactors = FALSE)
		str(movie)

Change type of "box" to num, sum top10 & bottom10

		movie$box_numeric <- as.numeric(gsub("\\$", "", movie$box))
		movie$box_numeric, decreasing = T)[1:10]
		sum(sort(movie$box_numeric)[1:10])

Creat "year.pass", calulate avg_box

		movie$year.pass = as.numeric(substr(Sys.Date(),1,4))- as.numeric(str_sub(movie$date, -4, -1))

		movie$avg_box = movie$box_numeric / movie$year.pass

