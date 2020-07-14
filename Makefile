export TEXMFHOME ?= lsst-texmf/texmf

dpdd.pdf:  dpdd.tex gliffy/*.pdf
	latexmk -bibtex -pdf -f dpdd.tex

.DEFAULT_GOAL := dpdd.pdf

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
