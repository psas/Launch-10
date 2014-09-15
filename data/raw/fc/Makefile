SRC=$(wildcard *.log)

all:
	for f in $(SRC) ; do \
		python logfile_to_csv.py $$f > $$f.csv ; \
		echo Finish $$f ; \
	done

clean:
	for f in $(SRC) ; do \
		rm -f $$f.csv ; \
	done
