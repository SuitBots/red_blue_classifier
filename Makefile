
all: Brain.java

Brain.java: sb.pkl
	python3.5 -m sklearn_porter -i $^ --language java

sb.pkl: observations.txt
	python3.5 make_classifier.py $^ $@

.PHONY: clean validate

validate:
	python3.5 validate.py observations.txt

clean:
	rm -f Brain.java sb.pkl
