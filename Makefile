# Makefile for downloading DTED files, managing Nginx configuration, and processing data

# URLs of the files to download
FILES = \
	https://tak.gov/elevation/DTED/dted_ne_hemi.zip \
	https://tak.gov/elevation/DTED/dted_nw_hemi.zip \
	https://tak.gov/elevation/DTED/dted_se_hemi.zip \
	https://tak.gov/elevation/DTED/dted_sw_hemi.zip

# Extract the filenames from the URLs
TARGETS = $(notdir $(FILES))

# Destination folder for downloaded files
DEST_DIR = data/stream/elevation/DTED

.PHONY: all clean install-nginx-conf enable-nginx-conf disable-nginx-conf process-data repack-dted build-index create-favicon resize-image

# Default target
all: $(addprefix $(DEST_DIR)/, $(TARGETS))

# Rule to download each file into the destination folder
$(DEST_DIR)/%: 
	@echo "Downloading $@..."
	@mkdir -p $(DEST_DIR)
	@curl -L -o $@ $(filter %$(@F), $(FILES))

# Clean target to remove downloaded files
clean:
	@echo "Cleaning up downloaded files..."
	@rm -f $(addprefix $(DEST_DIR)/, $(TARGETS))
	@rm -rf data/build/in/*
	@rm -rf data/build/out/*

# Target to install Nginx configuration
install-nginx-conf:
	@echo "Installing Nginx configuration..."
	@sudo cp web/DTED.org-nginx.conf /etc/nginx/sites-available/DTED.org
	@echo "Configuration installed to /etc/nginx/sites-available/DTED.org"

# Target to enable Nginx configuration
enable-nginx-conf:
	@echo "Enabling Nginx configuration..."
	@sudo ln -sf /etc/nginx/sites-available/DTED.org /etc/nginx/sites-enabled/DTED.org
	@sudo nginx -t && sudo systemctl reload nginx
	@echo "Nginx configuration enabled and reloaded."

# Target to disable Nginx configuration
disable-nginx-conf:
	@echo "Disabling Nginx configuration..."
	@sudo rm -f /etc/nginx/sites-enabled/DTED.org
	@sudo nginx -t && sudo systemctl reload nginx
	@echo "Nginx configuration disabled and reloaded."

# Target to process data from zip files
build-simple-dted:
	@echo "Building Simple DTED Server data files..."
	@mkdir -p data/simple
	@mkdir -p data/build
	@mkdir -p data/src
	@mkdir -p data/stream/elevation/DTED
	@mkdir -p data/build/in
	@mkdir -p data/build/out
	@bash tools/build_simple_dted.sh
	@echo "Data processing complete."

repack-dted:
	@bash tools/repack_dted.sh

build-index:
	@bash tools/build_index.sh

create-favicon:
	@convert web/html/media/DTED.org.png -define icon:auto-resize=64,48,32,16 web/html/favicon.ico

resize-images:
	@bash tools/resize_images.sh

web: build-index create-favicon resize-images
nginx: install-nginx-conf enable-nginx-conf
process-data: build-simple-dted repack-dted
	@echo "Processing data complete."
	@echo "Run 'make web' to build the HTML index and favicon."
	@echo "Run 'make nginx' to install and enable the Nginx configuration."
	@echo "Run 'make clean' to remove downloaded files and build artifacts."
	@echo "Run 'make all' to download files and process data."
	@echo "Run 'make clean' to remove downloaded files and build artifacts."

mkdocs:
	pip install -r docs/requirements.txt
	mkdocs serve
