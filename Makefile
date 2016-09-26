dpdd.pdf:  dpdd.tex gliffy/*.pdf
	latexmk -bibtex -pdf -f dpdd.tex

.PHONY: web
web: dpdd.pdf
	python deployment/builder.py --template deployment/index.jinja2 --pdf dpdd.pdf --build-dir _build

.DEFAULT_GOAL := web

.PHONY: clean
clean:
	rm -f dpdd.aux
	rm -f dpdd.fdb_latexmk
	rm -f dpdd.fls
	rm -f dpdd.log
	rm -f dpdd.out
	rm -f dpdd.pdf
	rm -f dpdd.toc
	rm -f -R _build
