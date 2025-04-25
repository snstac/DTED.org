#!/bin/bash

pandoc README.md -o web/html/index.html -f markdown --template web/html/standalone.html