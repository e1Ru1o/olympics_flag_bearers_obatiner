.DEFAULT_GOAL 	:= help

year			:= 1936

list: ## download the page of flag baerers per country
	python list_downloader.py

countries: ## download the page of flag baerers per country
	python countries_downloader.py -y $(year)

view: ## display the Makefile
	@cat Makefile

edit: ## open the Makefile with `code`
	@code Makefile

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

