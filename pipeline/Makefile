# KneeSchool content pipeline.
#
#   make test      run the test suite, no AWS account needed
#   make lint      run the style gate over a draft: make lint DRAFT=path/to.md
#   make build     stage the config files the Lambda bundles need, then sam build
#   make deploy    guided deployment; asks for the account, region and parameters
#
# build and deploy need the AWS SAM CLI and credentials for the target account.

PYTHON ?= python3
DRAFT  ?= tests/fixtures/clean_1.2.3.md
BRIEF  ?= config/briefs/1.2.3.json
ENV    ?= dev
STACK  ?= kneeschool-pipeline-$(ENV)

.PHONY: test lint build deploy clean validate

test:
	cd .. && $(PYTHON) -m unittest discover -s pipeline/tests -v

lint:
	$(PYTHON) tools/lint_local.py $(DRAFT) --brief $(BRIEF)

# The style gate Lambda needs the rule file inside its own bundle. It is copied
# at build time so pipeline/config stays the single source of truth.
stage-config:
	cp config/lint_rules.json functions/style_lint/lint_rules.json

validate: stage-config
	sam validate --lint --template infra/template.yaml

build: stage-config
	sam build --template infra/template.yaml

deploy: build
	sam deploy --guided --stack-name $(STACK) \
	  --capabilities CAPABILITY_IAM \
	  --tags project=kneeschool environment=$(ENV)

clean:
	rm -f functions/style_lint/lint_rules.json
	rm -rf .aws-sam
	find . -name '__pycache__' -type d -prune -exec rm -rf {} +
