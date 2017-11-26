
all: config.dat

config.dat: Brain.java
	python3.5 -m make_dat > $@

Brain.java: sb.pkl
	python3.5 -m sklearn_porter -i $^ --language java --pipe > Brain.java

sb.pkl: observations.txt
	python3.5 make_classifier.py $^ $@

.PHONY: clean validate

validate:
	python3.5 validate.py observations.txt

clean:
	rm -f Brain.java Brain.class sb.pkl config.dat
