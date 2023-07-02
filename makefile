output := output
resource := resources

source := $(firstword $(wildcard *.tex))
target := $(patsubst %.tex,%.pdf,${source})

sources := $(shell find . -type f -name "*.tex")
resources := $(shell find ${resource} -type f -name "*")

${target}: ${source} ${sources} ${resources}
	@mkdir -p ${output}
	@texfot pdflatex --output-directory=${output} $<
	@texfot pdflatex --output-directory=${output} $<
	@mv ${output}/${target} $@

.PHONY: force clean

force: clean ${target}

clean:
	@rm -f ${target}
	@rm -rf ${output}


