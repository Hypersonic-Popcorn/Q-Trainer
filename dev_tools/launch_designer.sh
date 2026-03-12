#!/usr/bin/env bash
# launch_designer.sh
#
# Activates the Q-Trainer venv and launches pyside6-designer with
# pl-widgets plugins loaded.
#
# Fixes the venv plugin-loading bug on Linux by adding the base Python
# lib directory to LD_LIBRARY_PATH, so the Designer plugin (libPySidePlugin.so)
# can find libpython3.11.so at runtime.
#
# Usage:
#   chmod +x launch_designer.sh
#   ./launch_designer.sh

VENV_DIR="../venv"
PLUGIN_DIR="../designer_plugins"

# Activate the venv
source "$VENV_DIR/bin/activate"

# Find the base Python executable (outside the venv) and its lib directory.
# This is needed because pyside6-designer's C++ plugin loader needs to find
# libpython3.11.so, which lives alongside the base (non-venv) Python binary.
BASE_PYTHON=$(python -c "import sys; print(sys._base_executable)")
BASE_PYTHON_DIR=$(dirname "$BASE_PYTHON")

# Walk up from the bin/ dir to find the lib/ dir containing libpython3.11.so
# Typically: /usr/lib, /usr/local/lib, or /usr/lib/x86_64-linux-gnu
PYTHON_LIB_DIR=$(python -c "
import sysconfig, os
libdir = sysconfig.get_config_var('LIBDIR')
print(libdir if libdir else '')
")

# Tell Designer where to find the plugins
export PYSIDE_DESIGNER_PLUGINS="$PLUGIN_DIR"

# Add the Python lib directory so libPySidePlugin.so can find libpython3.11.so
if [ -n "$PYTHON_LIB_DIR" ]; then
    export LD_LIBRARY_PATH="$PYTHON_LIB_DIR:${LD_LIBRARY_PATH:-}"
fi

echo "Launching pyside6-designer..."
echo "  VENV:                     $VENV_DIR"
echo "  PYSIDE_DESIGNER_PLUGINS:  $PLUGIN_DIR"
echo "  BASE_PYTHON:              $BASE_PYTHON"
echo "  LD_LIBRARY_PATH:          $LD_LIBRARY_PATH"
echo ""

pyside6-designer "$@"
