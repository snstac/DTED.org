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
	@for zipfile in data/src/*.zip; do \
		dirname=$$(basename $$zipfile .zip | cut -d'-' -f1); \
		echo "Processing $$zipfile for $$dirname..."; \
		tmpdir=$$(mktemp -d); \
		echo "Unzipping $$zipfile to $$tmpdir..."; \
		unzip $$zipfile -d $$tmpdir; \
		echo "Moving files to data/build/in/$$dirname..."; \
		rm -rf data/build/in/$$dirname; \
		mkdir -p data/build/in/$$dirname; \
		mv $$tmpdir/*/* data/build/in/$$dirname; \
		echo "Creating index for $$dirname..."; \
		python3 tools/create_index.py data/build/in/$$dirname data/build/out/$$dirname; \
		rm -rf $$tmpdir; \
	done
	@echo "Data processing complete."

# Target to repack DTED files
repack-dted:
	@echo "Repacking DTED files..."
	@for build_dir in data/build/out/*; do \
			if [ -d "$$build_dir" ]; then \
					dirname=$$(basename $$build_dir); \
					echo "Repacking $$dirname..."; \
					tmpdir=$$(mktemp -d); \
					unzip -q data/stream/elevation/DTED/dted_nw_hemi.zip -d $$tmpdir; \
					cp -r $$build_dir/* $$tmpdir/; \
					(cd $$tmpdir && zip -qr ../../data/stream/$$dirname/dted_nw_hemi.zip .); \
					rm -rf $$tmpdir; \
			fi; \
	done
	@echo "Repacking complete."

build-index:
	@echo "Building HTML index from README.md..."
	@pandoc README.md -o web/html/index.html -f markdown --template web/html/standalone.html

# Target to convert noun.png into favicon.ico
create-favicon:
	@echo "Converting web/media/noun.png to favicon.ico..."
	@convert web/html/media/noun-elevation-5901019.png -define icon:auto-resize=64,48,32,16 web/html/favicon.ico
	@echo "favicon.ico created at web/html/favicon.ico."

.PHONY: all clean install-nginx-conf enable-nginx-conf disable-nginx-conf process-data repack-dted build-index create-favicon


# build-simple-dted:
# 	@echo "Processing data..."
	
# 	@mkdir -p data/simple
# 	@mkdir -p data/build
# 	@mkdir -p data/src
# 	@mkdir -p data/stream/elevation/DTED
# 	@rm -rf data/build/in/*
# 	@rm -rf data/build/out/*
# 	@mkdir -p data/build/in
# 	@mkdir -p data/build/out

# 	@for zipfile in data/src/*.zip; do \
# 		echo "Processing $$zipfile..."; \
# 		dirname=$$(basename $$zipfile .zip); \
# 		tmpdir=$$(mktemp -d); \

# 		echo "Unzipping $$zipfile to $$tmpdir..."; \
# 		unzip $$zipfile -d $$tmpdir; \ 

# 		echo "Moving files to data/build/in/$$dirname..."; \
# 		mkdir -p data/build/in/$$dirname; \
# 		mv $$tmpdir/*/* data/build/in/$$dirname; \

# 		echo "Creating index for $$dirname..."; \
# 		python3 tools/create_index.py $$tmpdir data/build/$$dirname; \
# 		rm -rf $$tmpdir; \
# 	done
# 	@echo "Data processing complete."
