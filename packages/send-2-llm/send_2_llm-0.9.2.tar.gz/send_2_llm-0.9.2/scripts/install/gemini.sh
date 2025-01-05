#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Required Python version
REQUIRED_PYTHON_VERSION="3.11"

# Function to check Python version
check_python_version() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Python 3 is not installed!${NC}"
        echo -e "Please install Python ${REQUIRED_PYTHON_VERSION} or higher:"
        echo -e "sudo apt update"
        echo -e "sudo apt install python${REQUIRED_PYTHON_VERSION}"
        exit 1
    fi

    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    
    if [ "$(printf '%s\n' "$REQUIRED_PYTHON_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_PYTHON_VERSION" ]; then
        echo -e "${RED}Error: Python ${REQUIRED_PYTHON_VERSION}+ is required, but Python ${PYTHON_VERSION} is installed${NC}"
        echo -e "\nTo install Python ${REQUIRED_PYTHON_VERSION}:"
        echo -e "1. sudo apt update"
        echo -e "2. sudo apt install python${REQUIRED_PYTHON_VERSION}"
        echo -e "3. sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python${REQUIRED_PYTHON_VERSION} 1"
        exit 1
    fi
    
    echo -e "${GREEN}✓ Using Python ${PYTHON_VERSION}${NC}"
}

# Function to check and uninstall old dependencies
check_and_uninstall() {
    local package=$1
    if pip show $package >/dev/null 2>&1; then
        echo -e "${YELLOW}Found old dependency: $package. Uninstalling...${NC}"
        pip uninstall -y $package
    fi
}

# Check Python version first
echo -e "${YELLOW}Checking Python version...${NC}"
check_python_version

# Check and remove old dependencies
echo -e "${YELLOW}Checking for old dependencies...${NC}"
check_and_uninstall "google-cloud-aiplatform"
check_and_uninstall "google-api-core"
check_and_uninstall "google-generativeai"
check_and_uninstall "protobuf"

# Update pip
echo -e "${YELLOW}Updating pip...${NC}"
python3 -m pip install --upgrade pip

# Install dependencies
echo -e "${YELLOW}Installing Gemini dependencies...${NC}"
python3 -m pip install -U -q "google-generativeai>=0.7.2" "protobuf>=5.0.0"

# Verify installation
echo -e "${YELLOW}Verifying installation...${NC}"
if python3 -m pip show google-generativeai >/dev/null 2>&1 && python3 -m pip show protobuf >/dev/null 2>&1; then
    echo -e "${GREEN}Installation completed successfully!${NC}"
    echo -e "\nInstalled versions:"
    python3 -m pip show google-generativeai | grep Version
    python3 -m pip show protobuf | grep Version
    
    echo -e "\n${GREEN}✓ Ready to use Gemini with Python $(python3 --version)${NC}"
else
    echo -e "${RED}Installation verification failed!${NC}"
    exit 1
fi 