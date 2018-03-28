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

Create Function called "check_fizz_and_fuzz", if-else

		check_fizz_and_fuzz <- function(x){
		if (x %% 3 == 0 & x %% 5 == 0) {
		out <- c("FizzFuzz")
		} else if (x %% 3 == 0) {
		out <- c("Fizz")
		} else if (x %% 5 == 0) {
		out <- c("Fuzz")
		} else if(x %% 7 < 4) {
		out <- c("Hi")
		} else {
		out <- c("Bye")
		}
		return(out)
		}

Use loop ans sapply to compare calculate speed

		a <- c(1:1000)
		start.time <- Sys.time()
		sapply(a, check_fizz_and_fuzz)
		end.time <- Sys.time()
		time.taken <- end.time - start.time
		time.taken

		start.time <- Sys.time()
		for (i in a){
		    print(check_fizz_and_fuzz(i))}
		end.time <- Sys.time()
		time.taken <- end.time - start.time
		time.taken

Find disp above median in mtcar
		data("mtcar")
		x <- which(mtcars$disp > median(mtcars$disp, na.rm = FALSE))
		mtcars[x,]
