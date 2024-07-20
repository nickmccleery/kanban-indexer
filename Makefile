PHONY: .clean .build .deploy-test

clean:
	rm -rf dist

build:
	python -m build

deploy-test:
	twine upload --repository testpypi dist/*