PHONY: .clean .build .deploy-test .deploy

clean:
	rm -rf dist

build:
	python -m build

deploy-test:
	twine upload --repository testpypi dist/*

deploy:
	twine upload --verbose --config-file .pypirc dist/*