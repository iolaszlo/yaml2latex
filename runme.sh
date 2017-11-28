#!/bin/bash



######Yaml input location and input files
YAML_DIR="./example"
YAML_FILE="resume.yaml"

###### Template location
TEMPLATE_DIR="example/template"

#### Body and header file are located in TEMPLATE_DIR
HEADER="cvhead1.tex"
BODY="cvbody1.tex"

###### Output file is captured from standard output
RESULT="example/cv.tex"


./mkresume.py --yaml ${YAML_DIR}/${YAML_FILE} --tpath ${TEMPLATE_DIR} --body ${BODY}  --header ${HEADER}  >$RESULT
